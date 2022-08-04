import numpy as np


class MyImage:
    def __init__(self, height=0, length=0):
        self.height = height
        self.length = length
        self.array1 = np.zeros([height, length, 3], dtype=np.uint8)
        self.array2 = np.zeros([height, length, 3], dtype=np.uint8)
        self.array3 = np.zeros([height, length, 3], dtype=np.uint8)
        self.array4 = np.zeros([height, length, 3], dtype=np.uint8)
        self.array5 = np.zeros([height, length, 3], dtype=np.uint8)

    def setArray(self, array):
        self.array5 = array

    def getArray1(self):
        return self.array1

    def getArray2(self):
        return self.array2

    def getArray3(self):
        return self.array3

    def getArray4(self):
        return self.array4

    def getArray5(self):
        return self.array5

    def pixelElimination(self, r=0, g=0, b=0):
        for i in range(self.height):
            for j in range(self.length):
                if self.array1[i][j][0] < r and self.array1[i][j][1] < g and self.array1[i][j][2] < b:
                    self.array1[i][j][0] = 0
                    self.array1[i][j][1] = 0
                    self.array1[i][j][2] = 0
        return self.array1

    def componentElimination(self, c):
        if c == 'r':
            for i in range(self.height):
                for j in range(self.length):
                    self.array2[i][j][0] = 0
        if c == 'g':
            for i in range(self.height):
                for j in range(self.length):
                    self.array2[i][j][1] = 0
        if c == 'b':
            for i in range(self.height):
                for j in range(self.length):
                    self.array2[i][j][2] = 0
        else:
            return self.array2

    def colorInv(self):
        for i in range(self.height):
            for j in range(self.length):
                self.array3[i][j][0] = 255 - self.array3[i][j][0]
                self.array3[i][j][1] = 255 - self.array3[i][j][1]
                self.array3[i][j][2] = 255 - self.array3[i][j][2]
        return self.array3

    def grayTone(self):
        for i in range(self.height):
            for j in range(self.length):
                self.array4[i][j] = 0.21 * self.array4[i][j][0] + 0.71 * self.array4[i][j][
                    1] + 0.07 * self.array4[i][j][2]
        return self.array4


class Pixel(MyImage):
    def __init__(self):
        super().__init__()

