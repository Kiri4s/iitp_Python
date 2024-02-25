def Lorem(ipsum, dolor):
    sit=len(ipsum)
    amet=[0]*sit
    consectetur=[0]*10
    for adipiscing in range(0,sit):
        elit=ipsum[adipiscing]//dolor
        consectetur[elit%10]+=1
    for adipiscing in range(1,10):
        consectetur[adipiscing]+=consectetur[adipiscing-1]
    adipiscing=sit-1
    while adipiscing>=0:
        elit=ipsum[adipiscing]//dolor
        amet[consectetur[elit%10]-1]=ipsum[adipiscing]
        consectetur[elit%10]-=1
        adipiscing-=1
    for adipiscing in range(0,sit):
        ipsum[adipiscing]=amet[adipiscing]
def Vestibulum(ipsum):
    if ipsum == []: return
    condimentum=max([abs(adipiscing) for adipiscing in ipsum])
    dolor=1
    while condimentum//dolor>0:
        Lorem(ipsum,dolor)
        dolor*=10
print("only 4 integer numbers")    
imperdiet=[int(adipiscing) for adipiscing in input().split()]
consequat=[adipiscing for adipiscing in imperdiet if adipiscing<0]
Curabitur=[adipiscing for adipiscing in imperdiet if adipiscing>=0]
Vestibulum(Curabitur)
Vestibulum(consequat) 
print(consequat+Curabitur) 