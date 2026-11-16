import sys; sys.path.insert(0, "/home/claude/pipeline")
from scenelib import *
T = load("v12"); c = lambda k, d=.2: T[k]-d
cuts = [0, c("whale"), c("nose"), c("hunt"), c("db"), c("care"), c("far"), c("verdict",.25), c("cta"), END]
S = Scene("v12", "CASE #008", cuts)
S.shot(0, {"mode":"black"}, [cap("THE *LOUDEST* ANIMAL", 230, .2, 44), cap("ON EARTH?", 290, .9, 44),
   {"type":"pill","text":"Not a lion","x":810,"y":560,"size":28,"t0":2.2,"tone":"red"},{"type":"pill","text":"Not a blue whale","x":790,"y":640,"size":28,"t0":3.4,"tone":"red"}], fadeIn=.2)
s = cuts[1]
S.shot(1, {"depth":.8,"spotlight":{"x":960,"w":320}}, [{"type":"creature","kind":"whale","x":960,"y":520,"approach":{"from":.7,"to":1.2,"dur":2.0,"t0":0}},
   cap("THE *SPERM WHALE*", 850, .4, 52)])
s = cuts[2]
S.shot(2, {"depth":.5}, [{"type":"creature","kind":"whale","x":900,"y":520,"scale":1.05,"bob":2},
   {"type":"circle","x":1010,"y":505,"rx":110,"ry":62,"t0":.8}, cap("THE BIGGEST *NOSE*", 215, .3, 46),
   cap("“MONKEY LIPS”", 820, T["click"]-s+2.4, 46), cap("FIRE *CLICKS*", 880, T["click"]-s+4.4, 42)], camera={"zoomFrom":1,"zoomTo":1.1,"x":980,"y":500})
s = cuts[3]
rings = "".join(f"<circle cx='960' cy='420' r='{r}' fill='none' stroke='#39ff6a' stroke-opacity='{.6-r/800}' stroke-width='3'/>" for r in (60,130,210,300))
S.shot(3, {"mode":"sonar"}, [svg(rings, .2, layer="overlay"), {"type":"creature","kind":"squid","x":960,"y":760,"scale":.5,"mode":"sonar","t0":1.8},
   cap("SONAR", 215, .2, 52), cap("*1,000 M* DOWN", 900, 2.0, 44)])
s = cuts[4]
S.shot(4, {"mode":"paper"}, [cap("*2003*: MEASURED", 200, .2, 42), {"type":"bignumber","from":0,"to":236,"suffix":" dB","x":960,"y":520,"size":130,"t0":.8,"dur":1.6},
   cap("UNDERWATER", 620, 2.6, 34), {"type":"stamp","text":"Record","x":960,"y":800,"size":60,"color":"#3ecf6a","t0":T["rec"]-s+.8}])
s = cuts[5]
S.shot(5, {"mode":"paper"}, [cap("CAREFUL:", 200, .1, 42), cap("WATER ≠ AIR", 260, .8, 52),
   {"type":"factstack","x":720,"y":420,"w":480,"gap":100,"size":28,"items":[{"text":"Underwater: 236 dB","t0":T["air"]-s},{"text":"In air: ~174 dB","t0":T["air"]-s+1.6,"tone":"red"},{"text":"Rock concert: ~120 dB","t0":T["air"]-s+3.6}]}])
s = cuts[6]
S.shot(6, {"depth":.6}, [{"type":"creature","kind":"whale","x":800,"y":420,"scale":.6},{"type":"creature","kind":"whale","x":1120,"y":760,"scale":.4,"flip":True,"dim":True},
   {"type":"bracket","x1":860,"y1":560,"x2":1080,"y2":700,"label":"tens of km","t0":1.0}, cap("HEARD FROM *FAR AWAY*", 215, .2, 42)])
s = cuts[7]
S.shot(7, {"mode":"paper"}, [{"type":"doccard","x":960,"y":520,"w":470,"h":600,"header":"Case #008","title":"Loudest\nanimal","footer":"Sperm whale"},
   {"type":"stamp","text":"Solved","x":960,"y":640,"size":76,"color":"#3ecf6a","t0":T["verdict"]-s+.55}])
s = cuts[8]
S.shot(8, {"depth":.92,"rays":False}, [{"type":"creature","kind":"whale","x":860,"y":540,"scale":.9,"mode":"silhouette","swim":{"vx":10}},
   svg(rings.replace("420","540").replace("cx='960'","cx='1080'"), .4, layer="overlay"),
   cap("HUNTING IN", 215, .2, 44), cap("*TOTAL DARKNESS*", 275, .9, 48), {"type":"pill","text":"Follow for the next case","x":752,"y":900,"size":24,"t0":2.0}], fadeOut=.5)
S.save({"style":"mystery","end":END,"pulse_from":c("hunt"),"impact":T["verdict"]+.55,"hits":[T["whale"],T["rec"]+.8],
 "pings":[T["click"]+4.4,T["hunt"]+.2,T["hunt"]+1.0,T["hunt"]+1.8,T["cta"]+.4,T["cta"]+1.2],
 "whoosh":[2.2,3.4,T["whale"]+.4,T["nose"]+.3,T["click"]+2.4,T["db"]+2.6,T["care"]+.8,T["air"],T["air"]+1.6,T["air"]+3.6,T["far"]+1.0,T["cta"]+.9]})
