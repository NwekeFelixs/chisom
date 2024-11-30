'use strict';

// navbar variables
const nav = document.querySelector('.mobile-nav');
const navMenuBtn = document.querySelector('.nav-menu-btn');
const navCloseBtn = document.querySelector('.nav-close-btn');

// navToggle function
const navToggleFunc = () => nav.classList.toggle('active');

navMenuBtn.addEventListener('click', navToggleFunc);
navCloseBtn.addEventListener('click', navToggleFunc);

// theme toggle variables
const themeBtn = document.querySelectorAll('.theme-btn');

// Function to toggle the theme
const toggleTheme = () => {
  // Check if body contains light-theme or dark-theme
  if (document.body.classList.contains('light-theme')) {
    // Switch to dark theme
    document.body.classList.replace('light-theme', 'dark-theme');
    localStorage.setItem('theme', 'dark-theme'); // Save to localStorage
  } else {
    // Switch to light theme
    document.body.classList.replace('dark-theme', 'light-theme');
    localStorage.setItem('theme', 'light-theme'); // Save to localStorage
  }
  
  // Toggle theme button classes
  themeBtn.forEach(btn => {
    btn.classList.toggle('light');
    btn.classList.toggle('dark');
  });
};

// Add event listeners to all theme buttons
themeBtn.forEach(btn => {
  btn.addEventListener('click', toggleTheme);
});

// Apply the theme from localStorage on page load
window.addEventListener('DOMContentLoaded', () => {
  const savedTheme = localStorage.getItem('theme');
  
  if (savedTheme) {
    document.body.classList.add(savedTheme); // Apply the saved theme

    // Set the theme button classes accordingly
    themeBtn.forEach(btn => {
      if (savedTheme === 'dark-theme') {
        btn.classList.remove('light');
        btn.classList.add('dark');
      } else {
        btn.classList.remove('dark');
        btn.classList.add('light');
      }
    });
  } else {
    // Default to light theme if nothing is saved
    document.body.classList.add('light-theme');
  }
});


const dropdownToggle = document.getElementById('userDropdown');
dropdownToggle.addEventListener('click', function () {
  console.log('Dropdown button clicked');
  dropdownMenu.classList.toggle('show');
});

