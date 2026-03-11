document.addEventListener('DOMContentLoaded', () => {
  const toggle = document.getElementById('navToggle');
  const links = document.getElementById('navLinks');
  if (toggle && links) {
    toggle.addEventListener('click', () => links.classList.toggle('open'));
    links.querySelectorAll('a').forEach(a => a.addEventListener('click', () => links.classList.remove('open')));
  }

  document.querySelectorAll('.flash').forEach(el => {
    setTimeout(() => {
      el.style.transition = 'opacity .4s, transform .4s';
      el.style.opacity = '0';
      el.style.transform = 'translateX(40px)';
      setTimeout(() => el.remove(), 400);
    }, 4500);
  });

  const fecha = document.getElementById('fecha');
  if (fecha) {
    const d = new Date();
    d.setDate(d.getDate() + 1);
    fecha.min = d.toISOString().split('T')[0];
  }

  if ('IntersectionObserver' in window) {
    const targets = document.querySelectorAll('.sv-card, .test-card, .eq-card, .info-block, .adm-stat, .sf-section, .trust-item');
    targets.forEach((el, i) => {
      el.classList.add('reveal');
      if (i % 3 === 1) el.classList.add('reveal-d1');
      if (i % 3 === 2) el.classList.add('reveal-d2');
    });
    const obs = new IntersectionObserver(entries => {
      entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('visible'); obs.unobserve(e.target); } });
    }, { threshold: 0.08, rootMargin: '0px 0px -30px 0px' });
    targets.forEach(el => obs.observe(el));
  }
});
