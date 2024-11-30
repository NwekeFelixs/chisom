from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from.forms import UserProfileForm, CustomUserCreationForm
from django.contrib.auth import get_user_model


from.models import Blog, Category, Comment, Like, SubCategory, Tag

# Create your views here.

def blog(request):
    blogs = Blog.objects.all().order_by('-created')  # Get all posts and order by newest
    categories = Category.objects.all()  # Fetch all categories
    tags = Tag.objects.all() # Fetch all tags

    # Set up pagination
    paginator = Paginator(blogs, 5)  # Show 5 blogs per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'somy/blog.html', {'page_obj': page_obj, 'categories': categories, tags: 'tags'})



def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # Automatically log in the user after registration
            messages.success(request, 'Account created successfully!')
            return redirect('blog')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomUserCreationForm()

    return render(request, 'somy/register.html', {'form': form})


def blogdetail(request, id):
    blog = get_object_or_404(Blog, id=id)
    comments = Comment.objects.filter(blog=blog)
    categories = Category.objects.all()  # Fetch all categories

    # Fetch related blogs in the same category
    related_blogs = Blog.objects.filter(category=blog.category).exclude(id=blog.id)  # Exclude the current blog

    return render(request, 'somy/blogpost.html', {
        'blog': blog,
        'comments': comments,
        'categories': categories,
        'related_blogs': related_blogs,
    })


def user_login(request):  # Rename this view function
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            auth_login(request, user)  # Use the renamed 'auth_login' to avoid conflict
            return redirect('blog')
        else:
            messages.error(request, 'Invalid email or password')
            return render(request, 'somy/login.html', {'email': email})
    
    return render(request, 'somy/login.html')

def logout(request):
    auth_logout(request)  # Log the user out
    messages.success(request, 'Successfully logged out!')
    return redirect('blog')  # Redirect to the blog page

@login_required
def profile(request):
    user = request.user
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile was updated successfully!')
            return redirect('profile')  # Redirect to profile page after saving
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserProfileForm(instance=user)

    return render(request, 'somy/profile.html', {'form': form})

    

@login_required
def add_comment(request, blog_id):
    if request.method == 'POST':
        blog = get_object_or_404(Blog, id=blog_id)
        comment_content = request.POST.get('comment')
        Comment.objects.create(blog=blog, user=request.user, comment=comment_content)
        return redirect('blogdetail', id=blog.id)
    
    # Optional: you could also handle GET requests if needed
    return redirect('blogdetail', id=blog_id)  # Redirect if GET request


@login_required
def like_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)

    # Get the actual user instance
    user = get_user_model().objects.get(id=request.user.id)

    # Check if the user has already liked the blog
    if blog.likes.filter(user=user).exists():
        # User already liked the blog, so unlike it
        blog.likes.get(user=user).delete()
    else:
        # Add a new like
        Like.objects.create(user=user, blog=blog)

    return redirect('blogdetail', id=blog_id)



def blogs_by_category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    blogs_list = Blog.objects.filter(category=category, published=True).order_by('-created')
    categories = Category.objects.all()  # Get all categories
    tags = Tag.objects.all() 

    paginator = Paginator(blogs_list, 5)  # Show 10 blogs per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'somy/blog_category.html', {'category': category, 'blogs': page_obj, 'tags': tags, 'categories': categories})

def blogs_by_subcategory(request, subcategory_slug):
    subcategory = get_object_or_404(SubCategory, slug=subcategory_slug)
    blogs = Blog.objects.filter(subcategory=subcategory, published=True).order_by('-created')
    
    return render(request, 'blogs_by_subcategory.html', {'subcategory': subcategory, 'blogs': blogs})

def blogs_by_tag(request, tag_slug):
    tag = get_object_or_404(Tag, slug=tag_slug)
    blogs = Blog.objects.filter(tags=tag, published=True).order_by('-created')
    
    return render(request, 'blogs_by_tag.html', {'tag': tag, 'blogs': blogs})



def newsletter_signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        NewsletterSubscription.objects.create(email=email)  # Save the email
        return redirect('thank_you_page')  # Adjust to your actual thank you page
    return HttpResponse("Invalid request", status=400)
