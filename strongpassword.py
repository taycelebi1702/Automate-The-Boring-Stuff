import re

def strongpassword(message):
    lengthReg = re.compile(r'''.{8,}''')
    if not lengthReg.search(message):
        return False
    upperCase = re.compile(r'''['A-Z']+''')
    if not upperCase.search(message):
        return False
    lowerCase = re.compile(r'''[a-z]+''')
    if not lowerCase.search(message):
        return False
    digitNum = re.compile(r'''\d+''')
    if not digitNum.search(message):
        return False
    else:
        return True


while True:
    mess = input('Please enter your password: ')
    if strongpassword(mess):
        print('Yeahh! This is a strong password')
    else:
        print('Upps. Try again. Your password is too weak!')
