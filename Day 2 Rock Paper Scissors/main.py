import os
cwd = os.getcwd()


hands = {
    'rock': 1,
    'paper': 2,
    'scissors': 3
}

strategy = [
    ['X', 'Y', 'Z'],
    ['X', 'Z', 'Y'],
    ['Y', 'X', 'Z'],
    ['Y', 'Z', 'X'],
    ['Z', 'X', 'Y'],
    ['Z', 'Y', 'X'],
]


def round(one, two):
    logic = {
        'rock': 'scissors',
        'paper': 'rock',
        'scissors': 'paper'
    }
    one_beats = logic[one]
    two_beats = logic[two]
    if one_beats == two:
        return False, hands[two]
    elif two_beats == one:
        return True, hands[two] + 6
    else:
        return 'draw', hands[two] + 3


def map_hands(one, two, strtg):
    abc = ['A', 'B', 'C']
    one_dict = {abc[i]: [k for k in hands.keys()][i] for i in range(len(abc))}
    two_dict = {strtg[i]: [k for k in hands.keys()][i] for i in range(len(strtg))}
    return one_dict[one], two_dict[two]


def read_input(file):
    output = []
    with open(file, 'r') as f:
        lines = f.read().split('\n')
        for line in lines:
            output.append(line.split(' '))
    return output


def main():
    inp = read_input(os.path.join(cwd, 'input'))
    for n, s in enumerate(strategy):
        result = []
        points = 0
        print(f"Strategy {n} - {s}")
        for i in inp:
            j = map_hands(*i, strategy[n])
            res = round(*j)
            result.append(res[0])
            points += res[1]

        wins = result.count(True)
        loses = result.count(False)
        draws = result.count('draw')
        print("Total wins {}".format(wins))
        print("Total loses {}".format(loses))
        print("Total draws {}".format(draws))
        print("Total points: {}".format(points))
        print('')



if __name__ == '__main__':
    main()
