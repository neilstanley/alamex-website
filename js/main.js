/* ============================================
   ALAMEX — Main JavaScript
   ============================================ */

(function () {
  'use strict';

  // --- Mobile Navigation Toggle ---
  const navToggle = document.getElementById('nav-toggle');
  const nav = document.getElementById('nav');

  if (navToggle && nav) {
    navToggle.addEventListener('click', function () {
      const isOpen = nav.classList.toggle('nav--open');
      navToggle.classList.toggle('nav-toggle--active');
      navToggle.setAttribute('aria-expanded', isOpen);
    });

    // Close nav when clicking a link (mobile)
    nav.querySelectorAll('.nav__link').forEach(function (link) {
      link.addEventListener('click', function () {
        nav.classList.remove('nav--open');
        navToggle.classList.remove('nav-toggle--active');
        navToggle.setAttribute('aria-expanded', 'false');
      });
    });
  }

  // --- Header scroll effect ---
  const header = document.getElementById('header');

  if (header) {
    var lastScroll = 0;
    window.addEventListener('scroll', function () {
      var currentScroll = window.pageYOffset;
      if (currentScroll > 10) {
        header.classList.add('header--scrolled');
      } else {
        header.classList.remove('header--scrolled');
      }
      lastScroll = currentScroll;
    }, { passive: true });
  }

  // --- Contact Form Handling ---
  // FormSubmit.co redirects back to ?sent=true after submission
  const form = document.getElementById('contact-form');
  const formSuccess = document.getElementById('form-success');

  if (form && formSuccess) {
    // Check if we're returning from a successful submission
    var urlParams = new URLSearchParams(window.location.search);
    if (urlParams.get('sent') === 'true') {
      form.style.display = 'none';
      formSuccess.style.display = 'block';
      // Clean up the URL
      if (window.history.replaceState) {
        window.history.replaceState({}, document.title, window.location.pathname);
      }
    }
  }

  // --- Scroll-triggered fade-in animations ---
  var animateElements = document.querySelectorAll('.card, .process__step, .stat__number, .contact-info__item');

  if (animateElements.length > 0 && 'IntersectionObserver' in window) {
    // Add initial hidden state
    animateElements.forEach(function (el) {
      el.style.opacity = '0';
      el.style.transform = 'translateY(20px)';
      el.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
    });

    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          // Stagger animations within the same parent
          var parent = entry.target.parentElement;
          var siblings = Array.from(parent.children).filter(function (child) {
            return animateElements.length && Array.from(animateElements).indexOf(child) !== -1;
          });
          var index = siblings.indexOf(entry.target);
          var delay = index * 100;

          setTimeout(function () {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
          }, delay);

          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

    animateElements.forEach(function (el) { observer.observe(el); });
  }

  // --- Smooth scroll for anchor links ---
  document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
    anchor.addEventListener('click', function (e) {
      var target = document.querySelector(this.getAttribute('href'));
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });

})();
