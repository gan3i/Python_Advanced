



def are_paranthesis_balanced(expr):
    stack = []

    for c in expr:
        if c in ["(","{","["]:
            stack.append(c)
        else:
            if len(stack)==0:
                return False
            curr = stack.pop()
            if (c =="{" and curr!="}") or (c=="(" and curr!=")") or (c=="[" and curr !="]"):
                return False
            
    if stack:
        return False
    else:
        return True

print(are_paranthesis_balanced("{({}}"))

print(*[1,2,3])