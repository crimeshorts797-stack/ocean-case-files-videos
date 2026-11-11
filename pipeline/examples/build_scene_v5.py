import sys; sys.path.insert(0, "/home/claude/pipeline")
from scenelib import *
T = load("v5"); c = lambda k, d=.2: T[k]-d
cuts = [0, c("seen"), c("e1"), c("e2"), c("nz"), c("e3"), c("leave"), c("verdict",.25), c("twist"), c("cta"), END]
S = Scene("v5", "WHO WINS? #002", cuts)
S.shot(0, {"depth":.92,"rays":False,"spotlight":{"x":960,"w":320}}, [
   {"type":"creature","kind":"whale","x":960,"y":330,"scale":1.0,"mode":"silhouette","bob":3},
   {"type":"creature","kind":"squid","x":960,"y":760,"scale":1.0,"mode":"silhouette","flip":True,"phase":2},
   cap("!VS!", 560, .15, 96), cap("IN *TOTAL DARKNESS*", 900, T["h2"]-.05, 38)], fadeIn=.25)
s = cuts[1]
S.shot(1, {"mode":"paper"}, [cap("ALMOST *NOBODY*", 230, .2, 44), cap("HAS SEEN IT", 285, .9, 44),
   {"type":"checklist","title":"The evidence","x":715,"y":420,"w":490,"t0":2.2,"items":[{"text":"The skin"},{"text":"The stomach"},{"text":"The size"}]}])
s = cuts[2]
scars = "".join(f"<circle cx='{x}' cy='{y}' r='{r}' fill='none' stroke='#e9e4dc' stroke-width='4' opacity='.75'/>" for x,y,r in [(860,470,16),(900,455,13),(940,480,18),(985,462,12),(1020,490,15),(880,505,11),(960,512,14),(1050,470,13),(1000,520,10)])
S.shot(3-1, {"depth":.55}, [{"type":"creature","kind":"whale","x":980,"y":500,"scale":1.4,"bob":2},
   svg(scars, T["scars"]-s+.8), cap("EXHIBIT *1*: THE SKIN", 215, .1, 42),
   {"type":"circle","x":950,"y":485,"rx":150,"ry":70,"t0":T["scars"]-s+1.6},
   cap("SUCKER *SCARS*", 820, T["scars"]-s+1.2, 46), {"type":"pill","text":"Point: squid","x":805,"y":880,"size":26,"t0":T["pt"]-s+.2,"check":True}],
   camera={"zoomFrom":1,"zoomTo":1.15,"x":960,"y":490})
s = cuts[3]
beak = "<g transform='translate(960 560)'><path d='M-60,-50 C-20,-90 60,-70 70,0 C40,-10 0,-6 -30,20 Z' fill='#3a2a22'/><path d='M-60,10 C-20,60 50,60 70,10 C40,20 0,18 -30,-6 Z' fill='#2a1d18'/></g>"
S.shot(3, {"depth":.75,"rays":False}, [cap("EXHIBIT *2*: THE STOMACH", 215, .1, 40), svg(beak, .8, layer="overlay"),
   cap("BEAKS DON'T *DIGEST*", 820, T["beaks"]-s+.3, 42)])
s = cuts[4]
S.shot(4, {"mode":"paper"}, [{"type":"bignumber","from":0,"to":23223,"x":960,"y":520,"size":130,"t0":1.2,"dur":2.2},
   cap("BEAKS IN *16* WHALES", 270, .2, 42), cap("NEW ZEALAND STRANDINGS", 325, .9, 28),
   {"type":"pill","text":"Giant squid among them","x":745,"y":640,"size":26,"t0":T["nz"]-s+6.0,"tone":"red"}])
s = cuts[5]
S.shot(5, {"depth":.4}, [cap("EXHIBIT *3*: SIZE", 215, .1, 42),
   {"type":"creature","kind":"whale","x":960,"y":470,"scale":1.5,"bob":2}, {"type":"creature","kind":"squid","x":960,"y":760,"scale":.32,"t0":1.0},
   cap("*100×+* HEAVIER", 880, T["size"]-s+2.0, 52)])
s = cuts[6]
S.shot(6, {"depth":.8,"rays":False}, [{"type":"creature","kind":"whale","x":900,"y":560,"scale":1.15,"swim":{"vx":14}},
   cap("SQUID: *SCARS*", 260, .2, 44), cap("WHALE: *DINNER*", 330, T["leave"]-s+1.6, 44)])
s = cuts[7]
S.shot(7, {"depth":.9,"spotlight":{"x":960,"w":300}}, [{"type":"creature","kind":"whale","x":960,"y":470,"approach":{"from":.8,"to":1.2,"dur":2.0,"t0":0}},
   cap("VERDICT", 215, .2, 44), {"type":"stamp","text":"Sperm whale wins","x":960,"y":760,"size":42,"t0":T["verdict"]-s+.6}])
s = cuts[8]
S.shot(8, {"mode":"paper"}, [{"type":"doccard","x":960,"y":540,"w":470,"h":560,"header":"Evidence file","title":"Giant squid\nis real","footer":"Found in whale stomachs"},
   cap("THE SQUID GETS", 175, .2, 40), cap("THE *LAST WORD*", 228, .9, 44)])
s = cuts[9]
S.shot(9, {"depth":.85}, [{"type":"creature","kind":"whale","x":820,"y":420,"scale":.8,"mode":"silhouette","swim":{"vx":10}},
   {"type":"creature","kind":"shark","x":1100,"y":700,"scale":.6,"mode":"silhouette","flip":True,"swim":{"vx":-10}},
   cap("WHO FIGHTS *NEXT*?", 215, .3, 48), {"type":"pill","text":"Comment your matchup","x":768,"y":880,"size":24,"t0":1.0}], fadeOut=.5)
S.save({"style":"thriller","end":END,"pulse_from":c("seen"),"hits":[.12,T["e1"],T["e2"],T["e3"]],
 "accents":[T["pt"]+.2,T["nz"]+6.0],"riser":[T["leave"],T["verdict"]+.1],"impact":T["verdict"]+.6,
 "whoosh":[T["h2"],T["seen"]+.2,T["seen"]+2.2,T["scars"]+1.2,T["beaks"]+.3,T["nz"]+.2,T["size"]+2.0,T["leave"]+.2,T["leave"]+1.6,T["twist"]+.9,T["cta"]+.3]})
