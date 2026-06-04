document.addEventListener('DOMContentLoaded', () => {
  // 1. Navbar Scroll Effect
  const navbar = document.getElementById('navbar');
  window.addEventListener('scroll', () => {
    // Navbar background change
    if (window.scrollY > 50) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }
  });

  // 2. Intersection Observer for standard scroll animations
  const observerOptions = {
    root: null,
    rootMargin: '0px',
    threshold: 0.15
  };

  const scrollObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

  // Select all elements to animate
  const animatedElements = document.querySelectorAll('.scroll-trigger, .slide-in-left, .slide-in-right, .fade-in');
  animatedElements.forEach(el => scrollObserver.observe(el));

  // 3. Timeline interactive fill and nodes
  const timelineSection = document.getElementById('timeline');
  const timelineProgress = document.getElementById('timeline-progress');
  const timelineNodes = document.querySelectorAll('.scroll-trigger-node');
  
  // Custom observer for timeline items
  const timelineObserver = new IntersectionObserver((entries) => {
    let activeIndex = -1;
    
    // Check which nodes are visible
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('active');
      }
    });
    
    // Calculate progress based on active nodes or scroll position
    // For a simpler approach, we'll just track scroll within the section
  }, { threshold: 0.5 });
  
  timelineNodes.forEach(node => timelineObserver.observe(node));

  // Listen to scroll to fill timeline progress line
  window.addEventListener('scroll', () => {
    if (!timelineSection) return;
    
    const rect = timelineSection.getBoundingClientRect();
    const sectionTop = rect.top;
    const sectionHeight = rect.height;
    const windowHeight = window.innerHeight;
    
    // If section is in view
    if (sectionTop < windowHeight && sectionTop + sectionHeight > 0) {
      // Calculate how far we've scrolled into the section
      const scrolled = windowHeight - sectionTop - (windowHeight * 0.3); // Offset to start later
      const total = sectionHeight;
      
      let percentage = (scrolled / total) * 100;
      percentage = Math.max(0, Math.min(100, percentage));
      
      // Check if it's mobile layout (vertical) or desktop (horizontal)
      if (window.innerWidth <= 768) {
        timelineProgress.style.height = `${percentage}%`;
        timelineProgress.style.width = '100%';
      } else {
        timelineProgress.style.width = `${percentage}%`;
        timelineProgress.style.height = '100%';
      }
      
      // Activate nodes sequentially
      timelineNodes.forEach((node, index) => {
        const threshold = (index * 40) + 10; // Trigger points
        if (percentage >= threshold) {
          node.classList.add('active');
        } else {
          node.classList.remove('active');
        }
      });
    }
  });
  
  // Form submission handler (mock)
  const contactForm = document.getElementById('contact-form');
  const submitBtn = document.getElementById('submit-btn');
  
  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();
      
      const btnText = submitBtn.querySelector('.btn-text');
      const originalText = btnText.innerText;
      
      btnText.innerText = 'PROCESANDO...';
      submitBtn.style.opacity = '0.8';
      submitBtn.style.pointerEvents = 'none';
      
      // Simulate API call
      setTimeout(() => {
        btnText.innerText = '¡ENVIADO CORRECTAMENTE!';
        submitBtn.style.backgroundColor = '#10B981'; // Green success
        
        setTimeout(() => {
          contactForm.reset();
          btnText.innerText = originalText;
          submitBtn.style.opacity = '1';
          submitBtn.style.pointerEvents = 'all';
          submitBtn.style.backgroundColor = '';
        }, 3000);
      }, 1500);
    });
  }
});
