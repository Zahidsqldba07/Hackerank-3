K = int(input())
room_numbers = list(map(int,input().split()))
captains_room_number = (sum(set(room_numbers))*K - sum(room_numbers))//(K-1)
'''  here we could've solved this question using dictionaries but it was not 
passing all of the test cases so we used maths..

considering the difference between the case 
if all of the elements had K copies (captains_room_number*K)
and
the given case (captains_room_number*1)
on solving this we'll get on the other side captains_room_number * K-1
so we divide it by K-1 '''
print(captains_room_number)