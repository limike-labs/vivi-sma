// ---------------- NAV MOBILE ----------------
const burger = document.getElementById('burgerBtn');
const menu = document.getElementById('mobileMenu');
burger.addEventListener('click', () => {
  const isOpen = menu.classList.toggle('open');
  burger.classList.toggle('open', isOpen);
  burger.setAttribute('aria-expanded', isOpen);
  document.body.classList.toggle('locked', isOpen);
});
document.querySelectorAll('.mobile-menu a').forEach(a=>{
  a.addEventListener('click', ()=>{
    menu.classList.remove('open');
    burger.classList.remove('open');
    burger.setAttribute('aria-expanded', false);
    document.body.classList.remove('locked');
  });
});

// ---------------- MOTION DESIGN (directiva 48) ----------------
const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

if (prefersReducedMotion) {
  // Sin animación: todo queda visible de inmediato, sin perder contenido
  document.querySelectorAll('.reveal, .reveal-btn').forEach(el => el.classList.add('is-visible'));
} else {
  // Fade-up + stagger al entrar en viewport (una sola vez por elemento)
  const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
        revealObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.15, rootMargin: '0px 0px -40px 0px' });

  // Stagger: dentro de cada contenedor, cada .reveal se retrasa un poco respecto al anterior
  document.querySelectorAll('.scroll-row, .grid-row, .cat-grid, .promos-grid, .eventos-grid').forEach(container => {
    container.querySelectorAll('.reveal').forEach((el, i) => {
      el.style.transitionDelay = Math.min(i * 70, 280) + 'ms';
    });
  });

  document.querySelectorAll('.reveal, .reveal-btn').forEach(el => revealObserver.observe(el));

  // Parallax muy suave del hero (se siente más de lo que se ve)
  const heroPhoto = document.querySelector('.hero-photo');
  const heroSection = document.querySelector('.hero');
  if (heroPhoto && heroSection) {
    let ticking = false;
    window.addEventListener('scroll', () => {
      if (ticking) return;
      ticking = true;
      requestAnimationFrame(() => {
        const rect = heroSection.getBoundingClientRect();
        if (rect.bottom > 0 && rect.top < window.innerHeight) {
          const offset = Math.max(-40, Math.min(40, window.scrollY * 0.12));
          heroPhoto.style.transform = `translateY(${offset}px)`;
        }
        ticking = false;
      });
    }, { passive: true });
  }
}
