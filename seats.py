def is_free(row, listOfLetters):
    for l in listOfLetters:
        if l in row:
            return False
    return True 

def solution(N, S):
    seats = [set() for _ in range(51)]
    for seat in S.split():
        number = seat[:-1]
        letter = seat[-1:]
        seats[int(number)].add(letter) 

    families = 0
    for row in range(1, N+1):
        be = is_free(seats[row], ['B', 'C', 'D', 'E'])
        fj = is_free(seats[row], ['F', 'G', 'H', 'J'])
        dg = is_free(seats[row], ['D', 'E', 'F', 'G'])
        
        if be:
            if fj:
                families += 2
            else:
                families += 1
        else:
            if fj or dg:
                families += 1
    
    return families

# Algorithm
# O ( Tickets + Seats )
# Each row is represented by a set
# A letter in the set represents an occupied seat
#
# A sold ticket 2B would mean:
# seats[2].add('B')
# 'B' in seats[2] == True
#
#
# # A B C _ D E F G _ H J K
# 1 
#
# Optimal Solution: two per row 
# # A B C   D E F G   H J K
# 2 _ x x   x x y y   y y _
#
# Options for 1 family per row:
# # A B C   D E F G   H J K
# 3 _ x x   x x _ _   _ _ _
# 4 _ _ _   y y y y   _ _ _
# 5 _ _ _   _ _ z z   z z _