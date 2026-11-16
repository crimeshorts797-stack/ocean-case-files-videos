import sys; sys.path.insert(0, "/home/claude/pipeline")
from scenelib import *
T = load("v14"); c = lambda k, d=.2: T[k]-d
cuts = [0, c("place"), c("flight"), c("learn"), c("others"), c("keep"), c("verdict",.25), c("cta"), END]
S = Scene("v14", "WHO WINS? #005", cuts)
TS = lambda x, y, s, **k: [{"type":"creature","kind":"shark","x":x,"y":y,"scale":s, **k}]
S.shot(0, {"depth":.2,"surface":True}, [albatross(960, 300, .8), *TS(960, 760, 1.0, mode="silhouette"), cap("!VS!", 540, .15, 96),
   cap("SOUNDS *UNFAIR*", 900, T["h2"], 44)], fadeIn=.25)
s = cuts[1]
island = "<ellipse cx='960' cy='620' rx='300' ry='60' fill='#e6d3a3'/><ellipse cx='960' cy='600' rx='220' ry='34' fill='#cdb98a'/>"
S.shot(1, {"mode":"black","sun":{"x":960,"y":540,"r":700}}, [svg("<rect x='0' y='620' width='1920' height='460' fill='#1d5a7a'/><rect x='0' y='0' width='1920' height='620' fill='#4f86a3'/>"),
   svg(island), *[albatross(860+i*60, 560, .18, t0=T["birds"]-s+.3+i*.15, water=False) for i in range(4)],
   cap("FRENCH FRIGATE SHOALS", 215, .2, 34), cap("HAWAII", 265, .9, 30),
   cap("*THOUSANDS* OF NESTS", 860, T["birds"]-s+.6, 40)])
s = cuts[2]
S.shot(2, {"mode":"black"}, [svg("<rect x='0' y='620' width='1920' height='460' fill='#1d5a7a'/><rect x='0' y='0' width='1920' height='620' fill='#4f86a3'/>"),
   albatross(900, 380, .55), albatross(1050, 612, .5, water=True, t0=T["fail"]-s+.4),
   cap("FIRST FLIGHT", 215, .2, 50), cap("SOME *SPLASH DOWN*", 880, T["fail"]-s+1.4, 42)])
s = cuts[3]
S.shot(3, {"depth":.25,"surface":True}, [albatross(1000, 140, .45, water=True), *TS(940, 640, 1.0, bob=2),
   tigerstripes(940, 640, 1.0), cap("THEY KNOW *WHEN*", 880, .4, 46),
   {"type":"pill","text":"Tagged sharks","x":810,"y":945,"size":24,"t0":T["tag"]-s+.2}])
s = cuts[4]
S.shot(4, {"depth":.4}, [*TS(940, 460, 1.1), tigerstripes(940, 460, 1.1), {"type":"creature","kind":"shark","x":1120,"y":780,"scale":.45,"flip":True,"dim":True,"swim":{"vx":-50},"t0":.6},
   cap("REEF SHARKS *STAY AWAY*", 215, .3, 38)])
s = cuts[5]
S.shot(5, {"mode":"black"}, [svg("<rect x='0' y='620' width='1920' height='460' fill='#1d5a7a'/><rect x='0' y='0' width='1920' height='620' fill='#4f86a3'/>"),
   albatross(960, 360, .7), cap("KEEP *FLYING*", 860, .3, 50), cap("ONE MEAL RESHAPES", 210, T["why"]-s+.4, 36), cap("A WHOLE *HUNT*", 262, T["why"]-s+1.6, 40)])
s = cuts[6]
S.shot(6, {"depth":.85,"spotlight":{"x":960,"w":320}}, [*TS(960, 470, 1.0), tigerstripes(960, 470, 1.0), cap("VERDICT", 215, .2, 44),
   {"type":"stamp","text":"Tiger shark wins","x":960,"y":740,"size":46,"t0":T["verdict"]-s+.6}, cap("…IF THEY *LAND*", 900, T["verdict"]-s+2.4, 40)])
s = cuts[7]
S.shot(7, {"mode":"black"}, [svg("<rect x='0' y='620' width='1920' height='460' fill='#1d5a7a'/><rect x='0' y='0' width='1920' height='620' fill='#4f86a3'/>"),
   albatross(960, 380, .6), cap("SHARKS HUNT *BIRDS*", 860, .3, 44), {"type":"pill","text":"Comment your matchup","x":768,"y":940,"size":24,"t0":1.2}], fadeOut=.5)
S.save({"style":"thriller","end":END,"pulse_from":c("flight"),"hits":[.12,T["fail"]+.4],"riser":[T["keep"],T["verdict"]+.1],"impact":T["verdict"]+.6,
 "whoosh":[T["h2"],T["place"]+.2,T["birds"]+.6,T["fail"]+1.4,T["learn"]+.4,T["tag"]+.2,T["others"]+.3,T["keep"]+.3,T["why"]+1.6,T["verdict"]+2.4,T["cta"]+.3]})
