import operator as op
import re


def splitter(exp):
    '''splits string into tokens'''
    return re.findall(r'[+-/()\*\^]|\d+', exp)


def infix_postfix(tokens):
    ops = ['+', '-', '*', '/', '^']
    prec = {
        '^': 2, 
        "+": 0, 
        "-": 0, 
        "*": 1,
        "/": 1, 
        '(': -1
    }
    output = []
    stack = []
    for item in tokens:
        #operator check
        if item in ops:
            #adds operators from the operator stack to the
            #output stack until
            # 1) operator stack is empty
            # 2) the precendence of the topmost operator
            #    in the operator stack is greater than or equal
            #    to that of the current operator
            while stack and prec[stack[-1]] >= prec[item]:
                output.append(stack.pop())
            #append the current operator to the operator stack
            stack.append(item)
        
        #parenthesis detection
        elif item == "(":
            stack.append("(")
        
        #if parenthesis has to be closed:
        elif item == ")":
            #emptys operator stack to the oupt stack until:
            # 1) the operator stack is empty
            # 2) the topmost operator in the stack is a '('
            while stack and stack[-1] != "(":
                output.append(stack.pop())
            
            #the '(' is removed, it is not needed in the rpn expression
            stack.pop()
        
        #not operator or parenthesis
        else:
            #appends to output stack
            output.append(item)
    
    #precedence order has been maintained
    while stack:
        #empties stack into ouput stack until
        #the ouptut stack is empty
        output.append(stack.pop())
    return output

exp = "2 + ( 3 - 5 )"

class Function:
    def __init__(self, n, func):
        self._n = n
        self._func = func

    def getn(self):
        '''
        returns the number of operands it operates on
        not necessary for this example
        maybe when binary and unary operators are mixed'''
        return self._n

    def getfn(self):
        return self._func

func = {
    '+': Function(2, op.add),
    '-': Function(2, op.sub),
    '*': Function(2, op.mul),
    '/': Function(2, op.truediv),
    '^': Function(2, op.pow),
}

def evaluate(exp):
    stack = []
    '''works just like taught in class'''
    for atom in exp:
        if atom in func.keys():
            operand1 = stack.pop()
            operand2 = stack.pop()

            stack.append(func[atom].getfn()(operand2, operand1))

        else:
            stack.append(float(atom))

    return stack.pop()

exp = input()
print(evaluate(infix_postfix(splitter(exp))))
