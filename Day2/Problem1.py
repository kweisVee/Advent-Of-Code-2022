class RockPaperScissors: 

    def __init__(self) -> None:

        self.arrayInput = []

        self.opponent = {
            "A":"Rock",
            "B":"Paper",
            "C":"Scissors"
        }

        self.player = {
            "X":["Rock", 1],
            "Y":["Paper", 2],
            "Z":["Scissors", 3]
        }

        # you just need the win, since if it's lose you don't need to add anything
        self.result = {
            "Rock": "Scissors",
            "Paper": "Rock",
            "Scissors": "Paper"
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
            p = self.player[j][0]

            nSum += self.player[j][1]
            if o == p: 
                nSum += 3
            elif o == self.result[p]: 
                nSum += 6

        return nSum

rockPaperScissors = RockPaperScissors()
res = rockPaperScissors.solution("input.txt")
print(res)