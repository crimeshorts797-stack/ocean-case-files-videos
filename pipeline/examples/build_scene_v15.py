import sys; sys.path.insert(0, "/home/claude/pipeline")
from scenelib import *
T = load("v15"); c = lambda k, d=.2: T[k]-d
cuts = [0, c("three"), c("neur"), c("each"), c("y20"), c("team"), c("verdict",.25), c("cta"), END]
S = Scene("v15", "CASE #010", cuts)
S.shot(0, {"depth":.6,"spotlight":{"x":960,"w":320}}, [octopus(960, 420, 1.3), cap("*9* BRAINS?", 860, .4, 72)], fadeIn=.25)
s = cuts[1]
S.shot(1, {"mode":"paper"}, [cap("THE TRUE PARTS", 200, .1, 44),
   {"type":"factstack","x":720,"y":360,"w":480,"gap":110,"size":30,"items":[{"text":"3 hearts","t0":1.2,"check":True},{"text":"Blue blood","t0":2.4,"check":True}]}])
s = cuts[2]
dots = lambda cx, cy, n, col: "".join(f"<circle cx='{cx+(i%8-4)*22}' cy='{cy+(i//8)*22}' r='7' fill='{col}'/>" for i in range(n))
S.shot(2, {"depth":.5}, [octopus(960, 360, .9), cap("~500 MILLION *NEURONS*", 200, .2, 38),
   svg(dots(960, 300, 8, "#f5a623"), 1.6, layer="overlay"), {"type":"pill","text":"Head: ~1/3","x":835,"y":250,"size":26,"t0":2.2},
   {"type":"pill","text":"Arms + body: ~2/3","x":780,"y":900,"size":28,"t0":T["arms"]-s+.3,"tone":"red"}])
s = cuts[3]
S.shot(3, {"depth":.5}, [octopus(960, 380, .9), *[{"type":"reticle","x":890+(i%4)*48,"y":660+(i//4)*40,"r":22,"t0":.8+i*.12} for i in range(8)],
   cap("SUCKERS *FEEL* + *TASTE*", 200, T["each"]-s+2.4, 36), cap("“1 + 8 MINI BRAINS”", 900, T["so"]-s+1.6, 42)])
s = cuts[4]
maze = "<path d='M700,820 L700,500 L960,500 L960,380 M1220,820 L1220,500 L960,500' stroke='#d9e2e6' stroke-width='14' fill='none'/><circle cx='1220' cy='820' r='22' fill='#f5a623'/>"
S.shot(4, {"depth":.45}, [svg(maze, .4), octopus(960, 260, .55), cap("*2020*: THE MAZE TEST", 920, .2, 40, t1=T["used"]-s+.6),
   svg("<path d='M960,380 L960,500 L1220,500 L1220,790' stroke='#c4564a' stroke-width='16' fill='none' stroke-linecap='round'/>", T["used"]-s),
   cap("EYES + *CENTRAL BRAIN*", 920, T["used"]-s+.8, 36), cap("STEER THE ARM", 975, T["used"]-s+1.8, 34)])
s = cuts[5]
S.shot(5, {"mode":"paper"}, [cap("ARMS: *CLEVER*", 200, .2, 46), cap("BUT NOT *ALONE*", 260, 1.2, 46),
   cap("“ONE BRAIN,", 600, T["quote"]-s+.6, 52), cap("8 VERY *CLEVER* ARMS”", 670, T["quote"]-s+1.6, 46), {"type":"pill","text":"Current Biology, 2020","x":815,"y":740,"size":22,"t0":T["quote"]-s+2.6}])
s = cuts[6]
S.shot(6, {"mode":"paper"}, [{"type":"doccard","x":960,"y":520,"w":470,"h":600,"header":"Case #010","title":"Octopus:\n9 brains?","footer":"Octopus vulgaris"},
   {"type":"stamp","text":"Half true","x":960,"y":640,"size":66,"color":"#f5a623","t0":T["verdict"]-s+.55}])
s = cuts[7]
S.shot(7, {"depth":.6}, [octopus(960, 420, 1.1), cap("WHICH FACT *SURPRISED* YOU?", 860, .3, 34),
   {"type":"pill","text":"Follow for the next case","x":752,"y":940,"size":24,"t0":1.6}], fadeOut=.5)
S.save({"style":"mystery","end":END,"pulse_from":c("y20"),"impact":T["verdict"]+.55,"hits":[T["so"]+1.6],
 "pings":[T["neur"]+1.6,T["each"]+.8,T["used"]],
 "whoosh":[.4,T["three"]+1.2,T["three"]+2.4,T["arms"]+.3,T["each"]+2.4,T["y20"]+.2,T["used"]+.8,T["team"]+.2,T["team"]+1.2,T["quote"]+.2,T["cta"]+.3]})
