class Solution:
    
    # define minimum and maximum result
    INT_MIN = 0 - 2 ** 31
    INT_MAX = 2 ** 31 - 1
    
    # check if it's a valid index
    def isValid(self, index:int, letter:list) -> bool:
        if index > len(letter) - 1:
            return False
        elif index < 0:
            return False
        else:
            return True
    
    # check if the current character pointed by index is a valid number
    def isNumber(self, index:int, letter:list) -> bool:
        if ord(letter[index]) > 57 or 48 > ord(letter[index]):
            return False
        else:
            return True
    
    # main function
    def myAtoi(self, str: str) -> int:
        # no conversion is performed if no such sequence exists because str is empty
        if len(str) < 1:
            return 0
        # store the characters in str variable into letter array
        letter = ','.join(str).split(',')
        # keep the index of the first non-whitespace character in the loop below
        first = -1
        # skip the space until the first non-whitespace character is found
        for i in range(len(letter)):
            if letter[i] == ' ':
                continue
            else:
                first = i
                break
        # no conversion is performed if no such sequence exists because it contains only whitespace characters
        if not (self.isValid(first, letter)):
            print("No conversion is performed!!")
            return 0

        # skip + or - and remember if the first non-whitespace character is '-', means the value is minus
        minus = False
        if letter[first] == '-':
            minus = True
            # increment the first index
            first = first + 1
            # and check if it's a valid index
            if not (self.isValid(first, letter)):
                print("index out of range after incrementing because of '-'")
                return 0
        elif letter[first] == '+':
            # increment the first index
            first = first + 1
            # and check if it's a valid index
            if not (self.isValid(first, letter)):
                print("index out of range after incrementing because of '-'")
                return 0

        # check if it's including a valid number
        if not (self.isNumber(first, letter)):
            print("the pointed character is not a valid number")
            return 0
        # store the number part into a list, num
        num = []
        num.append(letter[first])
        for i in range(first + 1, len(letter)):
            if (self.isNumber(i, letter)):
                num.append(letter[i])
            else:
                break
        # construct an integer from the stored number part
        result = 0
        for i in range(len(num)):
            result = result + int(num[-1 - i]) * (10 ** i)
        # make it negative number if it's detected as minus number
        if minus == True:
            result = 0 - result    
        # check if it's in a valid range of number
        if result < self.INT_MIN:
            return self.INT_MIN
        elif result > self.INT_MAX:
            return self.INT_MAX
        else:    
            # output the result if it's valid
            return result
