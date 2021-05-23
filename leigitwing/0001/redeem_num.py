# 为 app 生成 200 个优惠码，16 位大写字母和数字混合的字符串
__author__ = 'Lei gitwing'
__create__ = '2021-05-22'
__modified__ = '2021-05-23'
import random

def generate_redeem_code(num):
    code_length = 16
    
    file = open('coupon.txt', 'w')
    chars = 'ABCDEFGHIJKLMNOPGRSTUVWXYZ1234567890'
    for i in range(num):
        result = ''
        for j in range(code_length):
            result += random.choice(chars)

        file.write(result + "\n")
    file.close()    

    # print(len(result) == 16)  # Check if the length of the result is 16

if __name__ == '__main__':
    generate_redeem_code(200)
