'''
ok = [0X7e, 0x22, 0X4d, 0x76, 0X45, 0x25, 0x71, 0x33, 0x5b, 0x78, 0x64, 0x62, 0x6f, 0x65]
flag = ""

for i in range(len(ok)):
    ok2 = (len(ok)//2 - 4)
    flag = chr(ok[i] ^ ok2) + flag
print(flag)

#flag{X0r&FuN!}
'''

'''
ok = [0X28, 0X0b, 0X17, 0x32, 0x0b, 0X07, 0X0a, 0X36, 0X12, 0x19, 0x00, 0X54, 0x29, 0x00, 0X2f, 0X08, 0X56, 0x18, 0X31, 0X5d, 0x03, 0x54, 0X0b]
ok2 = [ord('f'), ord('l'), ord('a'), ord('g'), ord('{')]
key = [0x4e, 0x67, 0x76, 0x55, 0x70]

for i in range(len(ok)):
    print(chr(key[i%len(key)]^ok[i]))


#flag{Im@GiN3_U_F1nd-M3}
'''