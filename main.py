import sys
import random
import datetime

record = []
print("Caesar cipher encrypt and decrypt service\ntype '/help' for help")

f = open("vocab.txt","r")
vocab = f.read().split("\n")

def checkHist(arr):
    for i in range(len(arr)):
        print("Record " + str(i + 1) + ":\nTime: " + arr[i][1] + "\nOperation Type: " + arr[i][0] + "\nInput: " + arr[i][2] + "\nOutput: " + arr[i][3])
    
def checkVocab(s, type):
    outputVocab = s.split(" ")
    cnt = 0
    for i in outputVocab:
        for j in vocab:
            if(i == j):
                cnt += 1
                print(i)
                if(cnt > len(outputVocab) / 6):
                    return True
    decrypt(s, 1, type)

def isSmall(k):
    if(k > 96 and k < 123): return True
    return False

def isLetter(k):
    if ((k > 64 and k < 91) or isSmall(k)): return True
    return False

def outputProcess(s, type):
    if(type == 1):
        try:
            g = open("result.txt", "w")
        except:
            g = open("result.txt", "x")
            g = open("result.txt", "w")
        g.write(s)
        g.close
        print("Done!")
    else:
        print("Output: " + s)

def encrypt(s, type):
    k = random.randint(1,25)
    output = ""
    for i in range(len(s)):
        intChar = ord(s[i])
        if(isLetter(intChar)):
            if((intChar + k > 122 and isSmall(intChar)) or (intChar + k > 90 and not(isSmall(intChar)))): newAscii = intChar + k - 26
            else: newAscii = intChar + k
            output += chr(newAscii)
        else: output += s[i]
    time = datetime.datetime.now()
    record.append(["Encryption", time.strftime("%d/%m/%Y - %H:%M:%S"), s, output])
    outputProcess(output, type)

def findDiff(s, type):
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
    diff = maxIndex - 4
    if(diff < 0) : diff += 26
    decrypt(s, diff, type)
    
def decrypt(s, k, type):
    output = ""
    for i in range(len(s)):
        intChar = ord(s[i])
        if(isLetter(intChar)):
            if((intChar - k < 97 and isSmall(intChar)) or (intChar - k < 65 and not(isSmall(intChar)))): newAscii = intChar - k + 26
            else: newAscii = intChar - k
            output += chr(newAscii)
        else: output += s[i]
    if(len(output.split(" ")) > 200 or checkVocab(output, type) == True):
        time = datetime.datetime.now()
        record.append(["Decryption", time.strftime("%d/%m/%Y - %H:%M:%S"), s, output])
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
        contentBool = True
        if(commandList[1] == "1"):
            try:
                f = open(commandList[2], "r", encoding="utf-8")
                content = f.read()
                f.close()
            except:
                print("File not exist")
                contentBool = False
        if contentBool:
            if(commandList[0] == "/decrypt"):
                if(commandList[1] == "2"):
                    content = input("Input the text you want to decrypt: ")
                findDiff(content, int(commandList[1]))
            else:
                if(commandList[1] == "2"):
                    content = input("Input the text you want to encrypt: ")
                encrypt(content, int(commandList[1]))
                