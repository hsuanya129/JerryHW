def cal():
    num1 = int(input("請輸入數字:"))
    symbol = input("請輸入運算符號:")
    num2 = int(input("請輸入數字:"))
    if symbol == '+':
        ans = num1+num2
    elif symbol == '-':
        ans = num1-num2
    elif symbol == '*':
        ans = num1*num2
    elif symbol == '/':
        ans = num1/num2
    else:
        print("輸入錯誤!!")
    return ans
