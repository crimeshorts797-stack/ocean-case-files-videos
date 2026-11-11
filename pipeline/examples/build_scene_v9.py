import sys; sys.path.insert(0, "/home/claude/pipeline")
from scenelib import *
T = load("v9"); c = lambda k, d=.2: T[k]-d
cuts = [0, c("name"), c("most"), c("stress"), c("lab"), c("catch"), c("full"), c("verdict",.25), c("genes"), END]
S = Scene("v9", "CASE #006", cuts)
S.shot(0, {"depth":.85,"rays":False,"spotlight":{"x":960,"w":260}}, [jelly(960, 480, 2.2, glow=True),
   cap("THE *IMMORTAL*", 820, .3, 52), cap("JELLYFISH?", 885, 1.1, 52)], fadeIn=.3, camera={"zoomFrom":1.1,"zoomTo":1})
s = cuts[1]
S.shot(1, {"depth":.4}, [jelly(960, 470, 1.4), cap("TURRITOPSIS DOHRNII", 215, .2, 36, caps=True),
   {"type":"bracket","x1":880,"y1":700,"x2":1040,"y2":700,"label":"~4.5 mm","t0":1.6}, cap("SMALLER THAN A *FINGERNAIL*", 880, T["name"]-s+2.4, 34)])
s = cuts[2]
S.shot(2, {"mode":"paper"}, [cap("A NORMAL JELLYFISH:", 215, .2, 40),
   {"type":"factstack","x":740,"y":400,"w":440,"gap":90,"size":26,"items":[{"text":"Grow up","t0":.8},{"text":"Reproduce","t0":1.6},{"text":"Die","t0":2.4,"tone":"red"}]},
   cap("THIS ONE: *REWIND*", 820, T["rew"]-s+.2, 50)])
s = cuts[3]
S.shot(3, {"depth":.55,"seabed":"sand","seabedY":880}, [jelly(960, 380, 1.2, t1=T["stress"]-s+3.0),
   polyp(960, 860, 1.4, t0=T["stress"]-s+3.4), cap("STRESSED? INJURED?", 215, .2, 40),
   cap("BACK TO A *POLYP*", 420, T["stress"]-s+4.0, 46), cap("THEN IT GROWS UP *AGAIN*", 480, T["again"]-s+.2, 34)])
s = cuts[4]
arrows = "<path d='M800,560 C800,380 1120,380 1120,560' fill='none' stroke='#f5a623' stroke-width='6' marker-end=''/><path d='M1120,640 C1120,820 800,820 800,640' fill='none' stroke='#f5a623' stroke-width='6'/><polygon points='1120,575 1105,545 1135,545' fill='#f5a623'/><polygon points='800,625 785,655 815,655' fill='#f5a623'/>"
S.shot(4, {"depth":.5}, [svg(arrows, .4, layer="overlay"), jelly(800, 560, .7), polyp(1120, 650, .7),
   cap("AGAIN AND *AGAIN*", 215, .5, 46), cap("NO DEATH BY *OLD AGE*", 900, T["old"]-s+.2, 40)])
s = cuts[5]
S.shot(5, {"depth":.45}, [jelly(1000, 430, 1.0, t1=T["eaten"]-s+2.5), cap("THE *CATCH*", 215, .1, 56),
   {"type":"creature","kind":"fish","x":700,"y":470,"scale":.9,"swim":{"vx":90},"t0":T["eaten"]-s+.8},
   {"type":"factstack","x":740,"y":680,"w":440,"gap":84,"size":24,"items":[{"text":"Eaten by fish","t0":T["eaten"]-s+.8,"tone":"red"},{"text":"Sea turtles","t0":T["eaten"]-s+1.7,"tone":"red"},{"text":"Disease","t0":T["eaten"]-s+4.2,"tone":"red"}]}])
s = cuts[6]
S.shot(6, {"depth":.4}, [cap("IF TRULY IMMORTAL…", 215, .2, 40), cap("THE OCEAN WOULD BE", 275, 2.6, 34), cap("*FULL OF THEM*", 330, 3.6, 46),
   *[jelly(700+(i%5)*130, 520+(i//5)*150, .45, t0=3.6+i*.06) for i in range(15)]])
s = cuts[7]
S.shot(7, {"mode":"paper"}, [{"type":"doccard","x":960,"y":520,"w":470,"h":600,"header":"Case #006","title":"Immortal\njellyfish","footer":"Turritopsis dohrnii"},
   {"type":"stamp","text":"Half true","x":960,"y":640,"size":66,"color":"#f5a623","t0":T["verdict"]-s+.6},
   cap("BEATS *OLD AGE*. NOT EVERYTHING.", 920, T["verdict"]-s+2.0, 30)])
s = cuts[8]
S.shot(8, {"depth":.8,"rays":False}, [jelly(960, 470, 1.6, glow=True), cap("A KEY TO *AGING*?", 215, .3, 46),
   cap("SHOULD WE BE *JEALOUS*?", 860, T["cta"]-s+.1, 40), {"type":"pill","text":"Follow for the next case","x":752,"y":930,"size":24,"t0":T["cta"]-s+1.4}], fadeOut=.6)
S.save({"style":"melancholy","end":END,"impact":T["verdict"]+.6,"hits":[T["catch"]],
 "pings":[T["rew"]+.2,T["stress"]+3.4,T["full"]+3.6],
 "whoosh":[1.1,T["name"]+2.4,T["most"]+.8,T["most"]+1.6,T["most"]+2.4,T["stress"]+4.0,T["lab"]+.5,T["old"]+.2,T["eaten"]+.8,T["eaten"]+1.7,T["eaten"]+4.2,T["verdict"]+2.0,T["cta"]+.1]})
