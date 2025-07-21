

# for i in range(3-1):
#     if i < 9:
#         i += 1
#         print(i+1)

#     else:
#         i = 0
#         print(i+1)
digits = [1,2,3]

class Solution:
    def plusOne(self, digits):
        
        output=[]
        num_string=""
        for i in str(digits):
            if i.isdigit():
                num_string+=i

        ans=str(int(num_string)+1)

        for j in list(ans):
            output.append(int(j))
        return output
    
obj =Solution().plusOne(digits)

print(obj)