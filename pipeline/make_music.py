#!/usr/bin/env python3
"""Original synthesized music bed + sound effects (no samples, no third-party music).
usage: make_music.py events.json out.wav   events: {"style":"thriller|mystery|melancholy","end":63,
 "pulse_from":s,"accents":[s..],"riser":[a,b],"impact":s,"whoosh":[s..],"pings":[s..],"hits":[s..]}"""
import sys, json, numpy as np
from scipy.signal import butter, sosfilt
import soundfile as sf
ev = json.load(open(sys.argv[1])); SR = 44100; END = ev["end"]; N = int(END*SR)
t = np.arange(N)/SR; rng = np.random.default_rng(7)
STY = {"thriller": dict(root=55.0, bpm=96, pulse=1.0, perc=1.0, pad=.55),
       "mystery": dict(root=49.0, bpm=72, pulse=.35, perc=0.0, pad=.8),
       "melancholy": dict(root=58.27, bpm=60, pulse=0.0, perc=0.0, pad=.9)}[ev.get("style", "thriller")]
def lp(x, fc, order=2): return sosfilt(butter(order, fc/(SR/2), "low", output="sos"), x)
def hp(x, fc, order=2): return sosfilt(butter(order, fc/(SR/2), "high", output="sos"), x)
def saw(f, tt): return 2*((f*tt) % 1)-1
def place(buf, x, at, gain=1.0):
    i = int(at*SR)
    if i >= N or i < 0: return
    x = x[:N-i]; buf[i:i+len(x)] += x*gain
L = np.zeros(N); R = np.zeros(N)
def add(x, at=0, g=1.0, pan=0.0):
    place(L, x, at, g*(1-max(0, pan))); place(R, x, at, g*(1+min(0, pan)))
root = STY["root"]
# pad: detuned saws, minor colour, slow movement
pad = sum(saw(f*d, t) for f in (root, root*1.5, root*2, root*2*1.189) for d in (0.996, 1.004))/8
pad = lp(pad, 420)*(0.75+0.25*np.sin(2*np.pi*0.07*t))
sub = np.sin(2*np.pi*root*t)*0.5
env = np.minimum(1, t/2.0)
add((pad*STY["pad"]+sub*.35)*env*0.5, 0, 1, 0)
shim = lp(saw(root*4*1.003, t)+saw(root*6*0.998, t), 1800)*0.04*(0.5+0.5*np.sin(2*np.pi*0.11*t+1))
add(shim*env, 0, 1, .3); add(np.roll(shim, 900)*env, 0, 1, -.3)
beat = 60/STY["bpm"]
def pluck(f, dur=.22):
    tt = np.arange(int(dur*SR))/SR
    return lp(saw(f, tt)+0.5*saw(f*2.01, tt), 900)*np.exp(-tt*14)
def kick():
    tt = np.arange(int(.28*SR))/SR
    return np.sin(2*np.pi*(45*tt+ (90-45)*(1-np.exp(-tt*30))/30))*np.exp(-tt*11)
def tick():
    tt = np.arange(int(.05*SR))/SR
    return hp(rng.standard_normal(len(tt)), 6000)*np.exp(-tt*90)
stop = ev.get("impact", END)-0.45
pf = ev.get("pulse_from")
if pf is not None and STY["pulse"] > 0:
    k = 0; x = pf
    while x < stop:
        lvl = STY["pulse"]*(0.55+0.45*min(1, (x-pf)/20))
        f = root*2 if k % 8 in (3, 6) else root*(1.189 if k % 16 == 14 else 1)
        add(pluck(f*2), x, .32*lvl)
        if STY["perc"] > 0 and x > pf+8:
            if k % 4 == 0: add(kick(), x, .5*STY["perc"])
            if k % 2 == 1: add(tick(), x, .10*STY["perc"], pan=.4 if k % 4 == 1 else -.4)
        x += beat/2; k += 1
def stab(dur=.5):
    tt = np.arange(int(dur*SR))/SR
    s = sum(saw(f*d, tt) for f in (root*2, root*2*1.189, root*3) for d in (.995, 1.005))/6
    return lp(s, 2200)*np.exp(-tt*7) + np.sin(2*np.pi*root*tt)*np.exp(-tt*9)*.8
for a in ev.get("accents", []): add(stab(), a, .55)
def boom(dur=3.0):
    tt = np.arange(int(dur*SR))/SR
    return (np.sin(2*np.pi*(38*tt+ (70-38)*(1-np.exp(-tt*18))/18))*np.exp(-tt*2.2)
            + lp(rng.standard_normal(len(tt)), 500)*np.exp(-tt*6)*.6 + hp(rng.standard_normal(len(tt)), 3000)*np.exp(-tt*25)*.15)
for h in ev.get("hits", []): add(boom(1.6), h, .5)
if "riser" in ev:
    a, b = ev["riser"]; tt = np.arange(int((b-a)*SR))/SR; k = tt/(b-a)
    r = lp(rng.standard_normal(len(tt)), 300+3500*k.max()*0+1, 1)
    r = hp(rng.standard_normal(len(tt)), 800)*k**2*.35 + np.sin(2*np.pi*np.cumsum(110+330*k**2)/SR)*k**1.5*.25
    add(r, a, .6)
if "impact" in ev:
    i0, i1 = int((ev["impact"]-0.42)*SR), int(ev["impact"]*SR)
    g = np.ones(N); g[i0:i1] = 0.05; g[i0-2000:i0] = np.linspace(1, .05, 2000)
    L *= g; R *= g; add(boom(3.2), ev["impact"], 1.0)
def whoosh(dur=.45):
    tt = np.arange(int(dur*SR))/SR; k = tt/dur
    n = rng.standard_normal(len(tt)); return hp(lp(n, 2500), 500)*np.sin(np.pi*k)**2
for i, w in enumerate(ev.get("whoosh", [])): add(whoosh(), w-.22, .16, pan=.5 if i % 2 else -.5)
def ping():
    tt = np.arange(int(.9*SR))/SR
    return np.sin(2*np.pi*1320*tt)*np.exp(-tt*6)*.6 + np.sin(2*np.pi*1980*tt)*np.exp(-tt*9)*.25
for p in ev.get("pings", []): add(ping(), p, .22, pan=.3); add(ping(), p+.28, .07, pan=-.5)
fade = np.ones(N); nf = int(1.6*SR); fade[-nf:] = np.linspace(1, 0, nf)**1.5
st = np.stack([L*fade, R*fade], 1); st = np.tanh(st*1.3)/1.3
st = st/np.max(np.abs(st))*0.9
sf.write(sys.argv[2], st.astype(np.float32), SR); print("music", round(END, 2), "s")
