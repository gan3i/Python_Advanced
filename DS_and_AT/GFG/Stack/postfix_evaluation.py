from infixtopostfix import infix_to_postfix

def postfix_evaluation(expr):
    stack = []

    for i in expr:

        if i.isalnum():
            stack.append(i) 
        else:
            try:
                val1 = stack.pop()
                val2 = stack.pop()
                result = eval(val1 + i + val2,{'a':3},{'a':2,'b':3})# eval(expression,globals,locals)
                stack.append(str(result))
            except:
                return -1

    print(stack.pop())

postfix_evaluation(infix_to_postfix("a+(b*(4+5)+6)"))