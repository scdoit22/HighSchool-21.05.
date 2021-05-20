"""
융합 탐구 학술제
구현 - 이도연
"""
class MidSquareMethod: # 중앙제곱법
    outNumLength = 0 #얻고자 하는 난수의 자릿수
    seedNum = 0

    def __init__(self):
        print("난수 자릿수 : ")
        self.outNumLength = int(input())
        print("시드 : ")
        self.seedNum = int(input())

    def createRandNum(self):
        num = self.seedNum ** 2
        num = MidSquareMethod.centerString(self, str(num))
        self.seedNum = int(num)
        return num #반환은 문자열으로 <- 맨 앞자리 '0'을 출력하기 위해서

    def centerString(self, s):
        stringLength = len(s)
        if stringLength % 2 == 1:
            return s[(stringLength - self.outNumLength - 1) // 2 : stringLength - ((stringLength - self.outNumLength + 1) // 2)]
        else:
            return s[(stringLength - self.outNumLength) // 2 : stringLength - ((stringLength - self.outNumLength) // 2)]
if __name__ == "__main__":
    MS = MidSquareMethod()
    randNum = 0
    print("난수 개수 : ")
    repeat = int(input())

    for i in range(1, repeat):
        randNum = MS.createRandNum()
        print(randNum)
