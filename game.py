def game(p1, p2):
    """
    Enter values that represent the player choice
    Return p1 if player 1 wins otherwise p2
    """

    if (p1 == "piedra" and p2 == "tijera") or (p1 =="papel" and p2 == "piedra") or (p1=="tijera" and p2 == "papel"):
        return 'p1'
    elif p1 == p2:
        return 'empate'
    else:
        return 'p2'
