class CalorieCounting: 
    def solution(self, fileName): 
        f = open(fileName, "r")
        res = float("-inf")
        nSum = 0
        i = 1
        for line in f:
            if line == "\n": 
                res = max(nSum, res)
                i += 1
                nSum = 0
            else: 
                nSum += int(line)
        return res


cc = CalorieCounting()
print(cc.solution("input.txt"))