import sys; sys.path.insert(0, "/home/claude/pipeline")
from scenelib import *
T = load("v10"); c = lambda k, d=.2: T[k]-d
cuts = [0, c("what"), c("jet"), c("bang"), c("saw"), c("heat"), c("name"), c("verdict",.25), c("cta"), END]
S = Scene("v10", "CASE #007", cuts)
def shrimp(x, y, s=1.0, t0=0, open_=True, **k):
    claw = ("<path fill='#e05a3a' d='M60,-10 C110,-50 200,-40 220,-10 C200,0 150,0 110,4 Z'/>"
            "<path fill='#c8462b' d='M60,6 C110,40 200,36 220,10 C190,4 150,8 110,4 Z'/>") if open_ else \
           "<path fill='#e05a3a' d='M60,-10 C110,-34 200,-26 222,0 C200,26 110,34 60,10 Z'/>"
    legs = "".join(f"<line x1='{-60+i*22}' y1='18' x2='{-70+i*22}' y2='52' stroke='#d9765c' stroke-width='4'/>" for i in range(5))
    m = (f"<g transform='translate({x} {y}) scale({s})'>{legs}"
         "<path fill='#f08a6a' d='M-150,0 C-120,-40 30,-44 70,-12 C80,0 80,10 70,20 C30,40 -120,36 -150,0 Z'/>"
         "<path fill='#f08a6a' d='M-150,0 L-200,-26 L-190,0 L-200,26 Z'/>"
         + "".join(f"<path d='M{-110+i*30},-30 q6,30 0,60' stroke='#d9765c' stroke-width='3' fill='none'/>" for i in range(5))
         + claw + "<line x1='60' y1='-14' x2='110' y2='-90' stroke='#f08a6a' stroke-width='3'/><line x1='60' y1='-14' x2='130' y2='-70' stroke='#f08a6a' stroke-width='3'/>"
         "<circle cx='50' cy='-16' r='6' fill='#111'/></g>")
    return svg(m, t0, **k)
bubble = lambda x, y, r, t0, t1=None: svg(f"<circle cx='{x}' cy='{y}' r='{r}' fill='none' stroke='#cfefff' stroke-width='5' opacity='.9'/><circle cx='{x-r*.3}' cy='{y-r*.3}' r='{r*.2}' fill='#ffffff' opacity='.6'/>", t0, t1=t1)
flash = lambda x, y, t0, r=40: svg(f"<circle cx='{x}' cy='{y}' r='{r}' fill='#fff6d0' filter='url(#glow)'/><circle cx='{x}' cy='{y}' r='{r*2.2}' fill='#f5a623' opacity='.35' filter='url(#glow)'/>", t0, layer="overlay")
S.shot(0, {"depth":.85,"rays":False,"spotlight":{"x":960,"w":300}}, [flash(960, 470, .1, 60), cap("ALMOST AS HOT", 790, .4, 46), cap("AS THE *SUN*?", 855, 1.2, 60)], fadeIn=.2)
s = cuts[1]
S.shot(1, {"depth":.35,"seabed":"dark","seabedY":820}, [shrimp(930, 600, 1.15), cap("PISTOL SHRIMP", 230, .2, 50),
   {"type":"pill","text":"About finger-sized","x":790,"y":285,"size":26,"t0":1.6},
   {"type":"circle","x":1100,"y":600,"rx":130,"ry":70,"t0":T["claw"]-s+.4}, cap("IT DOESN'T PINCH.", 900, T["claw"]-s+1.6, 38), cap("IT *SNAPS*.", 960, T["claw"]-s+2.6, 52)])
s = cuts[2]
jetl = "".join(f"<line x1='{1010+i*28}' y1='{560+(i%2)*14}' x2='{1070+i*28}' y2='{560+(i%2)*14}' stroke='#cfefff' stroke-width='5' opacity='{.9-i*.12}'/>" for i in range(6))
S.shot(2, {"depth":.4,"seabed":"dark","seabedY":820}, [shrimp(780, 560, .85, open_=False), svg(jetl, 1.0, layer="overlay"),
   cap("WATER JET", 220, .3, 48), cap("*~100 KM/H*", 290, 1.6, 64),
   bubble(1170, 560, 42, T["low"]-s+1.8), cap("PRESSURE DROPS →", 860, T["low"]-s+.6, 36), cap("A *BUBBLE* OPENS", 915, T["low"]-s+2.0, 44)], camera={"zoomFrom":1,"zoomTo":1.08,"x":960})
s = cuts[3]
S.shot(3, {"depth":.5}, [bubble(960, 520, 160, 0, t1=T["bang"]-s+1.3), bubble(960, 520, 60, T["bang"]-s+1.3, t1=T["bang"]-s+1.6),
   {"type":"reticle","x":960,"y":520,"r":220,"t0":T["bang"]-s+1.6}, cap("*BANG.*", 820, T["bang"]-s+1.6, 96),
   cap("LOUD ENOUGH TO", 215, T["loud"]-s+.3, 40), cap("*STUN* PREY", 275, T["loud"]-s+3.6, 52)])
s = cuts[4]
S.shot(4, {"mode":"black"}, [cap("*2001*: HIGH-SPEED CAMERAS", 215, .2, 36), bubble(960, 540, 90, .5, t1=T["flash"]-s+.8),
   flash(960, 540, T["flash"]-s+.8, 30), cap("A FLASH OF *LIGHT*", 860, T["flash"]-s+1.4, 48)])
s = cuts[5]
S.shot(5, {"mode":"paper"}, [cap("LIGHT = *HEAT*", 200, .2, 52),
   {"type":"factstack","x":720,"y":360,"w":480,"gap":110,"size":30,"items":[
     {"text":"Bubble: 5,000+ K","t0":2.0,"tone":"red"},{"text":"Sun's surface: ~6,000 K","t0":T["sun"]-s+.8}]}])
s = cuts[6]
S.shot(6, {"mode":"black"}, [flash(960, 520, .1, 45), cap("“SHRIMPO-", 800, .5, 56), cap("*LUMINESCENCE*”", 870, .9, 56)])
s = cuts[7]
S.shot(7, {"mode":"paper"}, [{"type":"doccard","x":960,"y":520,"w":470,"h":600,"header":"Case #007","title":"The pistol\nshrimp","footer":"Nature, 2001"},
   {"type":"stamp","text":"True","x":960,"y":640,"size":84,"color":"#3ecf6a","t0":T["verdict"]-s+.6},
   cap("FOR A *SPLIT SECOND*", 920, T["verdict"]-s+2.0, 36)])
s = cuts[8]
S.shot(8, {"depth":.35,"seabed":"dark","seabedY":820}, [shrimp(930, 620, .9), cap("HEAR *CRACKLING*", 215, .3, 46), cap("ON A REEF?", 275, 1.0, 46),
   cap("THAT'S *THEM*", 900, 2.4, 52)], fadeOut=.5)
S.save({"style":"thriller","end":END,"pulse_from":c("jet"),"hits":[.12,T["bang"]+1.6],
 "pings":[T["flash"]+.8,T["name"]+.1],"riser":[T["sun"],T["verdict"]+.1],"impact":T["verdict"]+.6,
 "whoosh":[1.2,T["what"]+1.6,T["claw"]+2.6,T["jet"]+1.6,T["low"]+2.0,T["loud"]+3.6,T["saw"]+.2,T["flash"]+1.4,T["heat"]+2.0,T["sun"]+.8,T["verdict"]+2.0,T["cta"]+2.4]})
