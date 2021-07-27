#基礎加密程式
import string

def encrypt(text,encrydict):    #加密函數
    cipher=[]                   #建立空字串
    for i in text:              #將待加密文字一一加密後丟至串列中
        ciphertext = encrydict[i]
        cipher.append(ciphertext)
    return ''.join(cipher)      #將串列轉為字串

abc = string.printable[:-5]     #建立全英文符文字元，不包括不可列印字元
subText = abc[-3:] + abc[:-3]   #加密規則，重新排列字元，將後三字元放到最前面
encry_dict = dict(zip(subText,abc))  #建立加密字典

#msg = input("請輸入待加密文字，限英文及符號: ")
msg = "i'am robot"                         #待加密字串
ciphertext = encrypt(msg,encry_dict)       #加密後字串

print("加密後字串為: " + ciphertext)