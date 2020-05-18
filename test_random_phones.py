import random
from typing import Set

android = {(6536, "Android"),
           (6537, "Android"),
           (6538, "Android"),
           (6535, "Android"),
           (5000, "Android"),
           (5001, "Android"),
           (5002, "Android"),
           (5003, "Android"),
           (5004, "Android"),
           (5006, "Android"),
           (5007, "Android"),
           (5008, "Android"),
           (5009, "Android"),
           (5012, "Android")}

ios = {
    (6554, "iOS"),
    (6563, "iOS"),
    (6566, "iOS"),
    (6565, "iOS"),
    (6568, "iOS"),
    (6567, "iOS"),
    (6534, "iOS"),
    (6544, "iOS"),
    (6542, "iOS"),
    (6541, "iOS"),
    (6531, "iOS"),
    (6533, "iOS"),
    (6543, "iOS"),
    (6548, "iOS")
}

all = ios.union(android)


def random_selection(options: Set, k=1) -> Set:
    copy = options.copy()
    result = set()
    i = 0
    while i < k:
        result.add(copy.pop())
        i += 1

    return result


# Bus scenario 11 participants
# Configuration 1
def bus_scenario():
    five_android = random_selection(android, k=5)
    five_ios = random_selection(ios, k=5)
    walking_person = random_selection(all - five_ios - five_android)

    options = five_android.union(five_ios)
    positions = random_selection(options, k=10)

    print("BUS SCENARIO ---------------------")
    print(f"Positons = {positions}")
    print(f"Walking person = {walking_person}")
    print("")


def train_platform(label="TRAIN SCENARIO"):
    for i in range(1, 7):
        five_android = random.sample(android, k=5)
        five_ios = random.sample(ios, k=5)
        options = five_android + five_ios

        stationary = random.sample(options, k=5)

        walking = set(options) - set(stationary)
        print(f"{label} ---------------------")
        print(f"Run {i}")
        print(f"Stationary {stationary}")
        print(f"Walking {walking}")
        print("")


def bar_scenario():
    for i in range(1, 7):
        eight_android = random.sample(android, k=8)
        seven_ios = random.sample(ios, k=7)
        print("BAR SCENARIO ---------------------")
        print(f"Run {i}")
        print(f"Walking {eight_android + seven_ios}")
        print("")


def supermarket():
    return train_platform("SUPERMARKET SCENARIO")


def grid():
    for i in range(1, 7):
        k_android = 13 if random.choice([True, False]) else 12
        k_ios = 25 - k_android
        a = random.sample(android, k=k_android)
        b = random.sample(ios, k=k_ios)
        print("GRID SCENARIO ---------------------")
        print(f'Android={k_android}, iOS={k_ios}')
        print(f"Run {i}")
        print(f"{random.sample(a + b, k=25)}")
        print("")


def park():
    for i in range(1, 7):
        print("Park SCENARIO ---------------------")
        print(f"Run {i}")
        print(f"{random.sample(all, k=2)}")
        print("")


if __name__ == '__main__':
    # bus_scenario()
    # train_platform()
    # bar_scenario()
    # supermarket()
    grid()
    # park()
