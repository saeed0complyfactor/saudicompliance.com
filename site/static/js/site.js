/* Saudi Compliance: interaction and motion. No dependencies. */
(() => {
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const rtl = document.documentElement.dir === 'rtl';
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];

  /* ---------- Wave linework (canvas) ---------- */
  function wave(canvas) {
    const ctx = canvas.getContext('2d');
    const kind = canvas.dataset.wave;
    const LINES = kind === 'hero' ? 46 : 34;
    let w = 0, h = 0, dpr = 1, t = 0, raf = 0, visible = true;
    const size = () => {
      dpr = Math.min(window.devicePixelRatio || 1, 2);
      w = canvas.clientWidth; h = canvas.clientHeight;
      canvas.width = w * dpr; canvas.height = h * dpr;
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    };
    const base = kind === 'hero' ? 0.5 : kind === 'cta' ? 0.6 : 0.66;
    const draw = () => {
      ctx.clearRect(0, 0, w, h);
      for (let i = 0; i < LINES; i++) {
        const p = i / (LINES - 1);               // 0 = back line, 1 = front line
        const depth = Math.pow(p, 1.6);
        const y0 = h * (base - 0.2 + depth * 0.5);
        const amp = h * (0.05 + depth * 0.13);
        const alpha = 0.12 + depth * 0.75;
        const lime = p > 0.55;
        ctx.strokeStyle = lime ? `rgba(191,239,76,${alpha * 0.55})` : `rgba(84,176,164,${alpha * 0.85})`;
        ctx.lineWidth = 0.7 + depth * 0.9;
        ctx.beginPath();
        for (let x = -20; x <= w + 20; x += 14) {
          const u = x / w;
          const y = y0
            + Math.sin(u * 3.1 + t * 0.55 + p * 1.9) * amp
            + Math.sin(u * 7.3 - t * 0.35 + p * 4.0) * amp * 0.22
            - Math.cos(u * 1.4 + t * 0.2) * h * 0.06 * (1 - p);
          x === -20 ? ctx.moveTo(x, y) : ctx.lineTo(x, y);
        }
        ctx.stroke();
      }
    };
    const loop = () => { t += 0.006; draw(); raf = visible ? requestAnimationFrame(loop) : 0; };
    size(); draw();
    addEventListener('resize', () => { size(); draw(); }, { passive: true });
    if (reduce) return;
    new IntersectionObserver(([e]) => {
      visible = e.isIntersecting;
      if (visible && !raf) raf = requestAnimationFrame(loop);
    }).observe(canvas);
  }
  $$('canvas[data-wave]').forEach(wave);

  /* ---------- Split headings: word-by-word rise ---------- */
  function splitWords(el) {
    let wi = 0;
    const walk = (node) => {
      [...node.childNodes].forEach((n) => {
        if (n.nodeType === 3) {
          const frag = document.createDocumentFragment();
          n.textContent.split(/(\s+)/).forEach((part) => {
            if (!part) return;
            if (/^\s+$/.test(part)) { frag.appendChild(document.createTextNode(part)); return; }
            const w = document.createElement('span'); w.className = 'w';
            const s = document.createElement('span'); s.textContent = part; s.style.setProperty('--wi', wi++);
            w.appendChild(s); frag.appendChild(w);
          });
          n.replaceWith(frag);
        } else if (n.nodeType === 1 && n.tagName !== 'BR') walk(n);
      });
    };
    walk(el);
    el.setAttribute('data-split-ready', '');
  }
  const io = new IntersectionObserver((entries) => {
    entries.forEach((e) => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
  }, { rootMargin: '0px 0px -12% 0px' });
  $$('[data-split]').forEach((el) => {
    if (reduce) return;
    splitWords(el);
    if (el.hasAttribute('data-split-now')) setTimeout(() => el.classList.add('in'), 80);
    else io.observe(el);
  });
  $$('.rise, .clip-in').forEach((el) => {
    if (el.closest('.hero')) setTimeout(() => el.classList.add('in'), 80);
    else io.observe(el);
  });
  // Safety net: nothing stays hidden if an observer never fires.
  setTimeout(() => $$('[data-split], .rise, .clip-in').forEach((el) => el.classList.add('in')), 4000);

  /* ---------- Nav: solid after the hero, hides on scroll down ---------- */
  const nav = $('[data-nav]');
  let lastY = scrollY;
  const onScroll = () => {
    const y = scrollY;
    nav.classList.toggle('solid', y > 40);
    const menuOpen = !$('#menu').hidden;
    nav.classList.toggle('hide', !menuOpen && y > 400 && y > lastY + 4);
    if (y < lastY - 4) nav.classList.remove('hide');
    lastY = y;
  };
  addEventListener('scroll', onScroll, { passive: true }); onScroll();
  const burger = $('[data-burger]');
  burger.addEventListener('click', () => {
    const m = $('#menu'); const open = m.hidden;
    m.hidden = !open; burger.setAttribute('aria-expanded', String(open));
    nav.classList.add('solid');
  });
  addEventListener('keydown', (e) => { if (e.key === 'Escape' && !$('#menu').hidden) { burger.click(); burger.focus(); } });

  /* ---------- Scroll-filled statement ---------- */
  const fill = $('[data-fill]');
  if (fill) {
    const parts = [];
    [...fill.childNodes].forEach((n) => {
      if (n.nodeType === 3) {
        const frag = document.createDocumentFragment();
        n.textContent.split(/(\s+)/).forEach((p) => {
          if (!p) return;
          if (/^\s+$/.test(p)) frag.appendChild(document.createTextNode(p));
          else { const s = document.createElement('span'); s.className = 'fw'; s.textContent = p; frag.appendChild(s); parts.push(s); }
        });
        n.replaceWith(frag);
      } else { n.classList.add('fw'); parts.push(n); }
    });
    const upd = () => {
      const r = fill.getBoundingClientRect();
      const prog = Math.min(1, Math.max(0, (innerHeight * 0.85 - r.top) / (r.height + innerHeight * 0.35)));
      const n = reduce ? parts.length : Math.round(prog * parts.length);
      parts.forEach((p, i) => p.classList.toggle('on', i < n));
    };
    addEventListener('scroll', upd, { passive: true }); upd();
  }

  /* ---------- Count-up numbers ---------- */
  const counters = new IntersectionObserver((entries) => {
    entries.forEach((e) => {
      if (!e.isIntersecting) return;
      counters.unobserve(e.target);
      const el = e.target; const raw = el.dataset.count; const m = raw.match(/^(\d+)(.*)$/);
      if (!m || reduce) return;
      const end = +m[1]; const suf = m[2]; const t0 = performance.now(); const dur = 1600;
      const step = (now) => {
        const k = Math.min(1, (now - t0) / dur); const eased = 1 - Math.pow(2, -10 * k);
        el.textContent = Math.round(end * (k === 1 ? 1 : eased)) + suf;
        if (k < 1) requestAnimationFrame(step);
      };
      requestAnimationFrame(step);
    });
  }, { threshold: 0.6 });
  $$('[data-count]').forEach((el) => counters.observe(el));

  /* ---------- Carousel ---------- */
  const car = $('[data-carousel]');
  if (car) {
    $$('[data-car]').forEach((b) => b.addEventListener('click', () => {
      const card = car.firstElementChild; const gap = 20;
      const dx = (card.getBoundingClientRect().width + gap) * +b.dataset.car * (rtl ? -1 : 1);
      car.scrollBy({ left: dx, behavior: reduce ? 'auto' : 'smooth' });
    }));
    // Drag to scroll with a mouse.
    let down = false, sx = 0, sl = 0, moved = false;
    car.addEventListener('pointerdown', (e) => { if (e.pointerType !== 'mouse') return; down = true; moved = false; sx = e.clientX; sl = car.scrollLeft; car.style.scrollSnapType = 'none'; });
    addEventListener('pointermove', (e) => { if (!down) return; const d = e.clientX - sx; if (Math.abs(d) > 4) moved = true; car.scrollLeft = sl - d; });
    addEventListener('pointerup', () => { if (!down) return; down = false; car.style.scrollSnapType = ''; });
    car.addEventListener('click', (e) => { if (moved) { e.preventDefault(); moved = false; } }, true);
  }

  /* ---------- Sticky steps + table of contents ---------- */
  function spy(targets, links, attr) {
    if (!targets.length) return;
    const set = (id) => {
      links.forEach((a) => a.classList.toggle('on', a.getAttribute(attr) === id));
      const idx = targets.findIndex((t) => t.dataset.spy === id);
      targets.forEach((t, i) => { t.classList.toggle('on', i === idx); t.classList.toggle('past', i < idx); });
    };
    const ob = new IntersectionObserver((entries) => {
      entries.forEach((e) => { if (e.isIntersecting) set(e.target.dataset.spy); });
    }, { rootMargin: '-45% 0px -50% 0px' });
    targets.forEach((t) => ob.observe(t));
    set(targets[0].dataset.spy);
  }
  const thread = $('[data-thread]');
  if (thread) {
    const panels = $('.st-panels');
    const upd = () => {
      const r = panels.getBoundingClientRect();
      const p = Math.min(1, Math.max(0, (innerHeight * 0.5 - r.top) / r.height));
      thread.style.setProperty('--p', (p * 100).toFixed(1) + '%');
    };
    addEventListener('scroll', upd, { passive: true }); upd();
  }
  const steps = $$('[data-step]');
  steps.forEach((s) => (s.dataset.spy = s.dataset.step));
  spy(steps, $$('[data-step-link]'), 'data-step-link');
  const secs = $$('.prose h2[id]').map((h) => { const s = h.closest('.blk') || h; s.dataset.spy = h.id; return s; });
  // Articles: each h2 owns the content until the next h2.
  if ($('.post')) secs.forEach((h) => { h.style.scrollMarginTop = '110px'; });
  spy(secs, $$('[data-toc]'), 'data-toc');

  /* ---------- Parallax image + drifting cards ---------- */
  const para = $$('[data-parallax]');
  const floatSec = $('[data-float]');
  const cards = floatSec ? $$('.float-card', floatSec) : [];
  const speeds = [0.28, -0.12, 0.18, -0.22, 0.32, -0.08];
  const frame = () => {
    para.forEach((el) => {
      const r = el.parentElement.getBoundingClientRect();
      const k = Math.max(-1, Math.min(1, (r.top + r.height / 2 - innerHeight / 2) / innerHeight));
      el.style.transform = `translate3d(0, ${k * -10}%, 0)`;
    });
    if (cards.length && innerWidth > 760) {
      cards.forEach((c, i) => {
        const r = c.getBoundingClientRect();
        const k = Math.max(-1.2, Math.min(1.2, (r.top + r.height / 2 - innerHeight / 2) / innerHeight));
        c.style.transform = `translate3d(0, ${k * speeds[i % speeds.length] * 260}px, 0) rotate(${k * (i % 2 ? 2 : -2)}deg)`;
      });
    }
  };
  if (!reduce && (para.length || cards.length)) {
    let ticking = false;
    addEventListener('scroll', () => { if (!ticking) { ticking = true; requestAnimationFrame(() => { frame(); ticking = false; }); } }, { passive: true });
    frame();
  }

  /* ---------- Contact form ---------- */
  const form = $('[data-form]');
  if (form) {
    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      const btn = $('button[type=submit]', form); const label = $('.btn-label', btn); const msg = $('.form-msg', form);
      const orig = label.textContent; btn.disabled = true; label.textContent = btn.dataset.sending; msg.className = 'form-msg'; msg.textContent = '';
      try {
        const res = await fetch(form.action, { method: 'POST', headers: { Accept: 'application/json' }, body: new FormData(form) });
        const j = await res.json();
        if (!j.success) throw new Error(j.message);
        form.reset(); msg.classList.add('ok'); msg.textContent = msg.dataset.ok;
      } catch (err) {
        msg.classList.add('err'); msg.textContent = msg.dataset.err;
      } finally { btn.disabled = false; label.textContent = orig; }
    });
  }

  // Review hook: #y=1200 scrolls there on load (used by the screenshot script).
  const m = location.hash.match(/^#y=(\d+)$/); if (m) { scrollTo(0, +m[1]); dispatchEvent(new Event('scroll')); }

  $$('[data-year]').forEach((el) => (el.textContent = new Date().getFullYear()));
})();
