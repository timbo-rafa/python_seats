from seats import solution
from itertools import product

s = 'ABC DEFG HJK'
seat_letters = ['B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K']

class Unit_Test():
    def test_basic(self):
        tickets = '1B 1D 1F 1H 2B 2H 4D 4G'

        ans = solution(4, tickets)

        assert ans == 3
    
    def test_one_family_per_row_on_different_seats(self):
        tickets = '1B 2H 3E 4F'

        ans = solution(4, tickets)

        assert ans == 4

    def test_for_full_plane(self):
        N = 5
        ticket_numbers = [str(tn) for tn in list(range(1, N+1))]
        ticket_permutation = product( ticket_numbers, seat_letters)
        tickets = ' '.join([''.join(tp) for tp in ticket_permutation])
        
        ans = solution(N, tickets)

        assert ans == 0

    def test_for_empty_seats(self):
        ans = solution(10, '')

        assert ans == 20
