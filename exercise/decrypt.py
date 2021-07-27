#基礎解密程式
import string

def decrypt(text,decrydict):
    cipher=[]       #建立空字串
    for i in text:
        ciphertext = decrydict[i]
        cipher.append(ciphertext)
    return ''.join(cipher)      #將串列轉為字串

abc = string.printable[:-5]     #建立全英文符文字元，不包括不可列印字元
subText = abc[-3:] + abc[:-3]   #加密規則，重新排列字元，將後三字元放到最前面
decry_dict = dict(zip(abc,subText))  #建立解密字典

#msg = input("請輸入待解密文字，限英文及符號: ")
msg = "l*dp2urerw"                         #待解密字串
ciphertext = decrypt(msg,decry_dict)       #解密後字串

print("解密後字串為: " + ciphertext)



#延伸思考
#建立一個加密模組
#建立更複雜的加密規則，並且只要在其他程式匯入此模組
#就能更快的建立加/解密字典，並且確保加密規則一致