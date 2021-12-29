import numpy as np
import matplotlib.pyplot as plt
import os


class Fractal:
    def __init__(self, file_name, numits=100000):
        self.name = os.path.basename(file_name)
        self.data = np.loadtxt(file_name)
        self.x = np.empty(numits)
        self.y = np.empty(numits)
        self.numits = numits
        self.n = 0
        self.x[0] = 0
        self.y[0] = 0

    def new_point(self, k):
        new_x = self.data[k, 0] * self.x[self.n] + self.data[k, 1] * self.y[self.n] + self.data[k, 4]
        new_y = self.data[k, 2] * self.x[self.n] + self.data[k, 3] * self.y[self.n] + self.data[k, 5]
        self.n += 1
        self.x[self.n] = new_x
        self.y[self.n] = new_y

    def ran_it(self):
        while self.n < self.numits - 1:
            k = np.random.choice(np.arange(self.data.shape[0]), p=self.data[:, -1])
            self.new_point(k)

    def plotting(self):
        fig, ax = plt.subplots()
        ax.set_title(self.name.capitalize())
        ax.set_aspect('equal', 'box')
        plt.scatter(self.x[:self.n], self.y[:self.n], marker=".", c='k', linewidths=0.1, edgecolors='c', s=1)
        plt.savefig("../figures/{0}.png".format(self.name), bbox_inches="tight")
        plt.show()


def main():
    test = Fractal("../data/branches")
    test.ran_it()
    test.plotting()


if __name__ == "__main__":
    main()
