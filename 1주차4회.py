import sys
num_of_strings = int(sys.stdin.readline())

stack = []

for x in range (num_of_strings):
    string = input()
    for char in string:
        if char == "(":
            stack.append(char)
        else:
            if len(stack) == 0:
                print('NO')
            stack.pop()
        print ("YES")

