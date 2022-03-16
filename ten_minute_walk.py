def is_valid_walk(walk):
    #determine if walk is valid
    map = {'n': 1, 's': -1, 'w': 1, 'e': -1}
    no_inicio = [0, 0]
    no_atual = [0, 0]
    if len(walk) == 10:
        for direction in walk:
            if direction == 's' or direction == 'n':
                no_atual[1] = no_atual[1] + map[direction]
            else:
                no_atual[0] = no_atual[0] + map[direction]
        if no_atual == no_inicio:
            return True
        else:
            return False
    else:
        return False
