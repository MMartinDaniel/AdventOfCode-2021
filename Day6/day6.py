file = open("day6_input.txt", "r")

from collections import deque

class LanternFishCounter():
    fishes = []
    day = 0
    fishes = deque([0,0,0,0,0,0,0,0,0])

    def __init__(self, fishes):
        for fish in fishes: self.fishes[int(fish)] += 1

    def pass_day(self):
        self.should_spawn()
        self.fishes.rotate(-1)
        self.day += 1

    def should_spawn(self):
        if self.fishes[0] != 0:
            total_to_spawn = self.fishes[0]
            self.fishes[7] += total_to_spawn

    def count_fishes(self):
        total = 0
        for i in range(9):
            total += self.fishes[i]
        print(f'Day {self.day}, total fishes: {total}')

fishes = []

for line in file: fishes = line.split(',')

lanternFishCounter = LanternFishCounter(list(map(int, fishes)))
lanternFishCounter.count_fishes()

for day in range(256):
    lanternFishCounter.pass_day()
    lanternFishCounter.count_fishes()




