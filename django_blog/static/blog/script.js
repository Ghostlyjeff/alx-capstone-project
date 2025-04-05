// JavaScript for Blog Interactivity

document.addEventListener("DOMContentLoaded", function() {

    // For now, we will simply add a scroll-to-top button functionality

    // Create a "scroll to top" button
    const scrollToTopButton = document.createElement('button');
    scrollToTopButton.innerHTML = '↑';
    scrollToTopButton.classList.add('scroll-to-top');
    document.body.appendChild(scrollToTopButton);

    // Show or hide the button based on scroll position
    window.onscroll = function() {
        if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
            scrollToTopButton.style.display = "block";
        } else {
            scrollToTopButton.style.display = "none";
        }
    };

    // Smooth scrolling to top
    scrollToTopButton.onclick = function() {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    };

});
