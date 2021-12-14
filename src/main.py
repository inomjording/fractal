import numpy as np
import matplotlib.pyplot as plt
import os
from numpy import sin, cos, arctan, pi, absolute


class Fractal:
    def __init__(self, file_name, numits=10000):
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
        plt.scatter(self.x[:self.n], self.y[:self.n], marker=".", c='k')
        plt.savefig("../figures/{0}.png".format(self.name))
        plt.show()

    def scale(self, k):
        if self.data[k, 0] == 0.:
            return self.data[k, 2]
        elif self.data[k, 2] == 0.:
            return self.data[k, 0]
        else:
            x = arctan(self.data[k, 2]/self.data[k, 0])
            while True:
                r = self.data[k, 2]/sin(x)
                s = self.data[k, 0]/cos(x)
                print(absolute(s - r))
                if absolute(s - r) <= 0.0001:
                    return s
                else:
                    x += pi/2

    def fractal_dim(self):
        return

    def box_count(self, res):
        x_min = np.amin(self.x)
        x_max = np.amax(self.x)
        y_min = np.amin(self.y)
        y_max = np.amax(self.y)
        step = min(abs(x_max - x_min)/res, abs(y_max - y_min)/res)
        boxes = 0
        box_total = 0
        x_pos = x_min
        y_pos = y_min
        while x_pos < x_max:
            i = 0
            x_indices = []
            for x_coordinate in self.x:
                if np.logical_and(x_coordinate >= x_pos, x_coordinate < x_pos + step):
                    x_indices.append(i)
                i += 1
            while y_pos < y_max:
                for j in x_indices:
                    if np.logical_and(self.y[j] >= y_pos, self.y[j] < y_pos + step):
                        boxes += 1
                        break
                box_total += 1
                y_pos += step
            x_pos += step
            y_pos = y_min
        return boxes, box_total


def main():
    test = Fractal("../data/tree")
    print(test.data)
    print(test.data.shape)
    print(test.scale(2))
    test.ran_it()
    print(test.box_count(10))
    test.plotting()


if __name__ == "__main__":
    main()
