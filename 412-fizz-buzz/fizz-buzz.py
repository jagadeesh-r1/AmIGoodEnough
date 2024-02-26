class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = [] 
        for i in range(1, n+1): 
            if (i%3==0 and i%5==0):
                value="FizzBuzz" 
            elif i%3==0 and not i%5==0:
                value = "Fizz"
            elif not i%3==0 and i%5==0:
                value = "Buzz"
            else:
                value = str(i)
            result.append(value)
        return result
        