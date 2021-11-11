Dict = {"A" : ".-","B" : "-...","C" : "-.-.","D" : "-..",
"E" : ".","F" : "..-.","G" : "--.","H" : "....",
"I" : "..","J" : ".---","K" : "-.-","L" : ".-..",
"M" : "--","N" : "-.","O" : "---","P" : ".--.",
"Q" : "--.-","R" : ".-.","S" : "...","T" : "-",
"U" : "..-","V" : "...-","W" : ".--","X" : "-..-",
"Y" : "-.--","Z" : "--..","1" : ".----","2" : "..---",
"3" : "...--","4" : "....-","5" : ".....","6" : "-....",
"7" : "--...","8" : "---..","9" : "----.","0" : "-----",
"." : ".-.-.-","," : "--..--","?" : "..--.."," " : "  ",}

codify("texto")

def Code(c):
    R = ""
    for i in c:
        R += i + " = "
        i = i.upper()
        R += Dict[i] + "\n"
    return R

print("insert a word to decode, can include A-Z 0-9 , . ? (write exit to exit)")
c = input()
while(c != "exit"):
  print(Code(input()))
  print("insert a word to decode, can include A-Z 0-9 , . ? (write exit to exit)")
  c = input()

'''insert a word to decode, can include A-Z 0-9 , . ? (write exit to exit)
banana xd
b = -...
a = .-
n = -.
a = .-
n = -.
a = .-
  =
x = -..-
d = -..

insert a word to decode, can include A-Z 0-9 , . ? (write exit to exit)
exit'''
