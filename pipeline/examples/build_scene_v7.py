import sys; sys.path.insert(0, "/home/claude/pipeline")
from scenelib import *
T = load("v7"); c = lambda k, d=.2: T[k]-d
cuts = [0, c("not"), c("ant"), c("pit"), c("own"), c("how"), c("only"), c("verdict",.25), c("why"), c("cta"), END]
S = Scene("v7", "WHO WINS? #003", cuts)
S.shot(0, {"depth":.5,"sun":{"x":960,"y":540,"r":520}}, [
   {"type":"creature","kind":"orca","x":960,"y":330,"scale":1.1,"mode":"silhouette"},
   humpback(960, 740, .95, flip=True, body="#05090d", belly="#05090d"),
   cap("!VS!", 560, .15, 96), cap("ORCA = *TOP PREDATOR*", 900, T["h2"]+.3, 36)], fadeIn=.25)
s = cuts[1]
S.shot(1, {"mode":"black"}, [cap("NOT", 520, .1, 120), cap("*QUITE.*", 640, .5, 120)])
s = cuts[2]
ice = "<polygon points='640,560 1280,560 1240,610 680,610' fill='#e6f3f8'/><polygon points='680,610 1240,610 1200,700 720,700' fill='#bcd9e4'/>"
S.shot(2, {"depth":.15,"surface":True}, [svg(ice), seal(960, 540, 1.0, t1=T["hb"]-s+1.0),
   {"type":"creature","kind":"orca","x":700,"y":820,"scale":.7,"swim":{"vx":30}},
   cap("ANTARCTICA, *2009*", 215, .2, 44),
   humpback(960, 840, .95, t0=T["hb"]-s), seal(990, 770, .7, t0=T["hb"]-s+1.6),
   cap("SEAL SAVED BY A *HUMPBACK*", 980, T["hb"]-s+2.4, 34)])
s = cuts[3]
S.shot(3, {"mode":"paper"}, [cap("ROBERT PITMAN'S *FILE*", 215, .2, 40),
   {"type":"bignumber","from":0,"to":115,"x":960,"y":560,"size":180,"t0":T["n"]-s+.8,"dur":1.6},
   cap("ENCOUNTERS", 650, T["n"]-s+1.8, 40), cap("1951 – 2012", 710, T["n"]-s+3.6, 32)])
s = cuts[4]
S.shot(4, {"depth":.45}, [cap("WHO DID THEY PROTECT?", 215, .2, 40),
   {"type":"factstack","x":720,"y":400,"w":480,"gap":88,"size":25,"items":[
     {"text":"Own calves: ~1 in 10","t0":1.2},{"text":"Seals + sea lions","t0":T["rest"]-s+.6,"check":True},
     {"text":"Gray whales","t0":T["rest"]-s+1.8,"check":True},{"text":"Even a sunfish","t0":T["rest"]-s+2.8,"check":True,"tone":"red"}]}])
s = cuts[5]
S.shot(5, {"depth":.35}, [humpback(900, 520, 1.15, t0=0), {"type":"creature","kind":"orca","x":1250,"y":820,"scale":.55,"flip":True,"swim":{"vx":-60},"t0":1.5},
   cap("TRUMPET. SLAP. *CHARGE.*", 215, .3, 42)], camera={"zoomFrom":1,"zoomTo":1.12})
s = cuts[6]
S.shot(6, {"depth":.6}, [humpback(960, 500, 1.0), cap("THE *ONLY* WHALES", 215, .2, 46), cap("KNOWN TO DRIVE", 820, 1.0, 38), cap("ORCAS *OFF*", 875, 1.8, 46)])
s = cuts[7]
S.shot(7, {"depth":.85,"spotlight":{"x":960,"w":320}}, [humpback(960, 470, 1.0), cap("VERDICT", 215, .2, 44),
   {"type":"stamp","text":"Humpbacks win","x":960,"y":760,"size":58,"color":"#3ecf6a","t0":T["verdict"]-s+.6}])
s = cuts[8]
S.shot(8, {"depth":.5}, [humpback(860, 560, .8), cap("WHY?", 215, .2, 72),
   {"type":"pill","text":"Maybe they hear orcas hunt","x":730,"y":800,"size":24,"t0":2.0}])
s = cuts[9]
S.shot(9, {"depth":.4,"sun":{"x":960,"y":430,"r":420}}, [humpback(960, 470, .9, body="#05090d", belly="#05090d"),
   cap("A *HERO*?", 820, .2, 72), {"type":"pill","text":"Tell us in the comments","x":752,"y":900,"size":24,"t0":1.2}], fadeOut=.5)
S.save({"style":"thriller","end":END,"pulse_from":c("ant"),"hits":[.12,T["not"]],"accents":[T["how"]+.4,T["how"]+1.2,T["how"]+2.0],
 "riser":[T["only"],T["verdict"]+.1],"impact":T["verdict"]+.6,
 "whoosh":[T["h2"]+.3,T["ant"]+.2,T["hb"]+2.4,T["n"]+1.8,T["own"]+.2,T["rest"]+.6,T["rest"]+1.8,T["rest"]+2.8,T["only"]+1.0,T["why"]+2.0,T["cta"]+.2]})
