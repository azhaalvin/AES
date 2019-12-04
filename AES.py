from tkinter import *

#SBOX
Rcon = [[0x8d, 0x01, 0x02, 0x04], [0x08, 0x10, 0x20, 0x40], [0x80, 0x1b, 0x36,0x6c], [0xd8, 0xab, 0x4d, 0x9a] ]
Sbox = [
        [0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76],
        [0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0],
        [0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15],
        [0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75],
        [0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84],
        [0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF],
        [0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8],
        [0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2],
        [0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73],
        [0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB],
        [0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79],
        [0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08],
        [0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A],
        [0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E],
        [0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF],
        [0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16]
        ]
Sbox_inv = [
        [0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB],
        [0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB],
        [0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E],
        [0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25],
        [0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92],
        [0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84],
        [0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06],
        [0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B],
        [0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73],
        [0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E],
        [0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B],
        [0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4],
        [0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F],
        [0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF],
        [0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61],
        [0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D]
        ]

defaultMatrix = [[0x02, 0x03, 0x01, 0x01],
                [0x01, 0x02, 0x03, 0x01],
                [0x01, 0x01, 0x02, 0x03],
                [0x03, 0x01, 0x01, 0x02]]

newMatrix = []

def hexa(a):
    n = len(a)-1
    d = 0
    array = []
    while d <= n :
        for i in range(4):
            bit = []
            for ii in range(4):
                c=[]
                b=hex(ord(a[d]))
                b = format(ord(a[d]), "x")
                b=int(b,16)
                d=d+1
                bit.append(b)
            array.append(bit)
    return array

def cek(x): #mengganti string ke int ntuk index s-box
    if x == '0':
        c = 0
        return c
    elif x == '1':
        c = 1
        return c 
    elif x == '2':
        c = 2
        return c 
    elif x == '3':
        c = 3
        return c 
    elif x == '4':
        c = 4
        return c 
    elif x == '5':
        c = 5
        return c 
    elif x == '6':
        c = 6
        return c 
    elif x == '7':
        c = 7
        return c
    elif x == '8':
        c = 8
        return c 
    elif x == '9':
        c = 9
        return c
    elif x == 'A' or x == 'a' :
        c = 10
        return c
    elif x == 'B' or x == 'b':
        c = 11
        return c 
    elif x == 'C' or x == 'c':
        c = 12
        return c 
    elif x == 'D' or x == 'd':
        c = 13
        return c 
    elif x == 'E' or x == 'e':
        c = 14
        return c
    elif x == 'F' or x == 'f':
        c = 15
        return c   

def subB(x): #fungsi sib byte
        for i in range(4):
                for ii in range(4):
                        #print("cek ascii = ",x[i][ii])
                        nilai = hex(x[i][ii])
                        nilai2=int(nilai,16)
                        #print("nilai=",nilai)
                        if nilai2 < 10 :
                            sbX = 0
                            sbY = 0
                        else:
                            if len(nilai) == 3:
                                sbX = 0
                                sbY = nilai [2]
                                sbY = cek(sbY)
                            else:
                                sbX = nilai [2]
                                sbX = cek(sbX)
                                sbY = nilai [3]
                                sbY = cek(sbY)
                        x[i][ii] = Sbox[sbX][sbY]
                        #if hex(Sbox[sbX][sbY]) == 0x09 :
                        #print("cek s-boxnya",hex(Sbox[sbX][sbY]))
                        #print('sbx=',sbX)
                        #print('sby=',sbY)
        return x

def shifter(x,i): #fungsi pembaliknya 
    for n in range(i):
        temp = x[0]
        x[0] = x[1]
        x[1] = x[2]
        x[2] = x[3]
        x[3] = temp
    return x

def shiftRow(x): #pemangginya 
    for i in range(4):
        x[i] = shifter(x[i],i)
    return x

def subBKey(x): #Sub byte key 
    for ii in range(4):
        nilai = hex(x[ii])
        sbX = nilai [2]
        sbY = nilai [3]
        sbX = cek(sbX)
        sbY = cek(sbY)
        x[ii] = Sbox[sbX][sbY]
        #print('sbx=',sbX)
        #print('sby=',sbY)
        return x

def xor(x,y):
    for i in range(4):
        x[i] = x[i] ^ y[1]
    print("x ke-1 : ",x[0])
    print("x ke-2 : ",x[1])
    print("x ke-3 : ",x[2])
    print("x ke-4 : ",x[3])
    print()
    return x

def KeySchedule(x,n):
    newKey=[]
    n = n % 4
    x1 = []
    x1 = subBKey(x[3])
    x[0] = xor(x[0],Rcon[n])
    x[0] = xor(x[0],x1)
    for i in range(4):
        newKey.append(x[i])
        if i > 0 :
            x[i] = xor(x[i],x[i-1])
    return newKey

def addroundkey(x,y):
    hasil = []
    status = False
    str_list = [4]
    res = []
    for i in range(4):
        if (i == 3):
            status = True
            res.append([x[i : j] for i, j in zip([0] + str_list, str_list + [None])])
            hasil.append(xor(res[0][0][0],y[i]))
        else:
            hasil.append(xor(x[i],y[i]))
    return hasil


def mixCol(leftMatrix, rightMatrix):
        #local variable
        tempBin = []
        splitList = [4, 8, 12]
        #algorithm
        for i in range(4):
                for j in range(4):
                        tempInt = leftMatrix[0][j] * rightMatrix[j][0+i]
                        tempMOD = tempInt % 283
                        tempBin.append(tempMOD)
                        if (j == 1): temp1 = tempBin[0] ^ tempBin[1]
                        elif (j == 3): temp2 = tempBin[2] ^ tempBin[3]
                temp = temp1 ^ temp2
                newMatrix.append(temp)
                tempBin.clear()
                for j in range(4):
                        tempInt = leftMatrix[1][j] * rightMatrix[j][0+i]
                        tempMOD = tempInt % 283
                        tempBin.append(tempMOD)
                        if (j == 1): temp1 = tempBin[0] ^ tempBin[1]
                        elif (j == 3): temp2 = tempBin[2] ^ tempBin[3]
                temp = temp1 ^ temp2
                newMatrix.append(temp)
                tempBin.clear()
                for j in range(4):
                        tempInt = leftMatrix[2][j] * rightMatrix[j][0+i]
                        tempMOD = tempInt % 283
                        tempBin.append(tempMOD)
                        if (j == 1): temp1 = tempBin[0] ^ tempBin[1]
                        elif (j == 3): temp2 = tempBin[2] ^ tempBin[3]
                temp = temp1 ^ temp2
                newMatrix.append(temp)
                tempBin.clear()
                for j in range(4):
                        tempInt = leftMatrix[3][j] * rightMatrix[j][0+i]
                        tempMOD = tempInt % 283
                        tempBin.append(tempMOD)
                        if (j == 1):  temp1 = tempBin[0] ^ tempBin[1]
                        elif (j == 3): temp2 = tempBin[2] ^ tempBin[3]
                temp = temp1 ^ temp2
                newMatrix.append(temp)
                tempBin.clear()
                temp = 0
        res = [newMatrix[i : j] for i, j in zip([0] + splitList, splitList + [None])] 
        return res

def encript(plain,key):
    keyS =[]
    roundkey =[]
    plain = hexa(plain)
    key = hexa(key)
    for i in range(10):
        if i == 0 :
            roundkey =  addroundkey(plain,key)
            keyS= KeySchedule(key,i)
            plain = roundkey
        else:
            plain = subB(plain)
            plain = shiftRow(plain)
            plain = mixCol(defaultMatrix,plain)
            plain = addroundkey(plain,keyS)
            keyS= KeySchedule(keyS,i)
    return plain


x=[]
# 16 key 
# "azhaalvinrahmans"
# "1234567892345670"
# val = input("input your name : ")
# plain = val
# valKey = input("input your key : ")
# key= valKey
# x = encript(plain,key)

#print(x)

#GUI 

def default():
    lbl.config(Text = "alvin")

def encrypt_data():
     
  plainText_info = plainText.get()
  key_info = key.get()
 
  file=open(plainText_info+".txt", "w")
  file.write(plainText_info+"\n")
  file.write(key_info)
  file.close()
 
  plainText_entry.delete(0, END)
  key_entry.delete(0, END)
 
def encrypt():
  global screen1
  screen1 = Toplevel(screen)
  screen1.title("AES")
  screen1.geometry("300x250")
   
  global plainText
  global key
  global plainText_entry
  global key_entry
  plainText = StringVar()
  key = StringVar()

  lbl = Label(screen1, Text = "your txt").lbl.pack()
  Label(screen1, text = "Please enter details below").pack()
  Label(screen1, text = "").pack()
  Label(screen1, text = "PlainText * ").pack()
  plainText_entry = Entry(screen1, textvariable = plainText)
  plainText_entry.pack()
  Label(screen1, text = "key * ").pack()
  key_entry =  Entry(screen1, textvariable = key)
  key_entry.pack()
  Label(screen1, text = "").pack()
  Button(screen1, text = "Encrypt", width = 10, height = 1, command = encrypt_data).pack()
 
def login():
  print("Login session started")
 
 
def main_screen():
  global screen
  screen = Tk()
  screen.geometry("300x250")
  screen.title("Notes 1.0")
  Label(text = "Notes 1.0", bg = "grey", width = "300", height = "2", font = ("Calibri", 13)).pack()
  Label(text = "").pack()
  Button(text = "Encrypt Here",height = "2", width = "30", command = encrypt).pack()
 
  screen.mainloop()
 

main_screen()
  