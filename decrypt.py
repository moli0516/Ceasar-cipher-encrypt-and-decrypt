import os
import sys
import datetime

record = []
print("Caesar cipher encrypt and decrypt service\ntype '/help' for help")

def checkHist(arr):
    for i in range(len(arr)):
        print("Record " + str(i + 1) + ":\nTime: " + arr[i][1] + "\nOperation Type: " + arr[i][0] + "\nInput: " + arr[i][2] + "\nOutput: " + arr[i][3])
    
def isSmall(k):
    if(k > 96 and k < 123): return True
    return False

def isLetter(k):
    if ((k > 64 and k < 91) or isSmall(k)): return True
    return False

def outputProcess(s, type):
    if(type == 1):
        g = open("result.txt", "w")
        g.write(s)
        g.close
    else:
        print(s)
    return 0

def encrypt(s, type):
    return 0

def decrypt(s, type):
    output = ""
    cnt = [0] * 26
    for i in range(len(s)):
        intChar = ord(s[i])
        if(isLetter(intChar)):
            if(isSmall(intChar)):
                letterIndex = intChar - 97
            else:
                letterIndex = intChar - 65
            cnt[letterIndex] += 1
    maxIndex = 0
    for i in range(25):
        if(cnt[i + 1] > cnt[maxIndex] and i != 3): maxIndex = i + 1
    different = maxIndex - 4
    if(different < 0) : different += 26
    for i in range(len(s)):
        intChar = ord(s[i])
        if(isLetter(intChar)):
            if((intChar - different < 97 and isSmall(intChar)) or (intChar - different < 65 and not(isSmall(intChar)))): newAscii = intChar - different + 26
            else: newAscii = intChar - different
            output += chr(newAscii)
        else: output += s[i]
    time = datetime.datetime.now()
    record.append(["Encryption", time.strftime("%d/%m/%Y - %H:%M:%S"), s, output])
    outputProcess(output, type)

while True:
    command = input("Command: ")
    if(command == "/quit"):
        sys.exit()
    elif(command == "/help"):
        print("/decrypt <operation type(1 / 2)> <file name> - decrypt the text")
        print("/encrypt <operation type(1 / 2)> <file name> - encrypt the text")
        print("/quit - exiting this application")
        print("/hist - check the operation history in this session")
        print("type 1 - input by the file that you provide and output the text to 'result.txt'")
        print("type 2 - input and output text through terminal")
    elif(command == "/hist"):
        checkHist(record)
    else:
        commandList = command.split(" ")
        if(commandList[1] == "1"):
            if(os.path.exists(commandList[2])):
                f = open(commandList[2], "r", encoding="utf-8")
                content = f.read()
            else:
                print("File not exist")
        if(commandList[0] == "/decrypt"):
            if(commandList[1] == "2"):
                content = input("Input the text you want to decrypt: ")
            decrypt(content, int(commandList[1]))
        else:
            if(commandList[1] == "2"):
                content = input("Input the text you want to decrypt: ")
            encrypt(content, int(commandList[1]))
                