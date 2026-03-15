/**
 * rumino-accessibility.js
 * ========================
 * Drop-in aksesibilitas untuk chatbot Rumino:
 *  - Text-to-Speech (TTS) via Web Speech API
 *  - Navigasi keyboard penuh (Tab, Enter, Arrow keys, Escape)
 *  - ARIA live region agar screen reader otomatis baca respons baru
 *  - Tombol "Baca Jawaban" per-pesan
 *  - Shortcut keyboard Alt+I/R/T/S
 */

const RuminoA11y = (() => {
  // ── KONFIGURASI (disesuaikan dengan HTML Rumino) ──────────────────────────
  const CONFIG = {
    selectors: {
      chatContainer:   '#chat-widget',
      messagesArea:    '#chat-box',
      inputField:      '#user-input',
      sendButton:      'button[onclick="sendUserMessage()"]',
      quickReplies:    '#quick-replies button',
      botMessageClass: '.bot-message',
    },
    shortcuts: {
      focusInput: 'i',   // Alt+I
      stopSpeech: 's',   // Alt+S
      readLast:   'r',   // Alt+R
      toggleTTS:  't',   // Alt+T
    },
    tts: {
      lang:     'id-ID',
      rate:     0.95,
      pitch:    1.0,
      autoRead: true,
    }
  };

  // ── STATE ─────────────────────────────────────────────────────────────────
  let ttsEnabled = CONFIG.tts.autoRead;
  const synth    = window.speechSynthesis;

  // ── TTS ───────────────────────────────────────────────────────────────────

  function cleanText(text) {
    return text
      .replace(/<[^>]*>/g, ' ')
      .replace(/[🤖👋📱📞📍💬🏢💼🎓✅❌⚠️]/gu, '')
      .replace(/https?:\/\/\S+/g, 'tautan')
      .replace(/\s+/g, ' ')
      .trim();
  }

  // Cache suara setelah browser siap
  let cachedVoice = null;
  function loadVoice() {
    const voices = synth.getVoices();
    cachedVoice = voices.find(v => v.lang.startsWith('id')) || null;
  }
  loadVoice();
  if (synth.onvoiceschanged !== undefined) synth.onvoiceschanged = loadVoice;

  function speak(text, onEnd = null) {
    if (!synth) return;
    synth.cancel();
    const clean = cleanText(text);
    if (!clean) return;

    const utter   = new SpeechSynthesisUtterance(clean);
    utter.lang    = CONFIG.tts.lang;
    utter.rate    = CONFIG.tts.rate;
    utter.pitch   = CONFIG.tts.pitch;
    if (onEnd) utter.onend = onEnd;
    if (cachedVoice) utter.voice = cachedVoice;

    synth.speak(utter);
  }

  function stopSpeech() {
    if (synth) synth.cancel();
  }

  // ── TOMBOL BACA PER-PESAN ─────────────────────────────────────────────────

  function createReadButton(msgEl) {
    const btn = document.createElement('button');
    btn.className = 'rumino-read-btn';
    btn.setAttribute('aria-label', 'Baca pesan ini dengan suara');
    btn.title = 'Tekan untuk membaca pesan (Alt+R untuk pesan terakhir)';
    btn.textContent = '🔊 Baca';

    Object.assign(btn.style, {
      marginTop:    '6px',
      padding:      '2px 10px',
      fontSize:     '11px',
      background:   'transparent',
      border:       '1px solid #cbd5e1',
      borderRadius: '12px',
      cursor:       'pointer',
      display:      'block',
      color:        '#64748b',
    });

    let reading = false;
    btn.addEventListener('click', () => {
      if (reading) {
        stopSpeech();
        btn.textContent = '🔊 Baca';
        reading = false;
      } else {
        speak(msgEl.textContent, () => {
          btn.textContent = '🔊 Baca';
          reading = false;
        });
        btn.textContent = '⏹ Stop';
        reading = true;
      }
    });

    return btn;
  }

  function attachReadButtons() {
    document.querySelectorAll(`${CONFIG.selectors.botMessageClass}:not([data-a11y])`).forEach(el => {
      el.setAttribute('data-a11y', 'true');
      el.appendChild(createReadButton(el));
    });
  }

  // ── ARIA ──────────────────────────────────────────────────────────────────

  function setupAria() {
    const area = document.querySelector(CONFIG.selectors.messagesArea);
    if (area) {
      area.setAttribute('role', 'log');
      area.setAttribute('aria-live', 'polite');
      area.setAttribute('aria-atomic', 'false');
      area.setAttribute('aria-label', 'Percakapan dengan Rumino');
    }

    const input = document.querySelector(CONFIG.selectors.inputField);
    if (input) {
      input.setAttribute('aria-label', 'Ketik pertanyaan untuk Rumino');
      input.setAttribute('aria-describedby', 'rumino-hint');

      const hint = document.createElement('span');
      hint.id = 'rumino-hint';
      hint.className = 'sr-only';
      hint.textContent = 'Tekan Enter untuk kirim. Alt+T toggle TTS. Alt+R baca pesan terakhir. Alt+S stop.';
      input.parentNode.insertBefore(hint, input.nextSibling);
    }

    const sendBtn = document.querySelector(CONFIG.selectors.sendButton);
    if (sendBtn) sendBtn.setAttribute('aria-label', 'Kirim pesan');

    const launcher = document.getElementById('chat-launcher');
    if (launcher) launcher.setAttribute('aria-label', 'Buka atau tutup chat Rumino');
  }

  // ── SCREEN READER ANNOUNCER ───────────────────────────────────────────────

  let announceEl = null;
  function announce(text) {
    if (!announceEl) {
      announceEl = document.createElement('div');
      announceEl.setAttribute('aria-live', 'assertive');
      announceEl.setAttribute('aria-atomic', 'true');
      announceEl.className = 'sr-only';
      document.body.appendChild(announceEl);
    }
    announceEl.textContent = '';
    setTimeout(() => { announceEl.textContent = text; }, 50);
  }

  // ── TOAST ─────────────────────────────────────────────────────────────────

  function showToast(text) {
    let toast = document.getElementById('rumino-toast');
    if (!toast) {
      toast = document.createElement('div');
      toast.id = 'rumino-toast';
      Object.assign(toast.style, {
        position: 'fixed', bottom: '90px', right: '20px',
        background: '#1e293b', color: '#fff',
        padding: '7px 14px', borderRadius: '8px',
        fontSize: '13px', zIndex: '9999', transition: 'opacity 0.3s',
      });
      document.body.appendChild(toast);
    }
    toast.textContent = text;
    toast.style.opacity = '1';
    clearTimeout(toast._t);
    toast._t = setTimeout(() => { toast.style.opacity = '0'; }, 2500);
  }

  // ── KEYBOARD ──────────────────────────────────────────────────────────────

  function readLastBotMessage() {
    const all = document.querySelectorAll(CONFIG.selectors.botMessageClass);
    if (!all.length) { announce('Belum ada pesan dari Rumino'); return; }
    const last = all[all.length - 1];
    speak(last.textContent, () => announce('Selesai membaca'));
    announce('Membaca pesan terakhir Rumino');
  }

  function setupKeyboard() {
    document.addEventListener('keydown', e => {
      if (e.altKey && !e.ctrlKey && !e.metaKey) {
        const k = e.key.toLowerCase();

        if (k === CONFIG.shortcuts.focusInput) {
          e.preventDefault();
          document.querySelector(CONFIG.selectors.inputField)?.focus();
          announce('Fokus di kotak pesan');
        }
        if (k === CONFIG.shortcuts.stopSpeech) {
          e.preventDefault();
          stopSpeech();
          announce('Pembacaan dihentikan');
        }
        if (k === CONFIG.shortcuts.readLast) {
          e.preventDefault();
          readLastBotMessage();
        }
        if (k === CONFIG.shortcuts.toggleTTS) {
          e.preventDefault();
          ttsEnabled = !ttsEnabled;
          const status = ttsEnabled ? 'aktif' : 'nonaktif';
          announce(`Text to Speech ${status}`);
          showToast(`🔊 TTS: ${status}`);
        }
      }

      // Arrow key untuk navigasi quick replies
      if (e.target.matches(CONFIG.selectors.quickReplies)) {
        const btns = [...document.querySelectorAll(CONFIG.selectors.quickReplies)];
        const idx  = btns.indexOf(e.target);
        if (e.key === 'ArrowRight' || e.key === 'ArrowDown') {
          e.preventDefault();
          btns[(idx + 1) % btns.length]?.focus();
        }
        if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') {
          e.preventDefault();
          btns[(idx - 1 + btns.length) % btns.length]?.focus();
        }
      }

      // Escape → balik ke input
      if (e.key === 'Escape') {
        stopSpeech();
        document.querySelector(CONFIG.selectors.inputField)?.focus();
      }
    });
  }

  // ── OBSERVER: auto-attach tombol & auto-TTS saat pesan baru ──────────────

  function waitStreamEnd(el, cb) {
    let last = '', stable = 0;
    const t = setInterval(() => {
      const cur = el.textContent;
      if (cur === last) { if (++stable >= 3) { clearInterval(t); cb(cur); } }
      else { stable = 0; last = cur; }
    }, 200);
  }

  function observeMessages() {
    const area = document.querySelector(CONFIG.selectors.messagesArea);
    if (!area) return;

    new MutationObserver(mutations => {
      mutations.forEach(m => {
        m.addedNodes.forEach(node => {
          if (node.nodeType !== 1) return;

          const isBotMsg  = node.matches?.(CONFIG.selectors.botMessageClass);
          const hasBotMsg = node.querySelector?.(CONFIG.selectors.botMessageClass);

          if (isBotMsg || hasBotMsg) {
            setTimeout(attachReadButtons, 400);
            if (ttsEnabled) {
              const target = isBotMsg ? node : node.querySelector(CONFIG.selectors.botMessageClass);
              if (target) waitStreamEnd(target, speak);
            }
          }

          // ARIA untuk quick reply yang baru muncul
          node.querySelectorAll?.(CONFIG.selectors.quickReplies)?.forEach(btn => {
            btn.setAttribute('role', 'button');
            if (!btn.hasAttribute('aria-label'))
              btn.setAttribute('aria-label', `Pilih: ${btn.textContent.trim()}`);
          });
        });
      });
    }).observe(area, { childList: true, subtree: true, characterData: true });
  }

  // ── CSS ───────────────────────────────────────────────────────────────────

  function injectCSS() {
    if (document.getElementById('rumino-a11y-css')) return;
    const s = document.createElement('style');
    s.id = 'rumino-a11y-css';
    s.textContent = `
      .sr-only {
        position:absolute!important;width:1px!important;height:1px!important;
        padding:0!important;margin:-1px!important;overflow:hidden!important;
        clip:rect(0,0,0,0)!important;white-space:nowrap!important;border:0!important;
      }
      :focus-visible { outline: 3px solid #2563eb !important; outline-offset: 2px !important; }
      .rumino-read-btn:hover, .rumino-read-btn:focus-visible {
        background: #f1f5f9 !important; border-color: #94a3b8 !important;
      }
    `;
    document.head.appendChild(s);
  }

  // ── PANEL SHORTCUT ────────────────────────────────────────────────────────

  function injectShortcutPanel() {
    if (document.getElementById('rumino-shortcuts')) return;
    const panel = document.createElement('div');
    panel.id = 'rumino-shortcuts';
    panel.setAttribute('role', 'complementary');
    panel.setAttribute('aria-label', 'Pintasan keyboard');
    panel.innerHTML = `
      <details style="font-size:11px;color:#94a3b8;padding:4px 12px 6px;border-top:1px solid #e2e8f0;">
        <summary style="cursor:pointer;font-weight:600;color:#64748b;">⌨️ Pintasan Keyboard</summary>
        <ul style="margin:4px 0 0;padding-left:14px;line-height:1.9;">
          <li><kbd>Alt+I</kbd> Fokus input</li>
          <li><kbd>Alt+R</kbd> Baca pesan terakhir</li>
          <li><kbd>Alt+T</kbd> Nyala/matikan TTS</li>
          <li><kbd>Alt+S</kbd> Stop pembacaan</li>
          <li><kbd>←/→</kbd> Pindah pilihan cepat</li>
          <li><kbd>Esc</kbd> Kembali ke input</li>
        </ul>
      </details>
    `;

    // Sisipkan sebelum area input (di dalam chat-widget)
    const inputArea = document.querySelector('#chat-widget .p-3.bg-white.border-t');
    if (inputArea) inputArea.insertAdjacentElement('beforebegin', panel);
  }

  // ── INIT ──────────────────────────────────────────────────────────────────

  function init() {
    const run = () => {
      injectCSS();
      setupAria();
      setupKeyboard();
      observeMessages();
      attachReadButtons();
      setTimeout(injectShortcutPanel, 500);
      console.log('[RuminoA11y] ✓ Alt+I=fokus | Alt+R=baca | Alt+T=TTS | Alt+S=stop');
    };
    document.readyState === 'loading'
      ? document.addEventListener('DOMContentLoaded', run)
      : run();
  }

  return { init, speak, stopSpeech, announce };
})();

RuminoA11y.init();