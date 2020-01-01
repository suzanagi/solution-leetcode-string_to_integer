from solution import Solution

def testcase01():
    # Input: "42"
    return "42"

def testcase02():
    # Input: "   -42"
    return "   -42"

def testcase03():
    # Input: "4193 with words"
    return "4193 with words"

def testcase04():
    # Input: "words and 987"
    return "words and 987"

def testcase05():
    # Input: "-91283472332"
    return "-91283472332"

def testcase06():
    # Input: ""
    return ""

def testcase07():
    # Input: "+"
    return "+"

if __name__ == '__main__':
    
    in_str = testcase04()
    sol = Solution()
    print(sol.myAtoi(in_str))

