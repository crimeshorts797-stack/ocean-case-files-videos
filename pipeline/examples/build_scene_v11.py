import sys; sys.path.insert(0, "/home/claude/pipeline")
from scenelib import *
T = load("v11"); c = lambda k, d=.2: T[k]-d
cuts = [0, c("size"), c("spring"), c("fast"), c("twice"), c("bubble"), c("shell"), c("verdict",.25), c("twist"), c("cta"), END]
S = Scene("v11", "WHO WINS? #004", cuts)
S.shot(0, {"depth":.6,"seabed":"dark","seabedY":860}, [mantis(990, 520, .85), snail(1110, 780, .9), cap("!VS!", 330, .15, 96),
   cap("ARMOR VS. A *FIST*", 880, T["h2"]+.2, 40)], fadeIn=.25)
s = cuts[1]
S.shot(1, {"depth":.4,"seabed":"dark","seabedY":860}, [mantis(980, 560, 1.0), cap("PEACOCK MANTIS SHRIMP", 215, .2, 36),
   {"type":"pill","text":"About pencil-length","x":790,"y":265,"size":24,"t0":1.4},
   {"type":"circle","x":1080,"y":580,"rx":90,"ry":60,"t0":T["club"]-s+1.4}, cap("TWO *CLUBS*", 880, T["club"]-s+1.0, 52)])
s = cuts[2]
S.shot(2, {"mode":"sonar"}, [{"type":"meter","x":720,"y":420,"w":480,"value":.95,"number":23,"unit":"m/s","t0":T["speed"]-s+.4,"dur":1.4},
   cap("A *SPRING* LETS GO", 215, .2, 42), cap("*~80 KM/H*", 720, T["speed"]-s+3.0, 64), cap("UNDERWATER", 790, T["speed"]-s+5.0, 36)])
s = cuts[3]
S.shot(3, {"mode":"paper"}, [cap("TOO FAST TO SEE", 215, .2, 44), {"type":"bignumber","from":0,"to":5000,"x":960,"y":540,"size":140,"t0":.8,"dur":1.6},
   cap("FRAMES PER SECOND", 640, 1.6, 36)])
s = cuts[4]
S.shot(4, {"depth":.55,"seabed":"dark","seabedY":860}, [mantis(880, 600, .8, strike=True), snail(1130, 610, .75),
   cap("HIT *TWICE*", 215, .1, 56), cap("1. THE *CLUB*", 860, T["first"]-s+.2, 46)])
s = cuts[5]
bub = lambda t0, t1=None: svg("<circle cx='1060' cy='600' r='70' fill='none' stroke='#cfefff' stroke-width='5'/><circle cx='1040' cy='580' r='14' fill='#fff' opacity='.6'/>", t0, t1=t1)
S.shot(5, {"depth":.55,"seabed":"dark","seabedY":860}, [mantis(880, 600, .8, strike=True), snail(1130, 610, .75), bub(1.0, T["bubble"]-s+4.6),
   {"type":"reticle","x":1060,"y":600,"r":140,"t0":T["bubble"]-s+4.8}, cap("2. A *BUBBLE*", 215, .2, 50),
   cap("WATER RIPS OPEN", 860, T["bubble"]-s+2.0, 38), cap("…AND *COLLAPSES*", 915, T["bubble"]-s+4.6, 40)])
s = cuts[6]
S.shot(6, {"depth":.55,"seabed":"dark","seabedY":860}, [mantis(880, 600, .8, strike=True), snail(1130, 610, .75, cracked=True), cap("SHELL: *CRACKED*", 215, .3, 50)])
s = cuts[7]
S.shot(7, {"depth":.85,"spotlight":{"x":960,"w":320}}, [mantis(960, 470, 1.1), cap("VERDICT", 215, .2, 44),
   {"type":"stamp","text":"Mantis shrimp wins","x":960,"y":760,"size":40,"t0":T["verdict"]-s+.6}])
s = cuts[8]
S.shot(8, {"mode":"paper"}, [{"type":"doccard","x":960,"y":520,"w":470,"h":600,"header":"Lab file","title":"The club","footer":"Studied for tougher materials"},
   cap("SO TOUGH, *ENGINEERS*", 900, .2, 38), cap("STUDY IT", 955, .9, 38)])
s = cuts[9]
S.shot(9, {"depth":.5,"seabed":"dark","seabedY":860}, [mantis(980, 600, .9), cap("WHO FIGHTS *NEXT*?", 215, .3, 48),
   {"type":"pill","text":"Comment your matchup","x":768,"y":900,"size":24,"t0":1.0}], fadeOut=.5)
S.save({"style":"thriller","end":END,"pulse_from":c("spring"),"hits":[.12,T["first"]+.2,T["bubble"]+4.8],"accents":[T["twice"],T["shell"]+.3],
 "riser":[T["shell"],T["verdict"]+.1],"impact":T["verdict"]+.6,
 "whoosh":[T["h2"]+.2,T["size"]+1.4,T["club"]+1.0,T["speed"]+.4,T["speed"]+3.0,T["fast"]+.8,T["twice"],T["bubble"]+2.0,T["twist"]+.2,T["cta"]+.3]})
