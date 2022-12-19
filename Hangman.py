print("Play Hangman, designed by Smera Kanaujia")
x=str(input("Player 1, enter the word: "))
spl=list(x)
num=len(spl)
chance=['H','A','N','G','M','A','N']
print(chance)
line=[]
for i in range (num):
    line.append('_')
y=' '.join(line)
print(y)

def find_index(letter):
    ind=[]
    for i in range(num):
        if spl[i]==letter:
            ind.append(i)
    return ind

def display():
    ans=' '.join(line)
    print(ans)
    print()
    print (chance)
c=0
while True: 
    letter=input("Enter letter: ")
    s=find_index(letter)
    for i in s:
        line[i]=letter
    if len(s)==0:
        chance[c]='X'
        c+=1
    if '_' not in line:
        display()
        print("you won")
        break
    if c==7:
        print(chance)
        print("you lost, try again!")
        break
    display()