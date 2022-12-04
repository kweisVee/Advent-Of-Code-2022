import heapq

class CalorieCounting:

    def __init__(self) -> None:
        self.topThree = []

    def getTotal(self):
        nSum = 0 
        for i in self.topThree: 
            nSum += i
        return nSum

    def solution(self, fileName): 
        f = open(fileName, "r")
        nSum = 0
        i = 1
        for line in f:
            if line == "\n": 
                if len(self.topThree) == 3:
                    heapq.heappushpop(self.topThree, nSum)
                else: 
                    heapq.heappush(self.topThree, nSum)
                i += 1 
                nSum = 0
            else: 
                nSum += int(line)
        return self.getTotal()


cc = CalorieCounting()
print(cc.solution("input.txt"))