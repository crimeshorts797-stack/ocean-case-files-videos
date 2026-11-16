import sys; sys.path.insert(0, "/home/claude/pipeline")
from scenelib import *
T = load("v13"); c = lambda k, d=.2: T[k]-d
cuts = [0, c("size"), c("when"), c("real"), c("s1"), c("s3"), c("over"), c("verdict",.25), c("cta"), END]
S = Scene("v13", "CASE #009", cuts)
S.shot(0, {"depth":.85,"rays":False}, [{"type":"creature","kind":"shark","x":960,"y":520,"approach":{"from":.8,"to":1.6,"dur":3.5,"t0":0},"mode":"silhouette"},
   cap("WHAT *KILLED*", 790, 1.2, 50), cap("THE GIANT?", 855, 1.9, 50)], fadeIn=.3)
s = cuts[1]
S.shot(1, {"depth":.6}, [{"type":"creature","kind":"shark","x":960,"y":480,"scale":1.2,"bob":2},
   {"type":"creature","kind":"fish","x":960,"y":760,"scale":.35,"t0":.6}, cap("MEGALODON", 215, .2, 56),
   {"type":"bracket","x1":700,"y1":660,"x2":1220,"y2":660,"label":"~15 m","t0":1.4}])
s = cuts[2]
S.shot(2, {"mode":"paper"}, [cap("OLD ESTIMATE", 200, .1, 42), cap("*2.6*", 400, .6, 130), cap("MILLION YEARS AGO", 470, 1.0, 34),
   cap("*2019* RECHECK:", 760, T["y19"]-s+.4, 40), {"type":"pill","text":"California + Mexico fossils","x":745,"y":800,"size":26,"t0":T["y19"]-s+1.4}])
s = cuts[3]
S.shot(3, {"mode":"paper"}, [cap("REAL FOSSILS STOP AT", 200, .1, 36), cap("*3.6*", 420, .6, 150), cap("MILLION YEARS AGO", 500, 1.0, 34),
   cap("*1 MILLION* YEARS EARLIER", 640, 3.0, 36)])
s = cuts[4]
S.shot(4, {"mode":"paper"}, [cap("THE *SUSPECTS*", 200, .1, 50),
   {"type":"factstack","x":720,"y":360,"w":480,"gap":110,"size":28,"items":[{"text":"1. Cooling ocean","t0":.6},{"text":"2. Changing prey","t0":T["s2"]-s+.4},{"text":"3. A rival","t0":c("s3")-s+.2,"tone":"red"}]}])
s = cuts[5]
S.shot(5, {"depth":.45}, [{"type":"creature","kind":"shark","x":820,"y":420,"scale":1.4,"dim":True,"bob":1},
   {"type":"creature","kind":"shark","x":1060,"y":760,"scale":.55,"flip":True,"swim":{"vx":-30},"t0":.6},
   {"type":"namecard","title":"GREAT WHITE","sub":"from ~4 million years ago","x":960,"y":890,"w":360,"t0":1.8},
   cap("A SMALLER, *FASTER* RIVAL", 200, .2, 36)])
s = cuts[6]
S.shot(6, {"depth":.6}, [{"type":"creature","kind":"shark","x":960,"y":520,"scale":.8,"swim":{"vx":12}},
   cap("*OUTCOMPETED*?", 215, .3, 56), cap("POSSIBLY.", 860, 2.4, 44)])
s = cuts[7]
S.shot(7, {"mode":"paper"}, [{"type":"doccard","x":960,"y":520,"w":470,"h":600,"header":"Case #009","title":"Megalodon's\nextinction","footer":"PeerJ, 2019"},
   {"type":"stamp","text":"Unsolved","x":960,"y":640,"size":66,"t0":T["verdict"]-s+.55}])
s = cuts[8]
S.shot(8, {"depth":.9,"rays":False}, [{"type":"creature","kind":"shark","x":900,"y":520,"scale":1.2,"mode":"silhouette","swim":{"vx":8}},
   cap("WHO DID IT?", 215, .3, 60), {"type":"pill","text":"Comment your suspect","x":768,"y":900,"size":24,"t0":1.2}], fadeOut=.5)
S.save({"style":"mystery","end":END,"pulse_from":c("s1"),"impact":T["verdict"]+.55,"hits":[.15,T["real"]+.6],
 "whoosh":[1.2,1.9,T["size"]+1.4,T["y19"]+.4,T["real"]+3.0,T["s1"]+.6,T["s2"]+.4,T["s3"],T["gw"]+1.8,T["over"]+2.4,T["cta"]+1.2]})
