#!/usr/bin/env python3
"""Trojan Cycle consolidated builder v2 — narration as page bands, balloons in-art (face-safe), smaller type."""
from PIL import Image, ImageDraw, ImageFont, ImageOps
import os
ROOT="/home/claude/tc/trojan-cycle"; ART=f"{ROOT}/issues/issue-01/art"; BUILD=f"{ROOT}/build"
os.makedirs(BUILD, exist_ok=True)
CB=f"{ROOT}/fonts/ComicNeue-Bold.ttf"; CI=f"{ROOT}/fonts/ComicNeue-BoldItalic.ttf"; BG=f"{ROOT}/fonts/Bangers-Regular.ttf"
CREAM=(250,238,196); PAPER=(245,236,216); INK=(20,16,12)
PW,PH,M,G=2000,2800,70,26
CW=PW-2*M

def wrap(d,t,f,mw):
    ws,ls,c=t.split(),[],""
    for w in ws:
        s=(c+" "+w).strip()
        if d.textlength(s,font=f)<=mw: c=s
        else: ls.append(c); c=w
    ls.append(c); return ls

def balloon(img,text,cx,cy,bw,tail=None,size=30,heart=False):
    d=ImageDraw.Draw(img); f=ImageFont.truetype(CI if heart else CB,size)
    pad,lead=int(size*0.75),int(size*1.2)
    ls=wrap(d,text.upper(),f,bw-2*pad)
    tw=max(d.textlength(l,font=f) for l in ls)
    w=min(bw,int(tw)+2*pad); h=2*pad+lead*len(ls)
    x,y=int(cx-w//2),int(cy-h//2)
    d.rounded_rectangle([x,y,x+w,y+h],radius=int(h*0.35),fill="white",outline=INK,width=4)
    if tail:
        tx,ty=tail; bx=min(max(cx,x+34),x+w-34); by=y+h-3 if ty>cy else y+3
        d.polygon([(bx-16,by),(bx+16,by),(tx,ty)],fill="white")
        d.line([(bx-16,by),(tx,ty)],fill=INK,width=4); d.line([(bx+16,by),(tx,ty)],fill=INK,width=4)
    ty0=y+pad
    for l in ls:
        lw=d.textlength(l,font=f); d.text((x+(w-lw)//2,ty0),l,font=f,fill=INK); ty0+=lead

def cap_art(img,text,x,y,bw,size=28,anchor="lt"):
    d=ImageDraw.Draw(img); f=ImageFont.truetype(CB,size)
    pad,lead=int(size*0.5),int(size*1.2)
    ls=wrap(d,text.upper(),f,bw-2*pad)
    h=2*pad+lead*len(ls)
    if anchor=="lb": y=y-h
    if anchor=="rb": x=x-bw; y=y-h
    if anchor=="rt": x=x-bw
    d.rectangle([x+5,y+5,x+bw+5,y+h+5],fill=(0,0,0))
    d.rectangle([x,y,x+bw,y+h],fill=CREAM,outline=INK,width=4)
    ty=y+pad
    for l in ls:
        d.text((x+pad,ty),l,font=f,fill=INK); ty+=lead

class Page:
    def __init__(self):
        self.im=Image.new("RGB",(PW,PH),PAPER); self.d=ImageDraw.Draw(self.im)
    def band(self,text,y,size=30,ornate=False,maxw=1760):
        f=ImageFont.truetype(CB,size)
        ls=wrap(self.d,text.upper(),f,maxw)
        lead=int(size*1.25); pad=22
        bw=max(self.d.textlength(l,font=f) for l in ls)+2*pad+16
        bh=2*pad+lead*len(ls)
        bx=(PW-bw)//2
        self.d.rectangle([bx+6,y+6,bx+bw+6,y+bh+6],fill=(0,0,0))
        self.d.rectangle([bx,y,bx+bw,y+bh],fill=CREAM,outline=INK,width=4)
        if ornate: self.d.rectangle([bx+8,y+8,bx+bw-8,y+bh-8],outline=(150,40,30),width=3)
        ty=y+pad
        for l in ls:
            lw=self.d.textlength(l,font=f); self.d.text((bx+(bw-lw)//2,ty),l,font=f,fill=INK); ty+=lead
        return bh
    def band_h(self,text,size=30,maxw=1760):
        f=ImageFont.truetype(CB,size)
        return 2*22+int(size*1.25)*len(wrap(self.d,text.upper(),f,maxw))
    def paste(self,im,x,y,w,h):
        self.im.paste(im.resize((int(w),int(h)),Image.LANCZOS),(int(x),int(y)))
        self.d.rectangle([x,y,x+w,y+h],outline=INK,width=6)
    def foot(self,text,y,right=M+CW):
        f=ImageFont.truetype(CI,22); tw=self.d.textlength(text,font=f)
        self.d.text((right-tw,y),text,font=f,fill=(90,70,50))
    def num(self,n):
        f=ImageFont.truetype(CB,28); self.d.text((PW//2-12,PH-50),str(n),font=f,fill=INK)
    def save(self,n):
        self.im.save(f"{BUILD}/page-{n:03d}.png")

A=lambda n: Image.open(f"{ART}/{n}").convert("RGB")

# ================= PAGE 1 — COVER =================
cov=A("i01-pg01-pn1.png"); d=ImageDraw.Draw(cov)
t1="THE TROJAN CYCLE"; f1=ImageFont.truetype(BG,110)
w1=d.textlength(t1,font=f1); d.text(((cov.width-w1)/2,30),t1,font=f1,fill=(255,202,62),stroke_width=7,stroke_fill=(96,24,12))
t2="1 \u00b7 THE BURDEN OF THE EARTH"; f2=ImageFont.truetype(BG,52)
w2=d.textlength(t2,font=f2); d.text(((cov.width-w2)/2,168),t2,font=f2,fill=(250,238,196),stroke_width=4,stroke_fill=(20,16,12))
pg=Page(); ch=PH-80; cwd=int(ch*cov.width/cov.height)
pg.paste(cov,(PW-cwd)//2,40,cwd,ch); pg.save(1)

# ================= PAGE 2 =================
pg=Page()
b1="Miletus, on the coast of Asia. Ten generations have passed since the age of heroes ended. In the hall of its princes \u2014 descendants of Nestor of Pylos \u2014 a singer has been summoned."
p1=A("i01-pg02-pn1.png"); p2=A("i01-pg02-pn2.png"); p3=A("i01-pg02-pn3.png")
h_b=pg.band_h(b1); h1=980; h2=830; h3=520
total=h_b+18+h1+G+h2+G+h3; y=(PH-total)//2
pg.band(b1,y); y+=h_b+18
p1c=p1.crop((0,60,1672,60+int(1672*h1/CW))); pg.paste(p1c,M,y,CW,h1); y+=h1+G
sc=CW/1448; p2s=p2.resize((CW,int(1086*sc)),Image.LANCZOS); p2c=p2s.crop((0,230,CW,230+h2))
balloon(p2c,"Sing for us, old father. Sing the great song \u2014 our fathers' fathers, and the war at Troy.",860,175,700,tail=(1330,150),size=34)
pg.paste(p2c,M,y,CW,h2); y+=h2+G
strip=p3.crop((0,250,1448,790))
balloon(strip,"The great song is long, my lords. It does not begin at Troy.",1140,110,470,tail=(880,320),size=26)
balloon(strip,"It begins before Helen \u2014 before the heroes. It begins with the groaning of the Earth.",1140,400,480,size=26)
pg.paste(strip,M,y,CW,h3)
pg.num(2); pg.save(2)

# ================= PAGE 3 =================
pg=Page()
p1=A("i01-pg03-pn1.png"); p2=A("i01-pg03-pn2.png"); p3=A("i01-pg03-pn3.png")
sep=ImageOps.colorize(ImageOps.grayscale(p2),black=(30,20,12),white=(238,214,170)).convert("RGB")
mask=Image.new("L",p2.size,120); md=ImageDraw.Draw(mask)
for i in range(40,-1,-1):
    r=int(1250*i/40); md.ellipse([600-r,400-r,600+r,400+r],fill=int(120*i/40))
p2g=Image.composite(sep,p2,mask)
balloon(p1,"Muse, goddess of memory, sing through me \u2014",790,150,520,tail=(430,400),size=30)
balloon(p2g,"\u2014 sing of the great wrath, of the long wanderings, of the burning of holy Wilios*, and of the hard roads home.",265,220,440,tail=(370,470),size=27)
balloon(p2g,"Begin where the gods began it.",250,1360,360,tail=(390,1100),size=27)
H1=1240; w1=int(H1*p1.width/p1.height); w2=int(H1*p2g.width/p2g.height)
bandt="HEAR THEN, AS THE MUSE GIVES IT: HOW THE PLAN OF ZEUS WAS SET IN MOTION."
h3=int(CW*p3.height/p3.width); bh=pg.band_h(bandt)
total=H1+40+bh+18+h3; y=(PH-total)//2; x0=(PW-(w1+G+w2))//2
pg.paste(p1,x0,y,w1,H1); pg.paste(p2g,x0+w1+G,y,w2,H1)
pg.foot("*WILIOS, OR ILIOS \u2014 THE CITY ALSO CALLED TROY; WILUSA IN THE TREATIES OF THE HATTI.",y+H1+8,x0+w1+G+w2)
y+=H1+40; pg.band(bandt,y,ornate=True); y+=bh+18
pg.paste(p3,M,y,CW,h3); pg.num(3); pg.save(3)

# ================= PAGE 4 =================
pg=Page()
p1=A("i01-pg04-pn1.png"); p2=A("i01-pg04-pn2.png"); p3=A("i01-pg04-pn3.png")
balloon(p3,"Zeus! Hear me! I am the Earth, mother of all living things!",512,105,600,tail=(500,300),size=32)
b1="In those days the generations of men had grown past all counting. Their kings warred, their cities multiplied, their weight lay heavy on the world."
b2="And the Earth herself \u2014 mother of all living things \u2014 grew weary."
h1=int(CW*p1.height/p1.width); H2=912; bh1=pg.band_h(b1); bh2=pg.band_h(b2)
total=bh1+18+h1+24+bh2+18+H2*0.75+0
w2c=int(H2*0.75*4/3); w3=int(H2*0.75*2/3)
rowh=int(H2*0.75)
total=bh1+18+h1+24+bh2+18+rowh
y=(PH-total)//2
pg.band(b1,y); y+=bh1+18
pg.paste(p1,M,y,CW,h1); y+=h1+24
pg.band(b2,y); y+=bh2+18
xr=(PW-(w2c+G+w3))//2
pg.paste(p2,xr,y,w2c,rowh); pg.paste(p3,xr+w2c+G,y,w3,rowh)
pg.num(4); pg.save(4)

# ================= PAGE 5 =================
pg=Page()
p1=A("i01-pg05-pn1.png"); p2=A("i01-pg05-pn2.png"); p3=A("i01-pg05-pn3.png")
balloon(p1,"The multitude of men is more than I can bear. Their cities crowd my plains; their wars tear my body; there is no rest left in me.",860,170,520,tail=(1200,210),size=27)
strip=p2.crop((0,120,1448,711))
balloon(strip,"I do not ask for their destruction \u2014 they are my children. I ask for relief.",290,130,460,tail=(620,350),size=26)
balloon(strip,"Lighten my burden, Zeus, or I will break beneath it.",1170,120,440,tail=(830,340),size=26)
p3c=p3.crop((0,0,1448,638))
b3="And Zeus was silent, weighing the fate of an age in his heart."
h1=int(CW*p1.height/p1.width); h2=730; h3=800; bh=pg.band_h(b3)
total=h1+G+h2+G+h3+16+bh; y=(PH-total)//2
pg.paste(p1,M,y,CW,h1); y+=h1+G
pg.paste(strip,M,y,CW,h2); y+=h2+G
pg.paste(p3c,M,y,CW,h3); y+=h3+16
pg.band(b3,y); pg.num(5); pg.save(5)

# ================= PAGE 6 =================
pg=Page()
p1=A("i01-pg06-pn1.png").crop((0,50,1448,836)); p2=A("i01-pg06-pn2.png"); p3=A("i01-pg06-pn3.png")
balloon(p2,"Once before, when mankind grew past all bearing, we sent the great flood. Not again \u2014 a flood is waste, and it teaches nothing.",300,210,500,tail=(620,300),size=38)
balloon(p2,"Let it be a war. Let the age of heroes end as it has lived \u2014 in glory.",300,620,470,tail=(630,340),size=38)
balloon(p3,"Then I will begin it with a quarrel among goddesses \u2014 and a judgment by a mortal man \u2014 and a woman so beautiful that every king will swear an oath for her sake.",1160,240,500,tail=(860,540),size=38)
balloon(p3,"And at Ilios, by the Hellespont, the finest of the heroes will fall \u2014 until Earth's burden is eased, and their names pass into song.",1160,700,500,tail=(870,560),size=38)
b1="Then Zeus took counsel \u2014 not with his queen, nor with the gods at feast, but with Themis, the goddess of Right Order."
bh=pg.band_h(b1); h1=int(CW*p1.height/p1.width); H2=684
total=bh+18+h1+G+H2; y=(PH-total)//2
pg.band(b1,y); y+=bh+18
pg.paste(p1,M,y,CW,h1); y+=h1+G
pg.paste(p2,M,y,912,H2); pg.paste(p3,M+912+36,y,912,H2)
pg.num(6); pg.save(6)

# ================= PAGE 7 =================
pg=Page()
p1=A("i01-pg07-pn1.png"); p2=A("i01-pg07-pn2.png"); p3=A("i01-pg07-pn3.png")
balloon(p2,"Let it begin far from Troy, and years before it \u2014 in the two royal houses that will one day fight the war.",740,150,620,tail=(420,320),size=38)
balloon(p3,"Now hear, princes, of the two old crimes from which your fathers' war grew. One was done at a table. One was done upon a wall.",430,190,600,tail=(320,400),size=38)
b1="So the plan was made: death for the heroes, and undying glory with it. For the plan of Zeus does not strike like the thunderbolt \u2014 it grows slowly, like an oak, from old seed planted in dark ground."
h1=int(CW*p1.height/p1.width); bh=pg.band_h(b1); H2=684
total=h1+16+bh+18+H2; y=(PH-total)//2
pg.paste(p1,M,y,CW,h1); y+=h1+16
pg.band(b1,y); y+=bh+18
pg.paste(p2,M,y,912,H2); pg.paste(p3,M+912+36,y,912,H2)
pg.num(7); pg.save(7)

# ================= PAGE 8 (splash, plates in page space) =================
pg=Page()
s=A("i01-pg08-pn1.png")
ch=PH-80; cwd=int(ch*s.width/s.height); x0=(PW-cwd)//2
pg.paste(s,x0,40,cwd,ch)
cap_art(pg.im,"In the west: the house of Tantalus \u2014 whom the gods loved too well.",x0+26,66,520,26)
cap_art(pg.im,"In the east: the house of Laomedon \u2014 who cheated the gods of their wage.",x0+26,PH-66,540,26,anchor="lb")
# center ornamented plate in the open sky (right-middle of splash)
f0=ImageFont.truetype(CB,26)
lines=wrap(pg.d,"TWO DEBTS OWED TO THE GODS. ONE RECKONING TO COME. FROM THESE ROOTS THE WAR WILL GROW.",f0,360)
lead=34; pad=20
bw=max(pg.d.textlength(l,font=f0) for l in lines)+2*pad; bh=2*pad+lead*len(lines)
bx=x0+int(cwd*0.775)-int(bw//2); by=int(40+ch*0.385)-bh//2
pg.d.rectangle([bx+5,by+5,bx+bw+5,by+bh+5],fill=(0,0,0))
pg.d.rectangle([bx,by,bx+bw,by+bh],fill=CREAM,outline=INK,width=4)
pg.d.rectangle([bx+7,by+7,bx+bw-7,by+bh-7],outline=(150,40,30),width=3)
ty=by+pad
for l in lines:
    lw=pg.d.textlength(l,font=f0); pg.d.text((bx+(bw-lw)//2,ty),l,font=f0,fill=INK); ty+=lead
pg.save(8)

# ================= PAGE 9 =================
pg=Page()
p1=A("i01-pg09-pn1.png"); p2=A("i01-pg09-pn2.png"); p3=A("i01-pg09-pn3.png")
balloon(p2,"What are secrets among friends?",1060,890,480,tail=(760,650),size=36,heart=True)
b1="No mortal was ever raised so high as Tantalus, king under Mount Sipylos. He sat at the gods' own table; nectar and ambrosia* passed his lips."
b2="But the gods' favor made him insolent. He stole the food of the gods for his friends on earth \u2014 and worse, he repeated the gods' secret counsels to mortal men, to make himself great."
h1=int(CW*p1.height/p1.width); bh1=pg.band_h(b1); bh2=pg.band_h(b2); H2=684
total=bh1+16+28+h1+22+bh2+18+H2; y=(PH-total)//2
pg.band(b1,y); pg.foot("*NECTAR AND AMBROSIA \u2014 THE DRINK AND FOOD OF THE GODS, WHICH KEEP THEM DEATHLESS.",y+bh1+6); y+=bh1+16+28
pg.paste(p1,M,y,CW,h1); y+=h1+22
pg.band(b2,y); y+=bh2+18
pg.paste(p2,M,y,912,H2); pg.paste(p3,M+912+36,y,912,H2)
pg.num(9); pg.save(9)

# ================= PAGE 10 =================
pg=Page()
p1=A("i01-pg10-pn1.png"); p2=A("i01-pg10-pn2.png"); p3=A("i01-pg10-pn3.png")
balloon(p2,"Abomination! Did you dream we would not know?",330,140,520,tail=(760,300),size=38)
balloon(p2,"Restore the boy! And for you, Tantalus \u2014 a table is prepared in the world below!",330,1000,520,tail=(500,700),size=38)
b1="Tantalus had stolen from the gods and betrayed their secrets \u2014 and gone unpunished. So his pride grew, until he believed the deathless gods could be deceived by a mortal's cunning."
b2="To test them, he did a deed the singer will name only once: he slew his own son, Pelops, and set the flesh before his guests as a feast \u2014 to see if they would know."
b3="The gods knew at once, and no dish was touched \u2014 save by one goddess, deep in mourning for a lost daughter, who tasted before she saw. The gods restored the boy whole and living. Only that one shoulder could not be made again \u2014 and in its place the Fates set gleaming ivory, the mark of his father's sin, carried all his days."
h1=int(CW*p1.height/p1.width); bh1=pg.band_h(b1); bh2=pg.band_h(b2); bh3=pg.band_h(b3); H2=620
total=bh1+14+bh2+18+h1+G+H2+16+bh3; y=(PH-total)//2
pg.band(b1,y); y+=bh1+14
pg.band(b2,y); y+=bh2+18
pg.paste(p1,M,y,CW,h1); y+=h1+G
w2=int(H2*4/3); w3=w2; xr=(PW-(w2+G+w3))//2
pg.paste(p2,xr,y,w2,H2); pg.paste(p3,xr+w2+G,y,w3,H2); y+=H2+16
pg.band(b3,y); pg.num(10); pg.save(10)

# ================= PAGE 11 =================
pg=Page()
p1=A("i01-pg11-pn1.png"); p2=A("i01-pg11-pn2.png"); p3=A("i01-pg11-pn3.png")
cap_art(p2,"Food and drink forever before him \u2014 and forever beyond his reach.",p2.width-30,p2.height-26,600,30,anchor="rb")
balloon(p3,"So ends the first debt, princes. Now for the son, Pelops \u2014 and the chariot-race that won a kingdom and a curse.",600,150,640,tail=(300,380),size=38)
b1="And in the house of Hades, Tantalus stands forever in the pool. He stoops to drink: the water flees into black earth. He reaches for the boughs: the wind tosses them to the clouds."
bh=pg.band_h(b1); L,R=864,960; H=1296
total=bh+18+H; y=(PH-total)//2
pg.band(b1,y); y+=bh+18
x0=(PW-(L+36+R))//2
pg.paste(p1,x0,y,L,H)
h2=int(R*p2.height/p2.width); pg.paste(p2,x0+L+36,y,R,h2)
h3=H-h2-36; p3c=p3.crop((0,0,1448,int(1448*h3/R)))
pg.paste(p3c,x0+L+36,y+h2+36,R,h3)
pg.num(11); pg.save(11)

# ================= PAGE 12 =================
pg=Page()
p1=A("i01-pg12-pn1.png"); p2=A("i01-pg12-pn2.png"); p3=A("i01-pg12-pn3.png")
balloon(p3,"Not this one too. O gods, not this one too.",1300,130,480,tail=(1010,250),size=26,heart=True)
b1="The boy grew into the fairest of men, and Poseidon*, who had loved him, gave him at parting a chariot swift as storm. With it Pelops crossed the sea to woo Hippodamia, daughter of King Oenomaus of Pisa."
b2="Thirteen suitors had come before him; their heads were set on stakes before the gate. For an oracle had told the king he would die by his daughter's husband \u2014 so he raced each suitor to the Isthmus, and speared each one from behind."
bh1=pg.band_h(b1); bh2=pg.band_h(b2)
r1=830; r2=700; r3=800
total=bh1+16+28+r1+22+bh2+18+r2+G+r3; y=(PH-total)//2
pg.band(b1,y); pg.foot("*POSEIDON \u2014 GOD OF THE SEA, OF HORSES, AND OF EARTHQUAKES.",y+bh1+6); y+=bh1+16+28
p1c=p1.crop((0,0,1672,int(1672*r1/CW))); pg.paste(p1c,M,y,CW,r1); y+=r1+22
pg.band(b2,y); y+=bh2+18
p2c=p2.crop((0,20,1448,20+int(1448*r2/CW))); pg.paste(p2c,M,y,CW,r2); y+=r2+G
p3c=p3.crop((0,0,1672,int(1672*r3/CW))); pg.paste(p3c,M,y,CW,r3)
pg.num(12); pg.save(12)

# ================= PAGE 13 =================
pg=Page()
p1=A("i01-pg13-pn1.png"); p2=A("i01-pg13-pn2.png"); p3=A("i01-pg13-pn3.png")
balloon(p2,"Take out the bronze pins from the king's wheels and set wax pins in their place. When I am king of Pisa, half the kingdom is yours \u2014 I swear it before Zeus, who hears all oaths.",370,660,560,tail=(600,320),size=34)
balloon(p2,"Before Zeus, then, prince. Half the kingdom. The god has heard you \u2014 and so have I.",1120,880,480,tail=(980,540),size=34)
cap_art(p3,"So the race was sold before it was run.",p3.width-30,p3.height-26,520,26,anchor="rb")
b1="But Hippodamia went by night to Myrtilus the charioteer, her father's servant, son of Hermes* \u2014 the only man whose hands touched the king's axles."
bh=pg.band_h(b1); H2=760; h3=int(CW*p3.height/p3.width)
total=bh+16+28+H2+G+h3; y=(PH-total)//2
pg.band(b1,y); pg.foot("*HERMES \u2014 GOD OF ROADS, HERALDS, AND CUNNING; FATHER OF MYRTILUS.",y+bh+6); y+=bh+16+28
w12=int(H2*4/3); xr=(PW-(w12*2+G))//2
pg.paste(p1,xr,y,w12,H2); pg.paste(p2,xr+w12+G,y,w12,H2); y+=H2+G
pg.paste(p3,M,y,CW,h3); pg.num(13); pg.save(13)

# ================= PAGE 14 =================
pg=Page()
p1=A("i01-pg14-pn1.png"); p2=A("i01-pg14-pn2.png"); p3=A("i01-pg14-pn3.png").crop((0,0,1448,920))
balloon(p1,"Faster, Myrtilus! This stranger's head will make it fourteen!",380,640,500,tail=(320,430),size=26)
balloon(p3,"Treachery... in my own house... Hear me, gods below \u2014 let Myrtilus die by the hand of the man he served today!",740,160,560,tail=(620,410),size=32)
b1="They raced for the altar of Poseidon at the Isthmus \u2014 the bride riding in the suitor's chariot, her father hunting behind with his spear, as he had twelve times before."
b2="And with the curse on his lips, the king of Pisa died."
bh1=pg.band_h(b1); bh2=pg.band_h(b2)
r1=r2=830
h3=PH-140-bh1-18-r1-24-r2-24-16-bh2
w3=int(h3*1448/920)
total=bh1+18+r1+24+r2+24+h3+16+bh2; y=(PH-total)//2
pg.band(b1,y); y+=bh1+18
p1c=p1.crop((0,0,1672,int(1672*r1/CW))); pg.paste(p1c,M,y,CW,r1); y+=r1+24
p2c=p2.crop((0,30,1672,30+int(1672*r2/CW))); pg.paste(p2c,M,y,CW,r2); y+=r2+24
pg.paste(p3,(PW-w3)//2,y,w3,h3); y+=h3+16
pg.band(b2,y); pg.num(14); pg.save(14)

# ================= PAGE 15 =================
pg=Page()
p1=A("i01-pg15-pn1.png"); p2=A("i01-pg15-pn2.png"); p3=A("i01-pg15-pn3.png")
r1=800
p1c=p1.crop((0,60,1448,60+int(1448*r1/CW)))
balloon(p1c,"My half of the kingdom, son of Tantalus. Pay me. You swore it before Zeus.",1080,105,460,tail=(880,260),size=24)
balloon(p1c,"I will not share my kingdom with the man whose treachery won it. You know too much, charioteer.",380,580,480,tail=(430,220),size=24)
cap_art(p2,"Pelops seized him and threw him from the cliff, to bury the secret of how he had won his kingdom.",26,26,450,26)
balloon(p2,"Zeus heard your oath, Pelops \u2014 now let him hear my curse! As you have betrayed me, let your own family betray one another!",255,470,430,tail=(430,390),size=30)
balloon(p2,"Let your children kill their own blood, and serve one another such feasts, until the gods grow sick of the house of Pelops!",512,1340,580,tail=(540,780),size=30)
b1="Myrtilus had done his part, and came to the new king for the payment sworn before Zeus. But Pelops had no intention of paying."
bh=pg.band_h(b1)
h_r2=1080; w2=int(h_r2*1024/1536); w3=CW-36-w2; h3=int(w3*p3.height/p3.width)
total=bh+18+r1+24+h_r2; y=(PH-total)//2
pg.band(b1,y); y+=bh+18
pg.paste(p1c,M,y,CW,r1); y+=r1+24
pg.paste(p2,M,y,w2,h_r2)
pg.paste(p3,M+w2+36,y,w3,h3)
# closing captions as paper plates under pn3
def plate(text,x,y0,bw):
    f=ImageFont.truetype(CB,28); pad,lead=18,36
    ls=wrap(pg.d,text.upper(),f,bw-2*pad); h=2*pad+lead*len(ls)
    pg.d.rectangle([x+5,y0+5,x+bw+5,y0+h+5],fill=(0,0,0))
    pg.d.rectangle([x,y0,x+bw,y0+h],fill=CREAM,outline=INK,width=4)
    ty=y0+pad
    for l in ls:
        pg.d.text((x+pad,ty),l,font=f,fill=INK); ty+=lead
    return h
cx0=M+w2+36; cy0=y+h3+22
hh=plate("From that day, men have called that sea the Myrtoan, after Myrtilus. And Hermes, his father, did not forget.",cx0,cy0,w3)
plate("Remember this cliff, princes. The curse thrown from it will climb back, generation by generation \u2014 and it climbs first to the table of Atreus.",cx0,cy0+hh+16,w3)
pg.num(15); pg.save(15)
print("all 15 pages built (band architecture)")

# ================= PAGE 16 =================
pg=Page()
p1=A("i01-pg16-pn1.png"); p2=A("i01-pg16-pn2.png"); p3=A("i01-pg16-pn3.png")
balloon(p1,"Let him reign who can show the gods' own token!",330,150,520,tail=(760,560),size=32)
balloon(p2,"Behold the sign, Mycenae! The gods choose me!",1120,190,460,tail=(780,430),size=46)
balloon(p3,"The heavens themselves un-say you, brother! Mycenae is mine \u2014 and you are banished!",255,120,430,tail=(560,430),size=32)
b1="Pelops's sons were Atreus and Thyestes. When the throne of golden Mycenae fell vacant, the city called for a son of Pelops \u2014 and the brothers' long hatred began."
b2="The token was a lamb with golden fleece, born in Atreus's flocks and hidden away. But Atreus's own wife, Aerope, loved Thyestes in secret \u2014 and stole it for him. So Thyestes showed the sign, and claimed the throne."
b3="Then Zeus answered with his own token, for Atreus: the sun stopped in heaven \u2014 and went backward, west to east, against its course."
bh1=pg.band_h(b1); bh2=pg.band_h(b2); bh3=pg.band_h(b3)
w1=1400; h1=int(w1*p1.height/p1.width)
H2=530; w2=int(H2*4/3)
w3=1450; h3=int(w3*p3.height/p3.width)
total=bh1+18+h1+16+bh2+18+H2+16+bh3+18+h3; y=(PH-total)//2
pg.band(b1,y); y+=bh1+18
pg.paste(p1,(PW-w1)//2,y,w1,h1); y+=h1+16
pg.band(b2,y); y+=bh2+18
pg.paste(p2,(PW-w2)//2,y,w2,H2); y+=H2+16
pg.band(b3,y); y+=bh3+18
pg.paste(p3,(PW-w3)//2,y,w3,h3)
pg.num(16); pg.save(16)

# ================= PAGE 17 =================
pg=Page()
p1=A("i01-pg17-pn1.png"); p2=A("i01-pg17-pn2.png"); p3=A("i01-pg17-pn3.png")
balloon(p1,"Rise, brother. What is past is past. Tonight you dine at my table.",1070,190,500,tail=(870,430),size=40)
balloon(p3,"My sons \u2014 my sons! Monster! Kin-devourer of your own blood's blood \u2014",330,780,460,tail=(380,380),size=36)
balloon(p3,"Gods of the dark! Break this house! Let the line of Atreus be served as I was served!",1080,880,480,tail=(450,380),size=36)
b1="In exile Thyestes starved \u2014 and in time Atreus learned of Aerope and the stolen lamb, and of the betrayal in his own marriage-bed. Yet he sent word of pardon, and welcome, and a feast of reconciliation."
b2="Of what was served at that table, the singer will say only this: Thyestes's young sons had been summoned to the palace before him \u2014 and were not at the feast."
bh1=pg.band_h(b1); bh2=pg.band_h(b2)
Hs=700; ws=int(Hs*4/3)
h2=750; p2c=p2.crop((0,40,1672,40+int(1672*h2/CW)))
total=bh1+18+Hs+22+bh2+18+h2+G+Hs; y=(PH-total)//2
pg.band(b1,y); y+=bh1+18
pg.paste(p1,(PW-ws)//2,y,ws,Hs); y+=Hs+22
pg.band(b2,y); y+=bh2+18
pg.paste(p2c,M,y,CW,h2); y+=h2+G
pg.paste(p3,(PW-ws)//2,y,ws,Hs)
pg.num(17); pg.save(17)

# ================= PAGE 18 =================
pg=Page()
p1=A("i01-pg18-pn1.png"); p2=A("i01-pg18-pn2.png"); p3=A("i01-pg18-pn3.png")
balloon(p2,"Say it again, my son.",300,160,360,tail=(500,420),size=36)
balloon(p2,"Remember Mycenae. Remember the feast.",1110,200,420,tail=(920,480),size=36)
balloon(p3,"And was it repaid, father? The feast?",1130,720,380,tail=(980,430),size=34)
balloon(p3,"All debts in this song are repaid, child. That one waits for the conqueror of Troy, on the day he comes home... but I run before my horses. Turn we now east \u2014 across the sea, to the wall.",330,918,560,tail=(290,460),size=32)
b1="Twice-cursed now \u2014 by Myrtilus's fall and Thyestes's feast \u2014 the house of Pelops shone on, golden and rotten at the root."
b2="In exile a son was born to Thyestes: Aegisthus. He was nursed on one lesson only."
h1=int(CW*p1.height/p1.width); bh1=pg.band_h(b1); bh2=pg.band_h(b2); H2=684
total=bh1+18+h1+22+bh2+18+H2; y=(PH-total)//2
pg.band(b1,y); y+=bh1+18
pg.paste(p1,M,y,CW,h1); y+=h1+22
pg.band(b2,y); y+=bh2+18
pg.paste(p2,M,y,912,H2); pg.paste(p3,M+912+36,y,912,H2)
pg.num(18); pg.save(18)

# ================= PAGE 19 — MAP =================
pg=Page()
mp=A("i01-pg19-pn1.png")
b1="East across the Aegean, at the gate of the Hellespont where all the sea-roads meet, stood Troy \u2014 Wilios of the songs, Wilusa in the great king's treaties \u2014 westernmost jewel of the empire of the Hatti."
bh=pg.band_h(b1)
mh=PH-2*M-bh-18-0
mw=int(mh*mp.width/mp.height)
if mw>CW: mw=CW; mh=int(CW*mp.height/mp.width)
y=(PH-(bh+18+mh))//2
pg.band(b1,y,ornate=True); y+=bh+18
pg.paste(mp,(PW-mw)//2,y,mw,mh)
cap_art(pg.im,"Her king in the old days was Laomedon. His story is the second root of the war \u2014 for the walls of Troy were built by gods... and never paid for.",PW//2-470,y+mh-40,940,26,anchor="lb")
pg.save(19)

# ================= PAGE 20 =================
pg=Page()
p1=A("i01-pg20-pn1.png"); p2=A("i01-pg20-pn2.png"); p3=A("i01-pg20-pn3.png")
balloon(p2,"Faster, you two! A year runs out, and my wall wants its towers!",1000,150,480,tail=(520,310),size=44)
balloon(p2,"The wage for those two, majesty \u2014 reckoned at the year's end \u2014",250,840,420,tail=(170,430),size=32)
balloon(p2,"The year is not ended.",680,960,330,tail=(470,340),size=32)
b1="In that age, for a fault against Zeus, Apollo and Poseidon were bound to serve a mortal man one full year for a wage. The man was Laomedon."
b2="Poseidon raised the wall. Apollo kept the king's cattle on the ridges of Ida. And the wall they made, no host of men could break."
b3="One short stretch only was built by mortal hands \u2014 the work of Aeacus, a pious mortal king who labored beside the gods. Mark that weaker stretch well, princes: the fate of Troy will pass through it."
h1=int(CW*p1.height/p1.width); bh1=pg.band_h(b1); bh2=pg.band_h(b2); bh3=pg.band_h(b3)
H=560; w2=int(H*4/3); w3=int(H*p3.width/p3.height)
if w2+G+w3>CW: w3=CW-G-w2
total=bh1+18+h1+16+bh2+22+H+16+bh3; y=(PH-total)//2
pg.band(b1,y); y+=bh1+18
pg.paste(p1,M,y,CW,h1); y+=h1+16
pg.band(b2,y); y+=bh2+22
xr=(PW-(w2+G+w3))//2
pg.paste(p2,xr,y,w2,H)
p3c=p3.crop((0,0,1672,int(1672*H/w3)))
pg.paste(p3c,xr+w2+G,y,w3,H); y+=H+16
pg.band(b3,y); pg.num(20); pg.save(20)

# ================= PAGE 21 =================
pg=Page()
p1=A("i01-pg21-pn1.png"); p2=A("i01-pg21-pn2.png"); p3=A("i01-pg21-pn3.png")
balloon(p1,"The year is served, king of Troy. The wall stands. Our wage.",300,850,440,tail=(330,430),size=36)
balloon(p1,"Wage? For runaway hirelings of whom no city will speak? Here is your wage: be gone unbeaten!",1120,900,460,tail=(1120,470),size=36)
balloon(p2,"And if you stand there glowering \u2014 I will bind your hands and feet, crop your ears with bronze, and sell you to the islands for what a mutilated slave will fetch!",370,300,500,tail=(700,600),size=36)
balloon(p3,"Hear him, brother. He has said it with his own mouth, before witnesses.",700,1290,360,tail=(670,470),size=30)
balloon(p3,"I heard, brother. Let the sea answer him. Let the sun answer him.",300,1430,380,tail=(400,390),size=30)
b1="And they were gone from the hall like light off bronze."
bh=pg.band_h(b1); H2=684; H3=1100; w3=int(H3*p3.width/p3.height)
total=H2+G+H3+16+bh; y=(PH-total)//2
pg.paste(p1,M,y,912,H2); pg.paste(p2,M+912+36,y,912,H2); y+=H2+G
pg.paste(p3,(PW-w3)//2,y,w3,H3); y+=H3+16
pg.band(b1,y); pg.num(21); pg.save(21)

# ================= PAGE 22 =================
pg=Page()
p1=A("i01-pg22-pn1.png"); p2=A("i01-pg22-pn2.png"); p3=A("i01-pg22-pn3.png")
balloon(p3,"The gods' price, majesty... is the king's own blood. The monster must have... your daughter. Hesione.",300,850,440,tail=(150,430),size=40)
balloon(p3,"...Then the gods shall have her. Chain her to the rocks.",1070,640,400,tail=(850,330),size=40)
b1="Then Apollo the far-shooter turned his silver bow on Troy, and plague walked the streets of the unpaid wall."
b2="And Poseidon sent the salt flood, and out of the flood a monster of the deep, to devour the people of the shore."
bh1=pg.band_h(b1); bh2=pg.band_h(b2)
r1=820; r2=820
p1c=p1.crop((0,50,1672,50+int(1672*r1/CW)))
p2c=p2.crop((0,80,1672,80+int(1672*r2/CW)))
H3=640; w3=int(H3*4/3)
total=bh1+18+r1+22+bh2+18+r2+G+H3; y=(PH-total)//2
pg.band(b1,y); y+=bh1+18
pg.paste(p1c,M,y,CW,r1); y+=r1+22
pg.band(b2,y); y+=bh2+18
pg.paste(p2c,M,y,CW,r2); y+=r2+G
pg.paste(p3,(PW-w3)//2,y,w3,H3)
pg.num(22); pg.save(22)

# ================= PAGE 23 =================
pg=Page()
p1=A("i01-pg23-pn1.png"); p2=A("i01-pg23-pn2.png"); p3=A("i01-pg23-pn3.png")
cap_art(p2,"But that day there put in at the Trojan shore, homing from the country of the Amazons, the mightiest man of that age or any age.",p2.width-30,26,560,26,anchor="rt")
balloon(p2,"The sea is standing up, Heracles.",900,400,340,tail=(600,280),size=36)
balloon(p2,"So it is. And there is a girl in its road.",700,700,360,tail=(320,270),size=36)
balloon(p3,"Stranger \u2014 that club, that bow \u2014 save her, and name your price!",700,140,440,tail=(930,220),size=30)
balloon(p3,"I do not sell rescues, king. But a labor deserves a wage. My price is the divine white mares of your house \u2014 the deathless horses Zeus himself once gave to Troy.",720,810,540,tail=(380,220),size=30)
balloon(p3,"The divine mares! ...Done, and done, before witnesses!",1220,970,380,tail=(990,300),size=30)
b1="And Troy chained its princess to the rock at low tide \u2014 Hesione, who had done no wrong \u2014 and the city watched from the walls, and the sea began to move."
bh=pg.band_h(b1); Hgrid=1296; L=863; R=960
h2=int(R*p2.height/p2.width); h3=Hgrid-h2-36
total=bh+18+Hgrid; y=(PH-total)//2
pg.band(b1,y); y+=bh+18
x0=(PW-(L+36+R))//2
pg.paste(p1,x0,y,L,Hgrid)
pg.paste(p2,x0+L+36,y,R,h2)
p3c=p3.crop((0,0,1448,int(1448*h3/R)))
pg.paste(p3c,x0+L+36,y+h2+36,R,h3)
pg.num(23); pg.save(23)

# ================= PAGE 24 =================
pg=Page()
p1=A("i01-pg24-pn1.png"); p2=A("i01-pg24-pn2.png"); p3=A("i01-pg24-pn3.png")
balloon(p3,"My life is yours, stranger.",1050,790,340,tail=(830,330),size=34,heart=True)
balloon(p3,"Keep it, princess. It was never your debt being paid on that rock.",330,950,460,tail=(360,320),size=38)
h1=int(CW*p1.height/p1.width); H2=684
total=h1+G+H2; y=(PH-total)//2
pg.paste(p1,M,y,CW,h1); y+=h1+G
pg.paste(p2,M,y,912,H2); pg.paste(p3,M+912+36,y,912,H2)
pg.num(24); pg.save(24)

# ================= PAGE 25 =================
pg=Page()
p1=A("i01-pg25-pn1.png"); p2=A("i01-pg25-pn2.png"); p3=A("i01-pg25-pn3.png")
balloon(p1,"Your wage, hero: two fine horses of my stable.",1300,140,380,tail=(1240,380),size=28)
balloon(p1,"These are not the mares of Tros.",700,115,340,tail=(300,185),size=28)
balloon(p1,"The mares of Tros are Troy's holy things \u2014 not fee for a wandering strongman. Take these and my thanks... or take the road.",1290,480,440,size=28)
balloon(p2,"King of Troy \u2014 a god built your wall, and you cheated him. A man saved your child, and you cheat him too.",380,190,560,size=44)
balloon(p2,"Keep the mares. Feed them well. I will come back for my wage \u2014 and your wall will not help you, because I know who built it... and I know where it was built by men.",1010,880,620,size=44)
b3="So Laomedon cheated a second wage \u2014 first the gods', now the hero's \u2014 and laughed. He would soon learn how long such debts are remembered."
h1=int(CW*p1.height/p1.width); bh3=pg.band_h(b3)
H=560; w2=int(H*4/3); w3=int(H*p3.width/p3.height)
if w2+G+w3>CW: w3=CW-G-w2
total=h1+G+H+16+bh3; y=(PH-total)//2
pg.paste(p1,M,y,CW,h1); y+=h1+G
xr=(PW-(w2+G+w3))//2
pg.paste(p2,xr,y,w2,H)
p3c=p3.crop((0,0,1672,int(1672*H/w3)))
pg.paste(p3c,xr+w2+G,y,w3,H); y+=H+16
pg.band(b3,y); pg.num(25); pg.save(25)

# ================= PAGE 26 =================
pg=Page()
p1=A("i01-pg26-pn1.png"); p2=A("i01-pg26-pn2.png"); p3=A("i01-pg26-pn3.png")
balloon(p2,"To the wall! Not the gate \u2014 the wall! Telamon \u2014 you remember the stretch I showed you?",620,650,420,tail=(575,335),size=30)
balloon(p2,"The man-built stretch, son of Zeus! My father Aeacus laid those stones \u2014 I know his work!",1080,660,440,tail=(795,335),size=30)
b1="Years later, Heracles came back for his wage \u2014 not with a great army, but with six ships, picked companions, and a debt to collect."
b3="For Telamon was the son of Aeacus \u2014 the very mortal who had helped the gods build the wall. And a son knows where his father's work is weakest."
bh1=pg.band_h(b1); bh3=pg.band_h(b3)
r1=800; r2=850
p1c=p1.crop((0,60,1672,60+int(1672*r1/CW)))
p2c=p2.crop((0,0,1672,int(1672*r2/CW)))
H3=600; w3=int(H3*4/3)
total=bh1+18+r1+G+r2+G+H3+16+bh3; y=(PH-total)//2
pg.band(b1,y); y+=bh1+18
pg.paste(p1c,M,y,CW,r1); y+=r1+G
pg.paste(p2c,M,y,CW,r2); y+=r2+G
pg.paste(p3,(PW-w3)//2,y,w3,H3); y+=H3+16
pg.band(b3,y); pg.num(26); pg.save(26)

# ================= PAGE 27 =================
pg=Page()
p1=A("i01-pg27-pn1.png"); p2=A("i01-pg27-pn2.png"); p3=A("i01-pg27-pn3.png")
balloon(p3,"Stones for an altar! An altar to Heracles the glorious victor \u2014 first of heroes, by whose might the wall is down!",420,200,560,tail=(560,560),size=36)
b1="And the wall the gods built was never broken. The wall men built broke \u2014 and Telamon of Salamis went through it first of all mankind."
b2="But glory is a dangerous wage too. When Heracles saw another man take the first honor of the breach, the black mood of his line came upon him."
b3="And Heracles stood a moment... and laughed, and the black mood passed \u2014 for honor had been given its share. Mark the trick of it, princes: a wise friend can turn a hero's wrath aside. Later in this song you will see what happens when no such friend is near."
bh1=pg.band_h(b1); bh2=pg.band_h(b2); bh3=pg.band_h(b3)
Hgrid=1296; L=863; Rw=840; hr=(Hgrid-36)//2
total=bh1+18+Hgrid+16+bh2+14+bh3; y=(PH-total)//2
pg.band(b1,y); y+=bh1+18
x0=(PW-(L+36+Rw))//2
pg.paste(p1,x0,y,L,Hgrid)
p2c=p2.crop((0,0,1448,int(1448*hr/Rw)))
p3c=p3.crop((0,0,1448,int(1448*hr/Rw)))
pg.paste(p2c,x0+L+36,y,Rw,hr)
pg.paste(p3c,x0+L+36,y+hr+36,Rw,hr); y+=Hgrid+16
pg.band(b2,y); y+=bh2+14
pg.band(b3,y); pg.num(27); pg.save(27)

# ================= PAGE 28 =================
pg=Page()
p1=A("i01-pg28-pn1.png"); p2=A("i01-pg28-pn2.png"); p3=A("i01-pg28-pn3.png")
balloon(p2,"King of Troy. Two wages owed. Payment... in full.",300,880,440,tail=(430,320),size=38)
b1="Through the lower city to the palace hill the six ships' men drove them, and at the top there was nowhere left to be carried in a litter."
b3="Laomedon fell, and his sons with him \u2014 all his sons but one: Podarces, the youngest, too young for the war and too proud to run."
h1=int(CW*p1.height/p1.width); bh1=pg.band_h(b1); bh3=pg.band_h(b3); H2=684
total=bh1+18+h1+G+H2+16+bh3; y=(PH-total)//2
pg.band(b1,y); y+=bh1+18
pg.paste(p1,M,y,CW,h1); y+=h1+G
pg.paste(p2,M,y,912,H2); pg.paste(p3,M+912+36,y,912,H2); y+=H2+16
pg.band(b3,y); pg.num(28); pg.save(28)

# ================= PAGE 29 =================
pg=Page()
p1=A("i01-pg29-pn1.png"); p2=A("i01-pg29-pn2.png"); p3=A("i01-pg29-pn3.png")
balloon(p1,"Son of Aeacus. My captor and my lord. May a captive ask one gift?",860,150,520,tail=(560,420),size=30)
balloon(p2,"My brother's life. I purchase it \u2014 with this veil, and all it is worth.",330,860,460,tail=(370,400),size=36)
balloon(p2,"Sold, princess. Let all Troy witness: the boy is bought back from the spear.",1090,930,440,tail=(760,290),size=36)
balloon(p3,"Podarces the swift-footed no longer. From this day your name is your ransom, boy: Priamos \u2014 'the purchased one.'",380,190,560,size=36)
balloon(p3,"Reign in Troy, and remember what buys and what forfeits: the wage paid, and the wage withheld.",1040,900,560,size=36)
b1="To Telamon, first through the wall, went the first prize of honor: Hesione the princess, whom he had seen at the rock and never ceased seeing."
h1=int(CW*p1.height/p1.width); bh1=pg.band_h(b1); H2=684
total=bh1+18+h1+G+H2; y=(PH-total)//2
pg.band(b1,y); y+=bh1+18
pg.paste(p1,M,y,CW,h1); y+=h1+G
pg.paste(p2,M,y,912,H2); pg.paste(p3,M+912+36,y,912,H2)
pg.num(29); pg.save(29)

# ================= PAGE 30 =================
pg=Page()
p1=A("i01-pg30-pn1.png"); p2=A("i01-pg30-pn2.png"); p3=A("i01-pg30-pn3.png")
b1="So Hesione of Troy sailed west to Salamis, a Trojan princess in an Achaean hall. There she bore Telamon a son: Teucer the archer \u2014 half-Trojan blood that would one day come back to Troy, in the ships of her enemies."
b2="And in the ashes, Troy crowned its child. Priam the purchased rebuilt the walls \u2014 and where men's work had broken, men's work was set again, stone by stone, in the same fated stretch."
b3="But a wall may be rebuilt, and a wage still owed. The gods' grievance was not buried with Laomedon. It waited \u2014 for the fullness of the plan of Zeus."
bh1=pg.band_h(b1); bh2=pg.band_h(b2); bh3=pg.band_h(b3)
r1=760; p1c=p1.crop((0,40,1672,40+int(1672*r1/CW)))
H2=760; w2=int(H2*p2.width/p2.height)
r3=420; p3c=p3.crop((0,180,1672,180+int(1672*r3/CW)))
total=bh1+18+r1+22+bh2+18+H2+G+r3+16+bh3; y=(PH-total)//2
pg.band(b1,y); y+=bh1+18
pg.paste(p1c,M,y,CW,r1); y+=r1+22
pg.band(b2,y); y+=bh2+18
pg.paste(p2,(PW-w2)//2,y,w2,H2); y+=H2+G
pg.paste(p3c,M,y,CW,r3); y+=r3+16
pg.band(b3,y); pg.num(30); pg.save(30)

# ================= PAGE 31 =================
pg=Page()
p1=A("i01-pg31-pn1.png"); p2=A("i01-pg31-pn2.png"); p3=A("i01-pg31-pn3.png")
balloon(p1,"Thus the two roots, princes: the feast in the west, the wall in the east. From the one came Agamemnon and the curse of his house. From the other, Priam and the debt of his city.",520,750,540,tail=(390,310),size=30)
balloon(p2,"And the Earth, father? Was her burden eased?",1080,790,400,tail=(1040,390),size=36)
balloon(p2,"Not yet, child. As yet, not one hero had fallen. The scales of Zeus had only begun to move.",330,930,440,tail=(430,440),size=36)
balloon(p3,"Tomorrow, if the Muse is willing: a wedding on a holy mountain \u2014 all the gods among the guests \u2014 and one goddess uninvited, with a golden apple in her hand.",1080,300,460,tail=(820,640),size=36)
h1=int(CW*p1.height/p1.width); H2=684
total=h1+G+H2; y=(PH-total)//2
pg.paste(p1,M,y,CW,h1); y+=h1+G
pg.paste(p2,M,y,912,H2); pg.paste(p3,M+912+36,y,912,H2)
pg.num(31); pg.save(31)

# ================= PAGE 32 — GNOME =================
pg=Page()
gp=A("i01-pg32-pn1.png")
gh=PH-80; gw=int(gh*gp.width/gp.height)
if gw>CW: gw=CW; gh=int(CW*gp.height/gp.width)
x0=(PW-gw)//2; y0=(PH-gh)//2
pg.paste(gp,x0,y0,gw,gh)
# ornamented gnome plate \u2014 centered in the art's blank cartouche (page-space center ~(1000,700), max ~1400x560)
f0=ImageFont.truetype(CB,36)
gn="\u201cTwo jars stand at the door-sill of Zeus: one holds evils, one holds blessings. To one man he gives of both mingled; to another, sorrow only \u2014 and no mortal chooses the ladle.\u201d"
lines=wrap(pg.d,gn.upper(),f0,1150)
lead=48; pad=34
fs=ImageFont.truetype(CI,24)
attr="\u2014 AFTER THE WORDS OF ACHILLES TO PRIAM, IN THE LAST BOOK OF THE SONG OF THE WRATH."
aw=pg.d.textlength(attr,font=fs)
tw=max(pg.d.textlength(l,font=f0) for l in lines)
bw=int(max(tw,aw))+2*pad
bh=pad+lead*len(lines)+18+34+pad
bx=1000-bw//2; by=700-bh//2
pg.d.rectangle([bx+6,by+6,bx+bw+6,by+bh+6],fill=(0,0,0))
pg.d.rectangle([bx,by,bx+bw,by+bh],fill=CREAM,outline=INK,width=4)
pg.d.rectangle([bx+9,by+9,bx+bw-9,by+bh-9],outline=(150,40,30),width=3)
ty=by+pad
for l in lines:
    lw=pg.d.textlength(l,font=f0); pg.d.text((bx+(bw-lw)//2,ty),l,font=f0,fill=INK); ty+=lead
ty+=18
pg.d.text((bx+(bw-aw)//2,ty),attr,font=fs,fill=(90,60,40))
# end plate
fb=ImageFont.truetype(BG,54)
ep="NEXT: ISSUE 2 \u2014 THE SWAN AND THE EGG"
ew=pg.d.textlength(ep,font=fb)
ex=PW//2-int(ew//2); ey=y0+gh-150
pg.d.rectangle([ex-30+6,ey-18+6,ex+ew+30+6,ey+72+6],fill=(0,0,0))
pg.d.rectangle([ex-30,ey-18,ex+ew+30,ey+72],fill=CREAM,outline=INK,width=4)
pg.d.text((ex,ey),ep,font=fb,fill=(150,40,30),stroke_width=2,stroke_fill=INK)
pg.save(32)
print("pages 16-32 built")
