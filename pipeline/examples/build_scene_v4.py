import sys, math; sys.path.insert(0, "/home/claude/pipeline")
from scenelib import *
T = load("v4"); c = lambda k, d=.2: T[k]-d
cuts = [0, c("y"), c("name"), c("loud"), c("loc"), c("season"), c("guess"), c("quiet"), c("verdict",.25), c("end"), END]
S = Scene("v4", "CASE #003", cuts)
def sweeps(col="#39ff6a", n=6):
    p = ""
    for i in range(n):
        x0 = 690 + i*95
        p += f"<path d='M{x0},700 Q{x0+40},690 {x0+70},430' fill='none' stroke='{col}' stroke-width='6' stroke-linecap='round' filter='url(#glow)'/>"
    return p
S.shot(0, {"mode":"sonar"}, [svg(sweeps(), .2, layer="overlay"), cap("A SOUND THAT", 260, .3, 46), cap("!NEVER STOPS!", 320, 1.1, 58),
   cap("NO ONE KNOWS", 860, 3.0, 38), cap("WHAT MAKES IT", 912, 3.6, 38)], fadeIn=.25)
s = cuts[1]
hyd = lambda x, y: f"<line x1='{x}' y1='{y}' x2='{x}' y2='1000' stroke='#9fb3bf' stroke-width='3' opacity='.6'/><rect x='{x-16}' y='{y-46}' width='32' height='92' rx='14' fill='#d9e2e6'/><rect x='{x-16}' y='{y-8}' width='32' height='16' fill='#f5a623'/>"
S.shot(1, {"depth":.65,"seabed":"dark","seabedY":930}, [svg(hyd(840,620)+hyd(1080,680)),
   cap("*1991*", 280, .2, 120), {"type":"pill","text":"Old Navy microphones","x":765,"y":330,"size":24,"t0":1.4},
   cap("IT WAS *ALREADY* THERE", 820, T["there"]-s+.2, 38),
   {"type":"reticle","x":840,"y":620,"r":70,"t0":T["there"]-s+.6}])
s = cuts[2]
S.shot(2, {"mode":"sonar"}, [svg(sweeps("#f5a623", 7), 0, layer="overlay"),
   cap("“THE *UPSWEEP*”", 270, .2, 64), cap("RISING TONES", 820, T["train"]-s+.6, 40), cap("AGAIN AND AGAIN", 872, T["train"]-s+2.4, 34)])
s = cuts[3]
rings = "".join(f"<circle cx='960' cy='560' r='{r}' fill='none' stroke='#39ff6a' stroke-opacity='{.5-r/1000}' stroke-width='3'/>" for r in (60,140,240,360,480))
S.shot(3, {"mode":"black"}, [svg(rings, .1, layer="overlay"), svg("<circle cx='960' cy='560' r='18' fill='#39ff6a' filter='url(#glow)'/>", 0, layer="overlay"),
   cap("HEARD ACROSS", 230, .3, 44), cap("THE *WHOLE PACIFIC*", 290, 1.2, 50)])
s = cuts[4]
S.shot(4, {"mode":"paper"}, [{"type":"doccard","x":960,"y":520,"w":470,"h":600,"header":"Source location","title":"54° South\n140° West","footer":"Far South Pacific"},
   cap("*THOUSANDS* OF KM", 900, 3.4, 40), cap("FROM ANY COAST", 955, 4.2, 34)])
s = cuts[5]
S.shot(5, {"depth":.5}, [cap("IT'S *SEASONAL*", 230, .2, 50),
   {"type":"factstack","x":720,"y":420,"w":480,"gap":92,"size":25,"items":[{"text":"Peaks: spring","t0":1.4},{"text":"Peaks: autumn","t0":2.2},{"text":"Source or ocean?","t0":T["why"]-s+.8,"tone":"red"}]}])
s = cuts[6]
volc = "<polygon points='700,1000 900,700 1020,700 1220,1000' fill='#1a1412'/><polygon points='900,700 1020,700 990,730 930,730' fill='#e5383b' filter='url(#glow)'/>"
S.shot(6, {"depth":.85,"rays":False}, [svg(volc), svg("".join(f"<circle cx='{960+(i%3-1)*30}' cy='{640-i*45}' r='{10+i*3}' fill='#5d5552' opacity='{.5-i*.06}'/>" for i in range(7)), .5),
   cap("BEST GUESS:", 220, .2, 40), cap("*UNDERWATER VOLCANO*", 280, .9, 46),
   {"type":"stamp","text":"Not proven","x":960,"y":480,"size":58,"t0":T["proof"]-s+.2}], camera={"zoomFrom":1,"zoomTo":1.1,"y":700})
s = cuts[7]
S.shot(7, {"mode":"sonar"}, [{"type":"meter","x":720,"y":480,"w":480,"value":.35,"title":"Loudness since 1991","t0":.2,"dur":2.4},
   cap("GETTING *QUIETER*", 800, 1.2, 42), cap("ORIGIN: !UNRESOLVED!", 860, T["noaa"]-s+2.2, 40)])
s = cuts[8]
S.shot(8, {"mode":"paper"}, [{"type":"doccard","x":960,"y":520,"w":470,"h":600,"header":"Case #003","title":"The Upsweep\n1991 – today","footer":"Source: unknown"},
   {"type":"stamp","text":"Unsolved","x":960,"y":640,"size":66,"t0":T["verdict"]-s+.55}])
s = cuts[9]
S.shot(9, {"mode":"sonar"}, [{"type":"sonar","x":960,"y":560,"r":520,"spread":179,"speed":1.1,"t0":0}, svg(sweeps("#39ff6a",4), .8, layer="overlay"),
   cap("WHAT IS STILL", 215, .2, 44), cap("*SINGING* DOWN THERE?", 275, .9, 46),
   {"type":"pill","text":"Follow for the next case","x":752,"y":900,"size":24,"t0":2.0}], fadeOut=.5)
S.save({"style":"mystery","end":END,"pulse_from":c("loud"),"impact":T["verdict"]+.55,"hits":[.15,T["proof"]+.2],
 "pings":[T["there"]+.6,T["loud"],T["loud"]+1.5,T["end"]+.5],
 "whoosh":[1.1,3.0,T["y"]+1.4,T["name"],T["train"]+.6,T["loc"]+3.4,T["season"],T["why"]+.8,T["guess"]+.9,T["quiet"]+1.2,T["noaa"]+2.2,T["end"]+.9]})
