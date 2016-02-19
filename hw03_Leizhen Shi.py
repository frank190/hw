#CS-UY1122
#HW3
#Leizhen Shi

import base64

#Q2 Converting decimal number to binary
def decimal_to_binary():
    num_input = int(input("Please enter the number you want to input: "))
    output = bin(num_input)
    print (output)

#Q3 Converting ascii to string
            
def hex_to_ascii(lst):
    output = ''.join(chr(i) for i in lst)
    print (output)

#Q4 Converting binary to hexadecimal
def binary_to_hex():
    string_in = input("Please enter the binary number you want to convert: ")
    output = hex(int(string_in, 2))
    print (output)

#Q5 Converting octal to decimal
def octal_to_deci():
    num_input = input("Please enter the octal number you want to input: ")
    output = 0
    power = len(num_input) -1
    for i in num_input:
        output += int(i)* 8** power
        power -= 1
    print (output)
