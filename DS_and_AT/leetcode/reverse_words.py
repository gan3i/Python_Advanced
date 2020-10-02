def reverseWords(s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if s is None or len(s)==0:
            return
        stack = s
        l = len(s)
        i = 0
        while i <l :
            stack.append(s[i])
            i += 1
        j = 0

        # this will not work.
        stack2 = []
        while len(stack)>0:
            current = stack.pop()
            if current == ' ':
                while len(stack2)>0:
                    s[j] = stack2.pop()
                    j +=1
                s[j] = ' '
                j +=1
            else:
                stack2.append(current)
                    
        while len(stack2):
            s[j] = stack2.pop()
            j +=1
        

s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]

reverseWords(s)