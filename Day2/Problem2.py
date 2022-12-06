class RockPaperScissors: 

    def __init__(self) -> None:

        self.arrayInput = []

        self.opponent = {
            "A":"Rock",
            "B":"Paper",
            "C":"Scissors"
        }

        # order is [n will win to x, n will lose to y, points added when n is chosen]
        self.result = {
            "Rock": ["Scissors", "Paper", 1], 
            "Paper": ["Rock", "Scissors", 2], 
            "Scissors": ["Paper", "Rock", 3]
        }
    
    def createArray(self, fileName):
        f = open(fileName, "r")
        for line in f: 
            self.arrayInput.append(line.split())
        return

    def solution(self, fileName):
        self.createArray(fileName)
        
        nSum = 0

        for i, j in self.arrayInput: 
            o = self.opponent[i]

            if j == "X": 
                need = self.result[o][0]
            elif j == "Y": 
                need = o
                nSum += 3
            else: 
                need = self.result[o][1]
                nSum += 6
            nSum += self.result[need][2]

        return nSum

rockPaperScissors = RockPaperScissors()
res = rockPaperScissors.solution("input.txt")
print(res)