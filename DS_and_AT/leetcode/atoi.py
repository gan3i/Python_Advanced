





#fuck you missed the i increment last time
def myAtoi(s: str) -> int:
        
        s = s.strip()
        
        sign = 1
        result = 0
        max_size = 2**31 -1
        ls = len(s)
        if ls == 0:
            return result
        
        if s[0] == '-':
            sign = -1
            s =s[1:]
            ls -=1
            max_size = max_size + 1
        elif s[0]== '+':
            s = s[1:]
            ls -=1
            
        if ls == 0:
            return result
        
        i = 0
        
        while i <ls:
            
            if not s[i].isdigit():
                break
            else:
                digit = int(s[i])
                if result * 10 >= max_size or result * 10 > (max_size - digit):
                    result = max_size
                    break
                else:
                    result = result * 10 + digit



        return result * sign
            
            
        
print(myAtoi("42"))