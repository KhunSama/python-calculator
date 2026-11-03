class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0
        if b > 0:
            for i in range(b):
                result = self.add(result, a)
        elif a > 0:
            for i in range(a):
                result = self.add(result, b)
        else:
            x = self.subtract(result, a)
            y = self.subtract(result, b)
            result = self.multiply(x, y)
        return result

    def divide(self, a, b):
        result = 0
        if a > 0:
            while a >= b:
                a = self.subtract(a, b)
                result += 1

        elif a < 0:
            x = self.subtract(result, a)
            while x >= b:
                x = self.subtract(x, b)
                result -= 1
        # else
            
        return result
    
    def modulo(self, a, b):
        while a <= b:
            a = a-b
        return a

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))