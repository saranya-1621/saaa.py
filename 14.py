chaa,acho=map(str,input().split())
ayas=0
if len(cha)>len(cho):
  chaa,acho=acho,chaa
p=0
while p<len(chaa):
  ayas+=(ord(acho[p])-ord(chaa[p]))
  p+=1
for p in range(p,len(acho)):
  ayas+=ord(acho[p])-ord('a')+1
print(ayas)
