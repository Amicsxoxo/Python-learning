class Solution(object):
    def addBinary(self, a, b):
        a = list(a)
        b = list(b)
        aNum = []
        bNum = []
        a.reverse()
        b.reverse()
        for n in range(len(a)):
            aNum.append(int(a[n]) * (2**n))
            
        for n in range(len(b)):
            bNum.append(int(b[n]) * (2**n))
   
        aTotal = 0
        bTotal = 0
        for n in aNum:
            aTotal += n
            
        for n in bNum:
            bTotal += n
            
        total = aTotal + bTotal
        ##
        print(total, aTotal, bTotal)
        ##
        loopFactor = True
        numList = []
        while loopFactor:
            if total//2 != 0:
                  numList.append(total%2)
                  total = total//2
            else:
                numList.append(total%2)
                loopFactor = False
        finalTotal= ""
        numList.reverse()
        for n in numList:
            finalTotal += str(n)
        return int(finalTotal) 
        """
        :type a: str
        :type b: str
        :rtype: str
        """
print(Solution().addBinary(a="1010", b="1011"))