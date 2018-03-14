from game import game 

def test_game_01():
   assert game('piedra', 'tijera') == 'p1', 'Unexpected result'
   assert game('tijera', 'piedra') == 'p2', 'Unexpected result'
   assert game('tijera', 'papel') == 'p1', 'Unexpected result'
   # p1= raw_input ('jugador 1: ')
    #p2= raw_input ('jugador 2: ')
    #print game(p1,p2)
   
    
