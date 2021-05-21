import matplotlib.pyplot as plt

class LinearCongruentialMethod:
    m = 2 ** 32
    a = 1103515245
    c = 12345

    def rand(self, x):
        return (self.a * x + self.c) % self.m

class Mean:
    _sum = 0
    count = 0
    meanList = []
    def mean(self, num):
        self._sum += num
        self.count += 1
        self.meanList.append(self._sum / self.count)
    def meanGets(self):
        return self.meanList

if __name__ == "__main__":
    LCM = LinearCongruentialMethod()
    Mean = Mean()
    print("시드 : ")
    seedNum = int(input())
    print("난수 개수 : ")
    repeat = int(input())
    randList = []
    for i in range(0, repeat):
        seedNum = LCM.rand(seedNum)
        Mean.mean(seedNum)
        randList.append(seedNum)
        print(seedNum)
    mean = Mean.meanGets()
    print("평균 : " + str(mean))

    #시각화
    plt.hist(randList, bins=10)
    plt.show()

    plt.plot(mean)
    plt.show()
