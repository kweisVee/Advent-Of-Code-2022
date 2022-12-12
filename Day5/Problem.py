import re


class SupplyStacks: 

    def insertInStacks(self, input): 
        indexes = [index for index, char in enumerate(input[-1]) if char != " "]
        stacks = {int(digit):[] for digit in input[-1].replace(" ", "")}

        for line in input[:-1]: 
            stackNum = 1
            for i in indexes: 
                if line[i] != " ": 
                    stacks[stackNum].insert(0, line[i])
                stackNum += 1
        return stacks
    
    def getInstructions(self, instructions): 
        arr = []
        for i in instructions: 
            num, get, idx = map(int, re.findall(r"\d+", i))
            arr.append([num, get, idx])
        return arr
    
    def getString(self, stacks): 
        string = ""
        for key in stacks:
            string += stacks[key][-1]
        return string

    def solution1(self, stacks, instructions): 
        for line in instructions: 
            for i in range(line[0]): 
                letter = stacks[line[1]].pop()
                stacks[line[2]].append(letter)
        return self.getString(stacks)
    
    def solution2(self, stacks, instructions): 
        for line in instructions: 
            array = stacks[line[1]][-line[0]:]
            # replacing the array with the removed arrays
            stacks[line[1]] = stacks[line[1]][:-line[0]]
            for e in array: 
                stacks[line[2]].append(e)
        return self.getString(stacks)


with open("input.txt") as f: 
    inputStr, instructions = (i.splitlines() for i in f.read().strip("\n").split("\n\n"))

ss = SupplyStacks()
stacks = ss.insertInStacks(inputStr)
instructions = ss.getInstructions(instructions)
res1 = ss.solution1(stacks, instructions)
print(f"Solution 1: {res1}")
stacks = ss.insertInStacks(inputStr)
res2 = ss.solution2(stacks, instructions)
print(f"Solution 2: {res2}")