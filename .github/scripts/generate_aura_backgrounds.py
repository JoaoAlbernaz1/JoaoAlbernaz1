"""Generate stable, atmospheric backgrounds for readme-aura components.

No external assets. Output PNGs are embedded by readme-aura into the final
SVGs; generated source PNGs do not need to be committed.
"""
from pathlib import Path
from math import exp
from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "assets" / "aura-backgrounds"
OUT.mkdir(parents=True, exist_ok=True)

# Each background has a black/navy base and four diffused, subdued light sources.
SCENES = {
    "hero": (860, 329, [
        ((.10,.89),(.46,.58),(57,175,125),.77),
        ((.91,.04),(.46,.65),(206,66,99),.66),
        ((.72,.98),(.37,.54),(133,91,205),.65),
        ((.12,.02),(.43,.55),(75,102,177),.40),
    ]),
    "about": (574, 250, [
        ((.85,.17),(.55,.79),(175,58,81),.65),
        ((.09,.93),(.48,.67),(65,146,135),.52),
        ((.78,.96),(.44,.55),(129,76,144),.37),
    ]),
    "stack": (860, 216, [
        ((.12,.93),(.49,.81),(64,154,120),.65),
        ((.91,.17),(.55,.73),(177,68,102),.59),
        ((.71,.95),(.49,.59),(102,86,181),.56),
    ]),
    "stats": (860, 217, [
        ((.13,.89),(.53,.89),(61,111,160),.59),
        ((.91,.08),(.45,.88),(126,80,178),.60),
        ((.53,.97),(.51,.85),(55,128,123),.29),
    ]),
}
BASE=(9,12,19)
for name,(w,h,lights) in SCENES.items():
    im=Image.new("RGB",(w,h))
    pixels=[]
    for y in range(h):
        fy=y/max(h-1,1)
        for x in range(w):
            fx=x/max(w-1,1)
            rgb=[float(c) for c in BASE]
            for (px,py),(sx,sy),color,power in lights:
                q=((fx-px)/sx)**2+((fy-py)/sy)**2
                gain=power*exp(-1.8*q)
                for c in range(3):
                    rgb[c]+=max(0,color[c]-BASE[c])*gain
            # Subtle center vignette and deterministic dither to suppress banding.
            vig=1-.13*((fx-.5)**2+ (fy-.5)**2)
            noise=((x*17+y*23)%7-3)*.34
            pixels.append(tuple(max(0,min(255,int(v*vig+noise))) for v in rgb))
    im.putdata(pixels)
    target=OUT/f"{name}.png"
    im.save(target,optimize=True)
    print(name,target.stat().st_size)
