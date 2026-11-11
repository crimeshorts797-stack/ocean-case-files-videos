import sys; sys.path.insert(0, "/home/claude/pipeline")
from scenelib import *
T = load("v6"); c = lambda k, d=.2: T[k]-d
cuts = [0, c("what"), c("cent"), c("eye"), c("dated"), c("range"), c("moms"), c("verdict",.25), c("end"), END]
S = Scene("v6", "CASE #004", cuts)
GS = dict(kind="shark", mode="ghost")
S.shot(0, {"depth":.85,"rays":False}, [greenland(960,560,1.25),
   cap("ALIVE BEFORE", 230, .3, 46), cap("THE *USA* EXISTED?", 290, 1.2, 50)], fadeIn=.4, camera={"zoomFrom":1.08,"zoomTo":1})
s = cuts[1]
S.shot(1, {"depth":.35,"surface":True}, [greenland(960,600,1.0),
   cap("GREENLAND SHARK", 230, .2, 46), {"type":"pill","text":"Water near 0 °C","x":790,"y":270,"size":24,"t0":1.6},
   cap("GROWS *~1 CM* A YEAR", 860, T["grow"]-s+.4, 40)])
s = cuts[2]
S.shot(2, {"mode":"paper"}, [cap("HOW OLD?", 215, .2, 52),
   {"type":"checklist","title":"Ways to age a fish","x":715,"y":420,"w":490,"t0":1.0,"items":[{"text":"Growth rings"},{"text":"Hard bones"}]},
   {"type":"redx","x":731,"y":452,"size":18,"t0":T["cent"]-s+3.0},{"type":"redx","x":731,"y":522,"size":18,"t0":T["cent"]-s+3.9}])
s = cuts[3]
eyeart = "<g transform='translate(960 560)'><ellipse rx='230' ry='150' fill='#d9dcd7'/><circle r='110' fill='#3b4a52'/><circle r='70' fill='#0d1215'/><circle r='24' fill='#f5a623' filter='url(#glow)'/></g>"
S.shot(3, {"depth":.7,"rays":False}, [svg(eyeart, .3), cap("A CLOCK IN THE *EYE*", 215, .4, 46),
   {"type":"circle","x":960,"y":560,"rx":45,"ry":45,"t0":T["lens"]-s+.5}, cap("LENS CORE: FORMED", 820, T["lens"]-s+.6, 36), cap("*BEFORE BIRTH*", 875, T["lens"]-s+1.4, 44)],
   camera={"zoomFrom":1,"zoomTo":1.2,"y":560})
s = cuts[4]
S.shot(4, {"mode":"paper"}, [cap("*28* SHARKS DATED", 215, .2, 46),
   greenland(960,520,1.15,t0=T["big"]-s),
   {"type":"bracket","x1":700,"y1":640,"x2":1220,"y2":640,"label":"5 m","t0":T["big"]-s+.8},
   {"type":"bignumber","from":0,"to":392,"suffix":" yrs","x":960,"y":800,"size":110,"t0":T["big"]-s+2.4,"dur":1.6}])
s = cuts[5]
S.shot(5, {"depth":.5}, [{"type":"meter","x":720,"y":470,"w":480,"value":.8,"title":"Age estimate","t0":.2,"dur":1.6},
   cap("*272* – *512* YEARS", 680, .8, 50),
   {"type":"pill","text":"Critics: at least 200","x":768,"y":800,"size":26,"t0":T["crit"]-s+2.4,"check":True}])
s = cuts[6]
S.shot(6, {"depth":.6}, [greenland(960,540,1.1),
   cap("MOTHERS AT", 230, .2, 44), cap("*~150* YEARS", 300, .9, 66, fade=.2)])
s = cuts[7]
S.shot(7, {"mode":"paper"}, [{"type":"doccard","x":960,"y":520,"w":470,"h":600,"header":"Case #004","title":"Greenland\nshark age","footer":"Science, 2016"},
   {"type":"stamp","text":"Solved","x":960,"y":640,"size":76,"color":"#3ecf6a","t0":T["verdict"]-s+.55},
   cap("OLDEST KNOWN *VERTEBRATE*", 920, T["verdict"]-s+1.6, 34)])
s = cuts[8]
S.shot(8, {"depth":.92,"rays":False}, [greenland(900,540,.9),
   cap("ONE MAY STILL BE", 215, .2, 42), cap("*OUT THERE*", 280, .9, 62),
   {"type":"pill","text":"Follow for the next case","x":752,"y":880,"size":24,"t0":2.0}], fadeOut=.6)
S.save({"style":"melancholy","end":END,"impact":T["verdict"]+.55,"hits":[T["eye"]],
 "pings":[T["lens"]+.5,T["big"]+2.4,T["end"]+1.0],
 "whoosh":[1.2,T["what"],T["grow"]+.4,T["cent"]+3.0,T["cent"]+3.9,T["lens"]+1.4,T["dated"],T["range"]+.8,T["crit"]+2.4,T["moms"]+.9,T["verdict"]+1.6,T["end"]+.9]})
