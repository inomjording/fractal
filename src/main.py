import numpy as np
import matplotlib.pyplot as plt


class Fractal:
    def __init__(self, file_name, numits=10000):
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
        # ax.set_xlim(-4, 4)
        # ax.set_ylim(0, 100)
        ax.scatter(self.x[:self.n], self.y[:self.n], marker=".")
        plt.savefig("../figures/koch.png")
        plt.show()


def main():
    test = Fractal("../data/koch snowflake")
    print(test.data)
    print(test.data.shape)
    test.ran_it()
    test.plotting()


if __name__ == "__main__":
    main()
