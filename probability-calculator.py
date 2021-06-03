import collections
import random
import copy

class Hat:
    def __init__(self, **args):
        self.hat = dict()
        for key, value in args.items():
            self.hat[key] = value

        self.contents = []
        for key in self.hat:
            for index in range(self.hat[key]):
                self.contents.append(key)

    def draw(self, num):
        if(num > len(self.contents)): return self.contents

        drawn_balls = random.sample(range(0, len(self.contents)), num)
        drawn_balls = sorted(drawn_balls, reverse=True)

        removed_balls = []
        for num in drawn_balls:
            removed_balls.append(self.contents.pop(num))

        return removed_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success = 0
    attempts = 0

    def run_test(balls, expected):
        for keys in expected:
            try: expected_balls[keys] <= hat_counter[keys]
            except: return False
            if not expected_balls[keys] <= hat_counter[keys]:
                return False
        return True

    for i in range(num_experiments):
        test = copy.deepcopy(hat).draw(num_balls_drawn)
        hat_counter = dict(collections.Counter(test))

        if run_test(hat_counter, expected_balls):
            success += 1
        attempts += 1

    return float(success)/float(attempts)
