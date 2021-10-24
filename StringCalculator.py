class StringCalculator:
    def add(self, numbers):
        if len(numbers) == 0:
            return 0
        elif len(numbers) == 1:
            return int(numbers)
        else:
            num = list(map(int, numbers.split(',')))
            return sum(num)


if __name__ == '__main__':
    calc = StringCalculator()
    # Empty string
    assert(calc.add("") == 0)   # Empty string will return 0
    
    # only 1 number
    assert(calc.add("1") == 1)
    assert(calc.add("10") == 10)
    
    # 2 number
    assert(calc.add("1,2") == 3)
    assert(calc.add("2,2") == 4)
    
    print("ALL TEST CASES PASS FOR 0, 1 OR 2 NUMBERS")