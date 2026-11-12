import json,os,sys,urllib.request as R
U=os.environ["MAKEFUN_ENV_URL"]
def q(p,d={}):
 return json.load(R.urlopen(R.Request(U+p,json.dumps(d).encode(),{"content-type":"application/json"})))
V=[0,100,325,335,500,975,2e4]
DV=[[],[33,31,18,14,-14,-18,-31,-33],[17,15,-15,-17],[16,1,-1,-16]]
DV+=[DV[2]+DV[3]]*2
SQ=[chr(97+(i&7))+str((i>>4)+1) for i in range(128)]
CB=[min(i&7,7-i&7)+min(i>>4,7-(i>>4)) if not i&0x88 else 0 for i in range(128)]
def F(x):
 p=x.split();b=[0]*128;c=0;r=7;f=0
 for ch in p[0]:
  if ch=="/":r-=1;f=0
  elif ch.isdigit():f+=int(ch)
  else:
   b[r*16+f]=(1+"pnbrqk".index(ch.lower()))*(1 if ch.isupper() else -1);f+=1
 for ch in p[2]:c|={"K":1,"Q":2,"k":4,"q":8}.get(ch,0)
 return b,p[1]=="w",c
def atk(b,i,s):
 o=1 if s else -1
 for d in DV[1]+DV[4]:
  j=i+d
  if not j&0x88 and b[j]*o==(2 if d in DV[1] else 6):return 1
 for d in(-1,1):
  j=i-(16 if s else -16)+d
  if not j&0x88 and b[j]==o:return 1
 for d in(16,-16,1,-1,17,15,-15,-17):
  j=i+d
  while not j&0x88:
   w=b[j]*o
   if w:
    if w==5 or w==(4 if abs(d)in(1,16) else 3):return 1
    break
   j+=d
 return 0
def G(b,s,c):
 M=[];o=1 if s else -1;si=16 if s else -16
 for i,p in enumerate(b):
  if not p or (p>0)!=s:continue
  t=abs(p)
  if t==1:
   J=[];j=i+si
   if not j&0x88 and not b[j]:
    J=[j]
    if i>>4==(1 if s else 6) and not b[j+si]:J+=[j+si]
   for d in(-1,1):
    j=i+si+d
    if not j&0x88 and b[j]*o<0:J+=[j]
   for j in J:M+=[(i,j,0)] if (j>>4)%7 else [(i,j,5),(i,j,4),(i,j,3),(i,j,2)]
  elif t==2:
   for d in DV[1]:
    j=i+d
    if not j&0x88 and b[j]*o<=0:M.append((i,j,0))
  elif t>4:
   for d in DV[4]:
    j=i+d
    if not j&0x88 and b[j]*o<=0:M.append((i,j,0))
   if t>5 and i in(4,116):
    if c&(1 if s else 4)and not(b[i+1]or b[i+2])and not atk(b,i+1,not s):M.append((i,i+2,0))
    if c&(2 if s else 8)and not(b[i-1]or b[i-2]or b[i-3])and not atk(b,i-1,not s):M.append((i,i-2,0))
  else:
   for d in DV[t-1]:
    j=i+d
    while not j&0x88:
     w=b[j]
     if w*o>0:break
     M.append((i,j,0))
     if w:break
     j+=d
 M.sort(key=lambda m:9*V[abs(b[m[1]])]-V[abs(b[m[0]])] if b[m[1]] else 0,reverse=True)
 return M
def H(b,m,s):
 f,t,p=m;n=b[:];pc=n[f];n[f]=0;n[t]=p*s if p else pc
 if abs(pc)==6 and abs(t-f)==2:
  r=t+(1 if t>f else -2);n[t+(-1 if t>f else 1)]=n[r];n[r]=0
 return n
def E(b):
 v=0
 for i,p in enumerate(b):
  if p:
   t=abs(p);w=V[t]+((i>>4 if p>0 else 7-(i>>4))*8 if t==1 else (CB[i]*8 if t<6 else -CB[i]*9))
   v+=w if p>0 else -w
 return v
def kp(b,s):return b.index(6 if s else -6)
N=0;LM=52000
def Z(b,s,c,a,z,d=0):
 global N
 N+=1
 v=E(b)*(1 if s else -1)
 if v>=z or d>3:return v
 if v>a:a=v
 for m in G(b,s,c):
  if not(b[m[1]]or m[2]):continue
  y=H(b,m,s)
  if atk(y,kp(y,s),not s):continue
  w=-Z(y,not s,c,-z,-a,d+1)
  if w>v:
   v=w
   if v>a:
    a=v
    if a>=z:break
 return v
def S(b,s,c,d,a,z):
 global N
 N+=1
 if N>LM:raise StopIteration
 if d<1:return Z(b,s,c,a,z)
 v=-99999;k=kp(b,s)
 for m in G(b,s,c):
  y=H(b,m,s)
  if atk(y,kp(y,s),not s):continue
  w=-S(y,not s,c,d-1,-z,-a)
  if w>v:
   v=w
   if v>a:
    a=v
    if a>=z:break
 return -25000+d*atk(b,k,not s) if v==-99999 else v
def C(m):
 f,t,p=m
 return SQ[f]+SQ[t]+("nbrq"[p-2]if p else"")
def B(b,s,c,lm):
 global N
 M=[m for m in G(b,s,c) if C(m) in lm]
 if not M:return lm[0]
 bm=M[0];N=0
 for d in range(1,9):
  a=-99999;nb=None
  try:
   for m in M:
    y=H(b,m,s)
    if atk(y,kp(y,s),not s):continue
    w=-S(y,not s,c,d-1,-99999,99999) if not nb else -S(y,not s,c,d-1,-a-1,-a)
    if nb and w>a:w=-S(y,not s,c,d-1,-99999,99999)
    if w>a:a=w;nb=m
  except StopIteration:break
  if nb is None:break
  bm=nb;M=[bm]+[x for x in M if x!=bm]
 return C(bm)
while True:
 g=q("/game")
 if g["status"]=="done":break
 while g["status"]=="your_move":
  b,s,c=F(g["fen"])
  g=q("/move",{"game":g["game"],"move":B(b,s,c,set(g["legal_moves"]))})
 print("G%d %s %d"%(g["game"],g["outcome"],g["plies"]),file=sys.stderr)
