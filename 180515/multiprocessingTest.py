import multiprocessing
from multiprocessing.managers import BaseManager, NamespaceProxy


class Counter(object):
    def __init__(self):
        self.value = 0

    def update(self, value):
        self.value += value



def main():
    manager = BaseManager()
    manager.start()
	
    counter = manager.Counter()



if __name__ == "__main__":
    main()
