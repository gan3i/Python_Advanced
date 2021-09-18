
def hamming_distance(x: int, y: int) -> int:
    '''
    001
    100
    
    '''
    count = 0
    
    while x or y:
        x_lsb = x & 1 # 0
        y_lsb = y & 1 # 1
        
        count += (x_lsb ^ y_lsb)
        
        x >>=1
        y >>=1
        
    return count

print(hamming_distance(1, 4))