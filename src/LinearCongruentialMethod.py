m = 2 ** 32;
a = 1103515245;
c = 12345;

def rand(x):
    return (a * x + c) % m
  
print("시드 : ")
seedNum = int(input())
print("난수 개수 : ")
repeat = int(input())
randList = []
for i in range(0, repeat):
    seedNum = rand(seedNum)
    randList.append(seedNum)
    print(seedNum)
