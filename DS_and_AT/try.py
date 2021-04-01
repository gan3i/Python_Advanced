class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n=len(A)
        even_sum=0
        odd_sum=0
        es= [0 for x in range(n)]
        os= [0 for x in range(n)]
        for i in range(n):
            if(i%2):
                odd_sum+=A[i]
            else:
                even_sum+=A[i]
            es[i]=even_sum
            os[i]=odd_sum


        c=0
        for i in range(n):
            esafter=es[n-1]-es[i]
            osafter=os[n-1]-os[i]
            if i==0 and esafter==osafter:
                c +=1
            else:
                if esafter+os[i-1]==osafter+es[i-1] :
                    c +=1

        return c

s = Solution()

print(s.solve([5, 5, 2, 5, 8]))
