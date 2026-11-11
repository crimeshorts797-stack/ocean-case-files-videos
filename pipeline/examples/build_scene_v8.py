import sys; sys.path.insert(0, "/home/claude/pipeline")
from scenelib import *
T = load("v8"); c = lambda k, d=.2: T[k]-d
cuts = [0, c("folk"), c("sat"), c("weeks"), c("yacht"), c("sus"), c("q"), c("verdict",.25), c("cta"), END]
S = Scene("v8", "CASE #005", cuts)
glowsea = lambda op=.8: svg(f"<defs><radialGradient id='ms' cx='.5' cy='.5' r='.5'><stop offset='0' stop-color='#e8fff8' stop-opacity='{op}'/><stop offset='.6' stop-color='#9fe8d8' stop-opacity='{op*.6}'/><stop offset='1' stop-color='#9fe8d8' stop-opacity='0'/></radialGradient></defs><ellipse cx='960' cy='760' rx='700' ry='320' fill='url(#ms)'/>")
ship = "<g transform='translate(960 560)'><path d='M-110,0 L110,0 L80,40 L-80,40 Z' fill='#1b1f24'/><line x1='0' y1='0' x2='0' y2='-170' stroke='#1b1f24' stroke-width='6'/><path d='M4,-160 L4,-10 L90,-10 Z' fill='#d9dee2'/></g>"
S.shot(0, {"mode":"black"}, [glowsea(.75), svg(ship, 0), cap("SAILORS' STORIES", 230, .2, 44),
   cap("THE SEA TURNED *WHITE*", 880, T["white"]-.05, 40)], fadeIn=.3)
s = cuts[1]
S.shot(1, {"mode":"paper"}, [{"type":"doccard","x":960,"y":540,"w":470,"h":600,"header":"Ship logs","title":"Glowing\nseas","footer":"Folklore?"},
   {"type":"stamp","text":"Myth?","x":960,"y":640,"size":60,"color":"#f5a623","t0":.8}, cap("THEN: *SPACE*", 175, T["space"]-s+.2, 46)])
s = cuts[2]
earth = "<circle cx='960' cy='1450' r='900' fill='#0d2b3e'/><path d='M560,700 C700,640 860,660 960,700 C1060,740 1200,700 1340,720 L1340,760 C1200,760 1100,790 960,770 C820,750 700,740 560,760 Z' fill='#2b3a2a'/>"
patch = "<ellipse cx='980' cy='860' rx='190' ry='70' fill='#d8fff4' opacity='.85' filter='url(#glow)'/>"
S.shot(2, {"mode":"black"}, [svg(earth, 0), satellite(960, 260, .9), svg(patch, 1.2),
   cap("*2019*: SOUTH OF JAVA", 400, .3, 40),
   {"type":"pill","text":"~100,000 km²","x":810,"y":445,"size":28,"t0":T["size"]-s+.4,"tone":"red"},
   cap("≈ *ICELAND*", 580, T["size"]-s+2.4, 44)], camera={"zoomFrom":1,"zoomTo":1.12,"y":820})
s = cuts[3]
S.shot(3, {"mode":"black"}, [glowsea(.9), cap("GLOWING FOR", 230, .2, 44), cap("*WEEKS*", 300, .8, 80)])
s = cuts[4]
S.shot(4, {"mode":"black"}, [glowsea(1.0), svg(ship, 0), cap("A YACHT SAILED", 215, .2, 42), cap("*RIGHT THROUGH IT*", 275, 1.0, 44),
   cap("BRIGHTER THAN THE", 880, T["crew"]-s+.4, 36), cap("*NIGHT SKY*", 935, T["crew"]-s+1.6, 46)])
s = cuts[5]
dots = "".join(f"<circle cx='{700+(i*137)%520}' cy='{420+(i*89)%400}' r='{6+(i%3)*3}' fill='#c9fff0' filter='url(#glow)' opacity='.9'/>" for i in range(40))
S.shot(5, {"mode":"black"}, [svg(dots, .4), cap("SUSPECT: *BACTERIA*", 215, .2, 44),
   cap("TRILLIONS", 860, T["sus"]-s+2.4, 50), cap("GLOWING *TOGETHER*", 920, T["sus"]-s+3.8, 40)], camera={"zoomFrom":1,"zoomTo":1.15})
s = cuts[6]
S.shot(6, {"mode":"paper"}, [{"type":"checklist","title":"Still unknown","x":715,"y":380,"w":490,"items":[{"text":"Why there?"},{"text":"Why then?"},{"text":"What triggers it?"}]},
   {"type":"redx","x":731,"y":412,"size":18,"t0":1.0},{"type":"redx","x":731,"y":482,"size":18,"t0":1.9},{"type":"redx","x":731,"y":552,"size":18,"t0":3.0}])
s = cuts[7]
S.shot(7, {"mode":"paper"}, [{"type":"doccard","x":960,"y":520,"w":470,"h":600,"header":"Case #005","title":"Milky seas\nJava, 2019","footer":"Seen from space"},
   cap("IT'S *REAL*", 175, .3, 50), {"type":"stamp","text":"Unsolved","x":960,"y":640,"size":66,"t0":T["verdict"]-s+1.6}])
s = cuts[8]
S.shot(8, {"mode":"black"}, [glowsea(.9), svg(ship, 0), cap("WOULD YOU", 215, .3, 46), cap("*SAIL INTO IT*?", 280, 1.0, 54),
   {"type":"pill","text":"Follow for the next case","x":752,"y":930,"size":24,"t0":2.0}], fadeOut=.6)
S.save({"style":"mystery","end":END,"pulse_from":c("sat"),"impact":T["verdict"]+1.6,"hits":[T["space"]],
 "pings":[T["sat"]+1.2,T["size"]+.4,T["sus"]+2.4],
 "whoosh":[T["white"],T["folk"]+.8,T["space"]+.2,T["size"]+2.4,T["weeks"]+.8,T["yacht"]+1.0,T["crew"]+1.6,T["sus"]+.2,T["q"]+1.0,T["q"]+1.9,T["q"]+3.0,T["verdict"]+.3,T["cta"]+1.0]})
