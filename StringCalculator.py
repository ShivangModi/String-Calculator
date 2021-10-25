count = 0

class StringCalculator:
    def add(self, numbers):
        global count
        count += 1

        if len(numbers) == 0:
            return 0
        
        if numbers[0:2] == '//':
            numbers = numbers[4:].replace(numbers[2], ',')

        numbers = numbers.replace('\n', ',')
        num = list(map(int, numbers.split(',')))
        num = [n if n<=1000 else 0 for n in num]

        try:
            negative = [str(i) for i in num if i < 0]
            if negative != []:
                raise ValueError("Negative values are not allowed. Negative values: " + ', '.join(negative))
            else:
                return sum(num)
        except ValueError as ve:
            print(ve)
    
    # returns how many times add() method was invoked
    def GetCalledCount(self):
        return count


if __name__ == '__main__':
    calc = StringCalculator()

    # how many times add() method was invoked
    assert(calc.GetCalledCount() == 0)

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

    # handle different delimiters
    # to change a delimiter, the beginning of the string will contain a separate line that looks like this:
    # "//[delimeter]\n[numbers]"
    assert(calc.add("//;\n1;2") == 3)
    assert(calc.add("//;\n1;2;3") == 6)

    # Negative numbers will throw an exception
    # assert(calc.add("1,-2,3"))  # single negative value
    # assert(calc.add("1,-2,-3")) # multiple negative values

    # numbers bigger than 1000 should be ignored
    assert(calc.add("2,1001") == 2)

    # assert(calc.GetCalledCount() == 12)

    print("ALL TEST CASES PASS FOR UNKNOWN AMOUNT OF NUMBERS")