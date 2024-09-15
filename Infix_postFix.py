operators = set(['+', '-', '*', '/', '(', ')', '^']) # collection of operators
priority = {'+':1, '-':1, '*':2, '/':2, '^':3} # dictionary having priorities of operators

def infix_to_postfix(expression):
    stack = [] # initialization of empty stack
    output = ''
    for character in expression:
        if character not in operators: # if an operand append in postfix expression
            output += character
        elif character == '(': # else operators push onto stack
            stack.append('(')
        elif character == ')':
            while stack and stack[-1] != '(':
                output += stack.pop()
            stack.pop()
        else:
            while stack and stack[-1] != '(' and priority[character] <= priority[stack[-1]]:
                output += stack.pop()
            stack.append(character)
    while stack:
        output += stack.pop()
    return output

expression = input('Enter infix expression: ')
print('Infix notation: ', expression)
print('Postfix notation: ', infix_to_postfix(expression))


# OUTPUT:
# ==================== RESTART: C:/Users/DELL/Desktop/pr3b.py ====================
# Enter infix expression m*n+(p-q)+r
# infix notation: m*n+(p-q)+r
# postfix notation: mn*pq-+r+
# ==================== RESTART: C:/Users/DELL/Desktop/pr3b.py ====================
# Enter infix expression (a+(c+d*f+t*a)*b/c)
# infix notation: (a+(c+d*f+t*a)*b/c)
# postfix notation: acdf*+ta*+b*c/+