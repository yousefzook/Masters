from turtle import *
from random import randrange
from freegames import square, vector

import time
import random
import numpy as np


class Solver:
    def __init__(self):
        self.timesheet = [True, True, True, True, True, True, True, True, False, False, False, False, False, False, False, False, False, True, True, True, True, True, True, False, False, False, False, False, False, True, True, True, True, True, True, True, True, False, False, False, False, False, False, True, True, True, True, True, True, False, False, False, False, False, False, True, True, True, True, True, True, False, False, False, False, False, False, True, True, True, True, True, True, False, False, False, False, False, False, False, False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]
        self.north = [[2, 2, 2, 1, 2, 0, 0, 1, 1, 2, 0, 0, 1, 3, 2, 0, 2, 3, 1, 3, 4, 2, 3, 4, 2, 3, 1, 2, 4, 0, 4, 0, 0, 1, 1, 0, 4, 1, 1, 3, 2, 0, 4, 0, 3, 4, 4, 2, 1, 2, 4, 0, 3, 3, 2, 3, 4, 4, 2, 0, 3, 0, 0, 4, 1, 2, 4, 4, 0, 2, 3, 4, 3, 3, 2, 4, 4, 1, 4, 2, 4, 4, 3, 10, 6, 2, 10, 1, 10, 4, 4, 1, 0, 5, 0, 0, 10, 20, 1, 2], [
            2, 2, 1, 3, 1, 1, 1, 1, 3, 4, 3, 1, 1, 5, 3, 2, 2, 4, 4, 3, 2, 3, 6, 4, 6, 4, 2, 3, 5, 5, 1, 4, 1, 1, 2, 2, 3, 5, 1, 5, 1, 3, 4, 3, 1, 8, 9, 3, 1, 3, 6, 4, 2, 3, 6, 1, 4, 2, 6, 1, 1, 3, 1, 5, 1, 1, 5, 7, 4, 1, 3, 8, 6, 2, 1, 1, 3, 1, 5, 5, 2, 4, 2, 4, 2, 1, 4, 2, 1, 5, 2, 1, 2, 10, 1, 1, 10, 3, 4, 3]]
        self.south = [[3, 1, 3, 1, 2, 4, 1, 0, 4, 3, 2, 4, 4, 2, 1, 3, 4, 1, 3, 2, 0, 3, 1, 1, 2, 4, 1, 4, 0, 3, 0, 2, 0, 2, 4, 2, 0, 3, 4, 2, 1, 1, 2, 0, 4, 4, 2, 2, 2, 0, 2, 1, 2, 1, 2, 2, 2, 2, 0, 1, 0, 4, 2, 1, 2, 2, 2, 0, 1, 2, 1, 4, 1, 0, 1, 3, 4, 3, 0, 0, 0, 1, 1, 0, 0, 0, 10, 1, 12, 10, 4, 2, 2, 10, 2, 2, 15, 4, 4, 4], [
            3, 4, 5, 1, 3, 3, 1, 1, 5, 7, 1, 4, 9, 5, 3, 1, 2, 4, 4, 1, 1, 3, 2, 2, 3, 7, 3, 5, 3, 4, 1, 2, 2, 1, 5, 1, 2, 1, 7, 7, 1, 2, 4, 2, 5, 7, 6, 2, 4, 1, 1, 1, 1, 4, 1, 3, 1, 5, 2, 2, 2, 3, 2, 2, 1, 1, 5, 2, 2, 2, 2, 6, 4, 2, 1, 4, 3, 7, 1, 1, 1, 1, 3, 2, 1, 1, 1, 3, 3, 1, 1, 4, 3, 12, 4, 10, 2, 3, 1, 9]]
        self.east = [[3, 2, 0, 4, 3, 4, 0, 1, 2, 3, 1, 4, 2, 2, 2, 0, 2, 4, 0, 1, 4, 4, 2, 0, 0, 3, 0, 0, 1, 4, 4, 4, 1, 0, 1, 4, 1, 4, 2, 4, 4, 1, 0, 3, 3, 2, 2, 3, 1, 0, 2, 3, 3, 2, 3, 2, 0, 2, 2, 0, 4, 1, 4, 3, 0, 3, 3, 0, 0, 0, 3, 0, 3, 4, 2, 0, 3, 4, 2, 4, 2, 4, 4, 1, 1, 1, 3, 2, 1, 3, 0, 2, 1, 2, 0, 4, 2, 2, 0, 4], [
            4, 3, 2, 4, 6, 8, 4, 1, 2, 3, 3, 1, 2, 5, 3, 3, 1, 7, 4, 1, 1, 5, 7, 1, 1, 4, 4, 1, 2, 4, 1, 5, 6, 2, 2, 3, 5, 4, 5, 7, 2, 1, 1, 3, 5, 1, 2, 5, 2, 2, 1, 4, 6, 6, 5, 2, 3, 2, 5, 1, 1, 2, 5, 6, 1, 1, 3, 3, 1, 1, 3, 2, 4, 7, 1, 3, 4, 4, 7, 5, 5, 3, 1, 2, 2, 1, 2, 6, 1, 3, 4, 1, 2, 2, 2, 4, 7, 2, 2, 3]]
        self.west = [[3, 3, 4, 2, 0, 2, 3, 1, 1, 1, 2, 1, 1, 0, 2, 3, 4, 3, 0, 2, 1, 3, 4, 2, 2, 4, 2, 1, 1, 1, 3, 2, 0, 4, 1, 0, 4, 4, 3, 3, 2, 2, 1, 2, 4, 3, 1, 4, 1, 0, 3, 3, 1, 0, 1, 0, 1, 1, 1, 3, 3, 1, 3, 2, 2, 4, 1, 0, 4, 2, 4, 4, 4, 3, 0, 1, 2, 4, 2, 1, 0, 0, 2, 0, 1, 0, 3, 3, 4, 2, 1, 3, 1, 1, 3, 4, 3, 4, 4, 0], [
            2, 4, 6, 6, 1, 1, 1, 4, 2, 1, 2, 1, 1, 1, 2, 4, 8, 1, 4, 2, 1, 5, 7, 3, 3, 7, 2, 2, 1, 3, 4, 5, 2, 4, 4, 2, 5, 1, 3, 1, 2, 2, 4, 1, 3, 7, 1, 6, 3, 2, 2, 3, 4, 2, 2, 1, 1, 2, 1, 2, 4, 1, 2, 5, 3, 4, 2, 1, 4, 5, 3, 8, 5, 7, 3, 1, 3, 2, 5, 4, 2, 1, 2, 3, 1, 1, 3, 6, 3, 1, 2, 1, 2, 2, 1, 4, 4, 6, 9, 5]]
        self.counter = -1
        # self.timesheet = [True, True, True, True, True, True, True, True, False, False, False, False, False, False, False, False, True, True, True, True, True, True, False, False, False, False, False, False, False, False, True, True, True, True, True, True, True, False, False, False, False, False, False, False, True, True, True, True, True,
        #                   True, True, True, True, False, False, False, False, False, False, True, True, True, True, True, True, True, False, False, False, False, False, False, True, True, True, True, True, True, False, False, False, False, False, False, True, True, True, True, True, True, True, False, False, False, False, False, False, False, False, True]
        # self.north = [[2, 2, 2, 3, 2, 0, 4, 3, 2, 3, 1, 2, 3, 3, 2, 4, 1, 1, 2, 0, 3, 4, 2, 3, 3, 3, 1, 3, 3, 3, 4, 4, 3, 2, 0, 1, 1, 4, 1, 2, 0, 0, 4, 1, 0, 0, 3, 4, 0, 0, 0, 2, 1, 1, 0, 1, 1, 3, 0, 0, 4, 1, 0, 4, 1, 2, 2, 2, 3, 1, 4, 0, 3, 0, 2, 2, 3, 0, 1, 4, 0, 1, 0, 4, 1, 2, 1, 4, 4, 1, 2, 2, 0, 3, 0, 1, 2, 4, 1, 3], [
        #     6, 1, 4, 4, 1, 3, 2, 6, 3, 6, 1, 1, 2, 1, 1, 5, 6, 2, 3, 3, 1, 6, 3, 4, 4, 2, 2, 1, 6, 7, 7, 1, 4, 2, 2, 1, 2, 4, 6, 1, 1, 1, 1, 6, 2, 1, 1, 1, 5, 1, 1, 3, 4, 3, 1, 2, 2, 2, 1, 1, 4, 6, 2, 3, 5, 1, 1, 4, 2, 3, 6, 2, 1, 3, 2, 5, 3, 4, 1, 1, 3, 1, 2, 2, 3, 2, 4, 3, 4, 6, 4, 5, 1, 3, 2, 2, 2, 5, 3, 4]]
        # self.south = [[2, 4, 0, 1, 0, 1, 0, 0, 4, 2, 3, 4, 1, 3, 4, 4, 4, 1, 1, 4, 1, 1, 3, 3, 0, 1, 2, 2, 4, 4, 0, 3, 4, 1, 0, 1, 3, 2, 2, 0, 1, 3, 2, 2, 3, 3, 3, 4, 1, 1, 4, 4, 2, 0, 4, 2, 0, 0, 0, 4, 0, 2, 0, 3, 0, 2, 4, 0, 3, 1, 1, 1, 3, 4, 2, 3, 1, 4, 2, 3, 0, 4, 3, 0, 0, 1, 1, 0, 4, 1, 1, 3, 3, 4, 3, 1, 3, 0, 4, 0], [
        #     3, 6, 4, 2, 1, 1, 2, 1, 5, 3, 6, 8, 2, 4, 6, 8, 1, 6, 1, 1, 2, 1, 3, 3, 1, 1, 2, 5, 4, 1, 2, 2, 8, 3, 1, 2, 1, 6, 2, 1, 2, 2, 5, 3, 3, 2, 3, 4, 2, 1, 5, 1, 4, 1, 4, 7, 2, 1, 1, 3, 2, 2, 1, 4, 3, 3, 2, 4, 1, 1, 3, 1, 1, 2, 2, 3, 1, 1, 5, 3, 3, 1, 3, 3, 1, 2, 1, 1, 3, 6, 2, 3, 6, 8, 5, 2, 4, 2, 4, 4]]
        # self.east = [[3, 2, 1, 1, 0, 3, 4, 3, 3, 1, 4, 3, 4, 0, 2, 0, 2, 2, 2, 0, 1, 1, 1, 3, 4, 0, 1, 3, 0, 1, 4, 4, 0, 1, 0, 4, 1, 0, 4, 0, 0, 3, 1, 2, 2, 2, 2, 4, 3, 4, 4, 3, 3, 0, 4, 2, 0, 0, 0, 2, 0, 4, 0, 1, 1, 3, 3, 1, 0, 1, 0, 1, 2, 2, 2, 0, 4, 3, 2, 0, 4, 3, 1, 0, 1, 2, 0, 1, 0, 0, 3, 4, 2, 4, 0, 0, 4, 0, 2, 0], [
        #     4, 2, 1, 1, 2, 1, 3, 4, 1, 2, 1, 1, 1, 3, 2, 3, 2, 3, 3, 3, 1, 3, 2, 4, 3, 1, 2, 4, 1, 1, 6, 8, 5, 1, 1, 2, 4, 2, 1, 4, 1, 4, 4, 4, 5, 3, 1, 6, 8, 6, 9, 5, 5, 2, 2, 4, 2, 1, 1, 3, 3, 5, 3, 1, 3, 2, 1, 4, 1, 1, 1, 2, 2, 3, 3, 1, 3, 5, 1, 2, 5, 3, 4, 2, 2, 1, 3, 1, 1, 1, 2, 4, 1, 5, 3, 1, 1, 1, 2, 3]]
        # self.west = [[3, 2, 1, 0, 4, 1, 4, 4, 3, 0, 1, 1, 2, 0, 0, 4, 4, 0, 3, 1, 1, 3, 1, 2, 2, 4, 1, 0, 1, 3, 2, 0, 4, 2, 3, 3, 2, 2, 0, 3, 1, 1, 0, 0, 4, 4, 3, 1, 4, 1, 1, 2, 2, 1, 2, 1, 3, 2, 3, 0, 4, 2, 2, 1, 1, 0, 0, 0, 3, 3, 1, 2, 4, 0, 2, 3, 4, 1, 1, 0, 4, 1, 3, 1, 4, 3, 2, 1, 2, 4, 3, 4, 3, 0, 0, 3, 4, 0, 4, 3],
        #              [5, 4, 2, 2, 2, 5, 1, 3, 3, 1, 2, 3, 1, 2, 1, 5, 5, 4, 1, 5, 3, 4, 1, 4, 3, 5, 3, 2, 2, 1, 4, 2, 1, 7, 5, 2, 6, 3, 2, 1, 4, 2, 1, 1, 2, 9, 5, 2, 3, 5, 3, 1, 3, 1, 2, 1, 2, 2, 2, 1, 3, 3, 4, 1, 1, 2, 1, 1, 4, 7, 5, 1, 5, 5, 2, 5, 5, 2, 3, 2, 2, 1, 5, 2, 4, 8, 2, 3, 1, 2, 5, 1, 8, 1, 1, 3, 1, 2, 2, 8]]
        self.counter = -1

    def solve(self):
        if self.counter == len(self.timesheet)-1:
            return None
          # self.counter = -1
        self.counter += 1
        return self.timesheet[self.counter], self.north[0][self.counter], self.north[1][self.counter], self.south[0][self.counter], self.south[1][self.counter], self.east[0][self.counter], self.east[1][self.counter], self.west[0][self.counter], self.west[1][self.counter]


def mergeS1234(S1, S2):
    return np.concatenate((S1, S1), axis=1)


def K_fn(A, B, p1, p2):
    B1 = B[:, 0:1]
    B2 = B[:, 1:2]
    k1 = np.matmul(
        np.matmul([[0, 1]], np.linalg.inv(M(A, B1))), alpha(A, p1, p2))
    k2 = np.matmul(
        np.matmul([[0, 1]], np.linalg.inv(M(A, B2))), alpha(A, p1, p2))
    return np.concatenate((k1, k2), axis=0)


def alpha(A, p1, p2):
    return np.matmul(A, A) + (-p1-p2)*A + (p1*p2)*np.identity(2)


def M(A, B):  # [B AB]
    return np.concatenate((B, np.matmul(A, B)), axis=1)


def Q_n1(Q_n, q_n, d_n, S_n):
    return Q_n + q_n - np.matmul(d_n, S_n)


def W_n1(W_n,  Q_n, q_n, d_n, S_n, T=1):
    return W_n + T*Q_n + 0.5*T*q_n - 0.5*T*np.matmul(d_n, S_n)


def A_fn(T):
    return np.array([[1, 0], [T, 1]])


def B_fn(d, T):
    return np.array([[-d[0][0]-d[1][0], -d[0][1]-d[1][1]],
                     [-0.5*T*d[0][0]-0.5*T*d[1][0], -0.5*T*d[0][1]-0.5*T*d[1][1]]])


def C_fn(q, T):
    return np.transpose(np.array([[T*(q[0][0]+q[1][0]), T*(q[0][1]+q[1][1])]]))


def X_n(Q, W):
    return np.transpose(np.array([[(Q[0][0] + Q[1][0] - Q[0][1] - Q[1][1]),
                                   (W[0][0] + W[1][0] - W[0][1] - W[1][1])]]))


def X_n1(X_n, S_n, A, B, C):
    return np.matmul(A, X_n) + np.matmul(B, S_n) + C


class Simulation:
    def __init__(self, solver):
        self.left = vector(-100, 0)
        self.right = vector(100, 0)
        self.bottom = vector(0, -100)
        self.top = vector(0, 100)
        self.isNorSou = True
        self.solver = solver
        self.n1 = 0
        self.n2 = 0
        self.s1 = 0
        self.s2 = 0
        self.e1 = 0
        self.e2 = 0
        self.w1 = 0
        self.w2 = 0

    # def hide(self, element=left):
    #   clear()
    #   if element != self.left:
    #     square(self.left.x, self.left.y, 20, 'green')
    #   if element != self.right:
    #     square(self.right.x, self.right.y, 20, 'green')

    #   if element != self.bottom:
    #     square(self.bottom.x, self.bottom.y, 20, 'red')
    #   if element != self.top:
    #     square(self.top.x, self.top.y, 20, 'red')

    def draw(self):
        clear()
        if not self.isNorSou:
            square(self.left.x, self.left.y, 20, 'green')
            self.drawNumbers(self.w1, self.e2)
            square(self.right.x, self.right.y, 20, 'green')
            self.drawNumbers(self.e1, self.w2)
            self.drawTotalEW(self.e1+self.w1, self.e2+self.w2)

            square(self.bottom.x, self.bottom.y, 20, 'red')
            self.drawNumbers(self.s1, self.n2)
            square(self.top.x, self.top.y, 20, 'red')
            self.drawNumbers(self.n1, self.s2)
            self.drawTotalNS(self.n1+self.s1, self.n2+self.s2)
        else:
            square(self.left.x, self.left.y, 20, 'red')
            self.drawNumbers(self.w1, self.e2)
            square(self.right.x, self.right.y, 20, 'red')
            self.drawNumbers(self.e1, self.w2)
            self.drawTotalEW(self.e1+self.w1, self.e2+self.w2)

            square(self.bottom.x, self.bottom.y, 20, 'green')
            self.drawNumbers(self.s1, self.n2)
            square(self.top.x, self.top.y, 20, 'green')
            self.drawNumbers(self.n1, self.s2)
            self.drawTotalNS(self.n1+self.s1, self.n2+self.s2)
        update()

    def drawTotalEW(self, input, output):
        forward(100)
        write('in_tot:' + str(input), False,
              align="center", font=("Arial", 10, "bold"))
        forward(60)
        write('out_tot:' + str(output), False,
              align="center", font=("Arial", 10, "bold"))

    def drawTotalNS(self, input, output):
        forward(100)
        write('in_tot:' + str(input), False,
              align="center", font=("Arial", 10, "bold"))
        forward(60)
        write('out_tot:' + str(output), False,
              align="center", font=("Arial", 10, "bold"))
        right(180)
        forward(160)
        right(180)

    def drawNumbers(self, input, output):
        hideturtle()
        right(90)
        forward(50)
        write('in:' + str(input), False, align="center",
              font=("Arial", 15, "bold"))
        left(180)
        forward(100)
        write('out:' + str(output), False,
              align="center", font=("Arial", 15, "bold"))
        right(180)
        forward(50)
        left(90)

    def start(self):
        self.draw()
        ontimer(self.start, 200)
        temp = self.solver.solve()
        if(temp is None):
            return
        (self.isNorSou, self.n1, self.n2, self.s1, self.s2,
         self.e1, self.e2, self.w1, self.w2) = temp
        # print(n1, n2, e1, e2, s1, s2, w1, w2)


setup(820, 400, 370, 0)
hideturtle()
tracer(False)
solver = Solver()
x = Simulation(solver)
x.start()
done()
