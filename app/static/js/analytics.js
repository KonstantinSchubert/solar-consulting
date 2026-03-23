/**
 * Lightweight analytics event tracking.
 * Logs events to the console and can be extended to send to a real analytics endpoint.
 */

function trackEvent(eventName, properties) {
  const payload = {
    event: eventName,
    timestamp: new Date().toISOString(),
    url: window.location.pathname,
    ...properties,
  };
  console.info('[analytics]', payload);

  // TODO: replace with real analytics endpoint, e.g.:
  // fetch('/api/events', { method: 'POST', body: JSON.stringify(payload), headers: { 'Content-Type': 'application/json' } });
  // Or forward to Plausible / Fathom / GA4 etc.
}

// ── Hero CTA click ──────────────────────────────────────────
document.getElementById('hero-cta')?.addEventListener('click', function () {
  trackEvent('hero_cta_click');
});

// ── Checklist CTA click ─────────────────────────────────────
document.getElementById('checklist-cta')?.addEventListener('click', function () {
  trackEvent('checklist_cta_click');
});

// ── Contact form submit ─────────────────────────────────────
document.getElementById('contact-form')?.addEventListener('submit', function () {
  trackEvent('form_submit');
});

// ── Scroll depth ────────────────────────────────────────────
(function () {
  const milestones = [25, 50, 75, 100];
  const reached = new Set();

  function getScrollDepth() {
    const scrollTop = window.scrollY || document.documentElement.scrollTop;
    const docHeight = document.documentElement.scrollHeight - window.innerHeight;
    if (docHeight <= 0) return 100;
    return Math.round((scrollTop / docHeight) * 100);
  }

  function onScroll() {
    const depth = getScrollDepth();
    for (const milestone of milestones) {
      if (depth >= milestone && !reached.has(milestone)) {
        reached.add(milestone);
        trackEvent('page_scroll_depth', { depth_percent: milestone });
      }
    }
  }

  window.addEventListener('scroll', onScroll, { passive: true });
})();
