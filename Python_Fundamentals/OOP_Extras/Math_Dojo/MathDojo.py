
class MathDojo:
    def __init__(self):
        self.result =0
    
    # addition method
    def add(self, num, *nums):
        self.result += num
        for num in nums :
            self.result+= num
        return self
    
    # subtraction method
    def sub(self, num, *nums):
        self.result -= num
        for num in nums :
            self.result-= num
        return self
    


# creating new instance from MathDojo class
testMath=MathDojo()
# Practice chaining methods
testMath=(testMath.add(5,5).sub(5,5).add(7.5).sub(3.5)).result
print("the result is : ",testMath)