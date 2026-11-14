"""Telifsiz, sakin fon müziği üretir: yumuşak pad akorları + çan tınılı arpej. Kullanım: python3 music.py <saniye> <çıktı.wav>"""
import sys, numpy as np
from scipy.io import wavfile
from scipy.signal import fftconvolve

SR = 44100
dur = float(sys.argv[1]) if len(sys.argv) > 1 else 40
out = sys.argv[2] if len(sys.argv) > 2 else "music.wav"
bpm = 76; beat = 60 / bpm; bar = 4 * beat

def hz(m): return 440 * 2 ** ((m - 69) / 12)
# Cmaj9 – Am7 – Fmaj7 – G6 (yumuşak, umutlu)
chords = [[48, 55, 64, 71, 74], [45, 52, 60, 67, 72], [41, 48, 57, 64, 69], [43, 50, 59, 64, 71]]

n = int(SR * (dur + 3)); mix = np.zeros(n)
t_all = np.arange(n) / SR

def env(length, a, r):
    e = np.ones(length); ai = int(a * SR); ri = int(r * SR)
    e[:ai] = np.linspace(0, 1, ai) ** 2
    e[-ri:] *= np.linspace(1, 0, ri) ** 2
    return e

# pad
t0, i = 0.0, 0
while t0 < dur + 1:
    ch = chords[i % 4]; L = int((bar + 1.2) * SR); s = int(t0 * SR)
    if s + L > n: L = n - s
    t = np.arange(L) / SR; e = env(L, 1.1, 1.4)
    for m in ch:
        f = hz(m)
        v = (np.sin(2*np.pi*f*t) + .35*np.sin(2*np.pi*f*1.003*t) + .25*np.sin(2*np.pi*2*f*t)) * e
        mix[s:s+L] += .055 * v
    t0 += bar; i += 1

# arpej (çan tınısı)
pattern = [0, 2, 3, 4, 3, 2, 1, 2]
t0, i = 0.0, 0
while t0 < dur:
    ch = chords[int(t0 // bar) % 4]
    m = ch[pattern[i % 8] % len(ch)] + 12
    L = int(1.8 * SR); s = int(t0 * SR)
    if s + L > n: L = n - s
    t = np.arange(L) / SR; f = hz(m)
    v = (np.sin(2*np.pi*f*t) + .3*np.sin(2*np.pi*2.01*f*t) + .12*np.sin(2*np.pi*3*f*t)) * np.exp(-t*3.2) * np.minimum(1, t*200)
    mix[s:s+L] += .07 * v
    t0 += beat / 2; i += 1

# bas
t0, i = 0.0, 0
while t0 < dur + 1:
    m = chords[i % 4][0] - 12; L = int(bar * SR); s = int(t0 * SR)
    if s + L > n: L = n - s
    t = np.arange(L) / SR
    mix[s:s+L] += .08 * np.sin(2*np.pi*hz(m)*t) * env(L, .3, .8)
    t0 += bar; i += 1

# basit reverb
ir_t = np.arange(int(2.2 * SR)) / SR
ir = np.random.default_rng(1).standard_normal(len(ir_t)) * np.exp(-ir_t * 2.6); ir[0] = 1
wet = fftconvolve(mix, ir)[:n] * .035
y = (mix + wet)[:int(SR * dur)]
# giriş/çıkış fade
fi, fo = int(.8 * SR), int(2.5 * SR)
y[:fi] *= np.linspace(0, 1, fi); y[-fo:] *= np.linspace(1, 0, fo)
y = y / np.max(np.abs(y)) * .7
st = np.stack([y, np.roll(y, int(.012 * SR))], 1)
wavfile.write(out, SR, (st * 32767).astype(np.int16))
print("ok", out)
