import os
cwd = os.getcwd()


hands = {
    'rock': 1,
    'paper': 2,
    'scissors': 3
}

strategy = [
    ['A', 'B', 'C'],
    # ['X', 'Y', 'Z'],
    # ['X', 'Z', 'Y'],
    # ['Y', 'X', 'Z'],
    # ['Y', 'Z', 'X'],
    # ['Z', 'X', 'Y'],
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


def map_hands(one, two):
    one_dict = {strategy[0][i]: [k for k in hands.keys()][i] for i in range(len(strategy[0]))}
    two_dict = {strategy[1][i]: [k for k in hands.keys()][i] for i in range(len(strategy[1]))}
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
    result = []
    points = 0
    for i in inp:
        # print(i)
        j = map_hands(*i)
        # print(j)
        res = round(*j)
        # result.append(round(*j)[0])
        result.append(res[0])
        points += res[1]

    wins = result.count(True)
    loses = result.count(False)
    draws = result.count('draw')
    print("Total wins {}".format(wins))
    print("Total loses {}".format(loses))
    print("Total draws {}".format(draws))
    print("Total points: {}".format(points))




if __name__ == '__main__':
    main()
