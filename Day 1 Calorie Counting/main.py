import os

cwd = os.getcwd()


def count_calories(meals):
    calories = 0
    for meal in meals:
        calories += meal
    return calories


def read_input(file):
    with open(file, 'r') as f:
        output = []
        for calories in f.read().split('\n\n'):
            output.append([eval(i) for i in calories.split('\n')])
    return output


def max_cal(elves):
    return max([count_calories(e) for e in elves])


elves = read_input(os.path.join(cwd, 'input'))

def part_one(elves):
    return max_cal(elves)

def part_two(elves):
    all_elves = [count_calories(e) for e in elves]
    top_three = sorted(all_elves, reverse=True)[:3]
    top_three_sum = sum(top_three)
    return top_three_sum

if __name__ == '__main__':
    ans1 = part_one(elves)
    print(ans1)
    ans2 = part_two(elves)
    print(ans2)
