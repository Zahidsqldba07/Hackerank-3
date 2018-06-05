import math
AB = float(input())
BC = float(input())
MBC = math.atan(AB/BC)
MBC = math.degrees(MBC)
fraction = MBC - int(MBC)
if fraction > 0.5 :
	MBC = math.ceil(MBC)
else :
	MBC = math.floor(MBC)
MBC = str(MBC) + '°'
print(MBC)