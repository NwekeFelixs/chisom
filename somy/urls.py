from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('blog/<int:id>/', views.blogdetail, name='blogdetail'),  
    path('profile/', views.profile, name='profile'),
    path('blog/<int:blog_id>/add_comment/', views.add_comment, name='add_comment'),
    path('like/<int:blog_id>/', views.like_blog, name='like_blog'),
    path('category/<slug:category_slug>/', views.blogs_by_category, name='blogs_by_category'),
    path('subcategory/<slug:subcategory_slug>/', views.blogs_by_subcategory, name='blogs_by_subcategory'),
    path('tag/<slug:tag_slug>/', views.blogs_by_tag, name='blogs_by_tag'),
     path('newsletter_signup/', views.newsletter_signup, name='newsletter_signup')
]
