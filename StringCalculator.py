class StringCalculator:
    def add(self, numbers):
        if len(numbers) == 0:
            return 0
        
            numbers = numbers[4:].replace(numbers[2], ',')
        
        numbers = numbers.replace('\n', ',')
        num = list(map(int, numbers.split(',')))
        return sum(num)


if __name__ == '__main__':
    calc = StringCalculator()
    # Empty string
    assert(calc.add("") == 0)   # Empty string will return 0
    
    # for unknown amount of numbers
    assert(calc.add("1") == 1)
    assert(calc.add("10") == 10)
    assert(calc.add("1,2") == 3)
    assert(calc.add("2,2") == 4)
    assert(calc.add("1,2,3") == 6)
    assert(calc.add("1,2,3,4") == 10)
    assert(calc.add("1,2,3,4,5") == 15)

    # handle new lines between numbers (instead of commas)
    assert(calc.add("1\n2,3") == 6)
    assert(calc.add("1\n2") == 3)
    print("ALL TEST CASES PASS FOR UNKNOWN AMOUNT OF NUMBERS")