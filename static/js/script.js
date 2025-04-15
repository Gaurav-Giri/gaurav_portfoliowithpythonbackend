// Dark mode toggle
const themeToggle = document.getElementById('theme-toggle');
const html = document.documentElement;

// Check for saved preference or use system preference
const storedTheme = localStorage.getItem('theme') || 
    (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
html.classList.toggle('dark', storedTheme === 'dark');

themeToggle.addEventListener('click', () => {
    html.classList.toggle('dark');
    localStorage.setItem('theme', html.classList.contains('dark') ? 'dark' : 'light');
});

// Mobile menu toggle
const mobileMenuButton = document.getElementById('mobile-menu-button');
const mobileMenu = document.getElementById('mobile-menu');

mobileMenuButton.addEventListener('click', () => {
    mobileMenu.classList.toggle('hidden');
});

// Flash message auto-dismiss
document.querySelectorAll('.alert').forEach(alert => {
    setTimeout(() => {
        alert.classList.add('opacity-0');
        setTimeout(() => alert.remove(), 500);
    }, 5000);
});