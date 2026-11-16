import sys; sys.path.insert(0, "/home/claude/pipeline")
from scenelib import *
import math
T = load("v16"); c = lambda k, d=.2: T[k]-d
cuts = [0, c("dark"), c("bite"), c("lose"), c("q"), c("y20"), c("human"), c("verdict",.25), c("cta"), END]
S = Scene("v16", "CASE #011", cuts)
S.shot(0, {"depth":.95,"rays":False}, [angler(960, 520, 1.3), tinymale(860, 610, 1.0, t0=1.5), cap("A BITE THAT", 820, .4, 46), cap("*NEVER* LETS GO", 885, 1.2, 50)], fadeIn=.3)
s = cuts[1]
S.shot(1, {"depth":.98,"rays":False}, [svg("<circle cx='1080' cy='420' r='14' fill='#cffff2' filter='url(#glow)'/>", .2, layer="overlay"),
   cap("PITCH *BLACK*", 215, .2, 52), angler(900, 560, .9, t0=T["size"]-s), tinymale(1170, 640, 1.0, t0=T["size"]-s+.6),
   cap("FEMALE: UP TO *60×* LONGER", 900, T["size"]-s+1.6, 36)])
s = cuts[2]
S.shot(2, {"depth":.95,"rays":False}, [angler(960, 480, 1.2), tinymale(880, 572, 1.0), {"type":"circle","x":880,"y":572,"rx":50,"ry":34,"t0":.4},
   cap("HE *BITES*", 215, .2, 56), cap("SKIN + BLOOD *FUSE*", 860, T["fuse"]-s+.4, 42)], camera={"zoomFrom":1,"zoomTo":1.25,"x":900,"y":560})
s = cuts[3]
S.shot(3, {"mode":"paper"}, [cap("HE LOSES:", 200, .2, 48),
   {"type":"checklist","title":"Male anglerfish","x":715,"y":320,"w":490,"items":[{"text":"Eyes"},{"text":"Fins"},{"text":"Independence"}]},
   {"type":"redx","x":731,"y":352,"size":18,"t0":1.0},{"type":"redx","x":731,"y":422,"size":18,"t0":1.7},{"type":"redx","x":731,"y":492,"size":18,"t0":2.6}])
s = cuts[4]
S.shot(4, {"mode":"paper"}, [cap("BUT WAIT…", 200, .1, 52), cap("BODIES *REJECT*", 480, 1.0, 50), cap("FOREIGN TISSUE", 545, 1.6, 44), cap("SO WHY NOT *HERS*?", 760, 3.2, 46)])
s = cuts[5]
dna = "".join(f"<circle cx='{960+math.sin(i*.6)*80:.0f}' cy='{300+i*24}' r='9' fill='#f5a623'/><circle cx='{960-math.sin(i*.6)*80:.0f}' cy='{300+i*24}' r='9' fill='#39b8ff'/>" for i in range(20))
S.shot(5, {"mode":"black"}, [svg(dna, .3), cap("*2020*: DNA STUDY", 200, .2, 44),
   {"type":"pill","text":"Key immune parts: lost","x":770,"y":860,"size":28,"t0":T["immune"]-s+1.6,"tone":"red"}], camera={"zoomFrom":1,"zoomTo":1.15,"y":520})
s = cuts[6]
S.shot(6, {"mode":"black"}, [cap("FOR HUMANS:", 480, .2, 46), cap("*FATAL*", 580, 1.0, 96)])
s = cuts[7]
S.shot(7, {"mode":"paper"}, [{"type":"doccard","x":960,"y":520,"w":470,"h":600,"header":"Case #011","title":"Anglerfish\nfusion","footer":"Science, 2020"},
   {"type":"stamp","text":"True","x":960,"y":640,"size":84,"color":"#3ecf6a","t0":T["verdict"]-s+.55}])
s = cuts[8]
S.shot(8, {"depth":.95,"rays":False}, [angler(960, 500, 1.1), tinymale(872, 590, .9), cap("STRANGEST", 820, .3, 46), cap("*RELATIONSHIP*?", 885, 1.0, 50),
   {"type":"pill","text":"Follow for the next case","x":752,"y":950,"size":24,"t0":1.8}], fadeOut=.5)
S.save({"style":"melancholy","end":END,"impact":T["verdict"]+.55,"hits":[T["bite"]+.4,T["human"]+1.0],
 "pings":[1.5,T["dark"]+.2,T["immune"]+1.6],
 "whoosh":[.4,1.2,T["size"]+1.6,T["fuse"]+.4,T["lose"]+1.0,T["lose"]+1.7,T["lose"]+2.6,T["q"]+1.0,T["y20"]+.2,T["cta"]+1.0]})
