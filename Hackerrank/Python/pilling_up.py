from collections import deque
T = int(input())
for i in range(T):

	n = int(input())
	sideLengths = deque(map(int,input().split()))
	vertical_tower = list()
	for j in range(len(sideLengths)):
		rightmost_cube_sidelength = sideLengths[-1]
		leftmost_cube_sidelength = sideLengths[0]

		if rightmost_cube_sidelength == leftmost_cube_sidelength :
			#choose leftmost cube
			vertical_tower.append(leftmost_cube_sidelength)
			sideLengths.popleft()


		elif rightmost_cube_sidelength > leftmost_cube_sidelength :
			#choose rightmost cube
			vertical_tower.append(rightmost_cube_sidelength)
			sideLengths.pop()

		else :
			#choose leftmost cube
			vertical_tower.append(leftmost_cube_sidelength)
			sideLengths.popleft()


	
	ideal_vertical_tower = sorted(vertical_tower,reverse=True)
	#print(vertical_tower)
	#print(ideal_vertical_tower)

	logic = bool()
	logic = ideal_vertical_tower == vertical_tower
	#print(logic) 
	if logic:
		print("Yes")
	else :
		print("No")