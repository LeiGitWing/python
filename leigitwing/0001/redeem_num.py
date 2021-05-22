# 为 app 生成优惠码，16位大写字母和数字混合的字符串
__author__ = 'Lei gitwing'
__create__ = '2021-05-22'
import string, random

def generate_redeem_code():
    count = 0
    result = ''
    
    while True:
        letter = random.choice(string.ascii_uppercase)
        digit = random.choice(string.digits)
        # 数字出现次数 0-4 次，出现位置也随机
        if count == random.choice(range(0, 17)):
            result += digit
            count += 1
        result += letter
        count += 1

        if count == 16:
            break
        
    print(result)
    print(len(result) == 16)  # Check if the length of the result is 16

if __name__ == '__main__':
    generate_redeem_code()
    