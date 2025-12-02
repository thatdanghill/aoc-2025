p=[(l[0]=='L',int(l[1:]))for l in open('input.txt')]
z=Z=0
s=50
S=100
for o,c in p:
 b=s!=0
 g=(1,-1)[o]
 s+=g*c
 Z+=g*s//S+(0,b)[o]
 s%=S
 z+=s==0
print(f"Silver: {z}\nGold: {Z}")