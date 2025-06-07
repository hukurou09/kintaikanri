// JavaScript for interactivity will be added here

document.addEventListener('DOMContentLoaded', function() {
    console.log('勤怠マネージャー script loaded');
    // Example: Set primary color from Flask template
    const primaryColor = getComputedStyle(document.documentElement).getPropertyValue('--primary-color').trim();
    if (primaryColor) {
        console.log('Primary color:', primaryColor);
        // You can use this color in JS if needed, e.g., for dynamic elements
    }
});
