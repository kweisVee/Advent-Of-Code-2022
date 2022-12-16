from string import ascii_lowercase

class TuningTrouble: 

    def __init__(self) -> None:
        self.dict = {}

    def setArray(self): 
        for c in ascii_lowercase: 
            self.dict[c] = 0
    
    def checkDuplicates(self): 
        for c in ascii_lowercase: 
            if self.dict[c] > 1: 
                return False
        return True
    
    # BUT ANOTHER OPTION IS TO JUST TREAT IT AS A SET 
    # THEN CHECK LENGTH IF EQUAL TO 4!! GRRR 
    def problem1(self, string): 
        start, end = 0, 3
        for i in range(start, end+1): 
            letter = string[i]
            self.dict[letter] += 1

        if self.checkDuplicates(): 
            return end+1

        while True: 
            start_letter = string[start]
            self.dict[start_letter] -= 1

            start += 1
            end += 1

            end_letter = string[end]
            self.dict[end_letter] += 1
            if self.checkDuplicates(): 
                return end + 1
    
    def problem2(self, string): 
        start, end = 0, 13
        for i in range(start, end+1): 
            letter = string[i]
            self.dict[letter] += 1

        if self.checkDuplicates(): 
            return end+1

        while True: 
            start_letter = string[start]
            self.dict[start_letter] -= 1

            start += 1
            end += 1

            end_letter = string[end]
            self.dict[end_letter] += 1
            if self.checkDuplicates(): 
                return end + 1
        

with open("input.txt") as f: 
    inputStr = f.read()
    # print("INPUT STRING", inputStr)

tt = TuningTrouble()
tt.setArray()
res1 = tt.problem1(inputStr)
print("res1:", res1)

tt.setArray()
res2 = tt.problem2(inputStr)
print("res2:", res2)

