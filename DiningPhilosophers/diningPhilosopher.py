import threading
import random
import time


class Philosophers(threading.Thread):
    running = True

    def __init__(self, xname, leftfork, rightfork):
        threading.Thread.__init__(self)
        self.name = xname
        self.leftfork = leftfork
        self.rightfork = rightfork

    def run(self):
        while self.running:
            time.sleep(random.uniform(3, 13))
            print("{} is hungry.".format(self.name))
            self.dine()

    def dine(self):
        fork1, fork2 = self.leftfork, self.rightfork

        while self.running:
            fork1.acquire(True)
            locked = fork2.acquire(False)
            if locked: break
            fork1.release()
            print("{} swaps forks.".format(self.name))
            fork1, fork2 = fork2, fork1
        else:
            return

        self.dining()
        fork2.release()
        fork1.release()

    def dining(self):
        print("{} starts eating. ".format(self.name))
        time.sleep(random.uniform(1, 10))
        print("{} finished eating and now thinking. ".format(self.name))


def DiningPhilosophers():
    fork = [threading.Lock() for i in range(5)]
    names = ('A', 'B', 'C', 'D', 'E',)
    philo = [Philosophers(names[i], fork[i % 5], fork[(i + 1) % 5]) for i in range(5)]
    random.seed(501312)
    Philosophers.running = True
    for p in philo: p.start()
    time.sleep(100)
    Philosophers.running = False
    print("Finishing")

DiningPhilosophers()


