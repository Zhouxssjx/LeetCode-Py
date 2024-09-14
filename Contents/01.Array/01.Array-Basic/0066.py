'''
    把数组串回整数
    给整数加一
    再按位数拆成数组
    
    直接给最后一位+1
    如果是10
    再遍历判断进位
'''

def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        """
        #向前预留一位
        digits = [0] + digits
        digits[-1] += 1
        
        index = len(digits) - 1 
        while index >= 0:
            #出现10时，前一位+1，本位变回0
            #应该从最后一位向前循环
            if digits[index] == 10:
                digits[index] = 0
                digits[index - 1] += 1
            else:
                break
            index -= 1
        
        if digits[0] == 0:
            return digits[1:]
        else:
            return digits
        """
        
        
        n = len(digits)
        
        #范围是 n-1 到 -1，反向遍历(from -1 to n-1)
        for i in range(n - 1, -1, -1):
            #不是9时，在这位数上+1
            if digits[i] != 9:
                digits[i] += 1
                #如果个位上不是9，则range是(n, n)，直接return
                for j in range(i + 1, n):
                    digits[j] = 0
                return digits

        # digits 中所有的元素均为 9
        return [1] + [0] * n

print(plusOne(1, [1,2,4,9]))