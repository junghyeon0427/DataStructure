T = int(input())

for i in range(T):
    string = input()
    left_stk = list()
    right_stk = list()
    for j in string:
        if j == '<':
            if left_stk:
                right_stk.append(left_stk.pop())
                
        elif j == '>':
            if right_stk:
                left_stk.append(right_stk.pop())
                
        elif j == '-':
            if left_stk:
                left_stk.pop()
        else:
            left_stk.append(j)
    
    print(''.join(left_stk + right_stk[::-1]))
