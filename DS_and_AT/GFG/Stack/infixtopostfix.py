
def infix_to_postfix(expr):
        stack = []
        output = []
        precedence = {'+':1,'-':1,'*':2,'/':2,'^':3}


        for c in expr:

            if c.isalnum():
                output.append(c)

            elif c=='(':
                stack.append(c)

            elif c== ')':
                while ((not len(stack)==0) and stack[-1]!='('):
                    output.append(stack.pop())

                if ( (not len(stack)==0) and stack[-1]!='('):
                    return -1
                else:
                    stack.pop()
            else:
                while ( len(stack) != 0 and stack[-1] in precedence and precedence[c] <= precedence[stack[-1]]):
                    output.append(stack.pop())
                stack.append(c)

        while len(stack)!= 0:
            output.append(stack.pop())

        print(*output)
        return ''.join(output)




infix_to_postfix("a+b*(c^d-e)^(f+g*h)-i")

'a b c d ^ e - f g h * + ^ * + i -'

infix_to_postfix("2+(3*(4+5)+6)")



            

                

