import random
import math
lower = int (input("Digite o menor numero:- "))
upper = int (input("Digite o maior numero:- "))
x = random.randint(lower, upper)
print("\n\tvocê tem ", round(math.log(upper - lower +1,2))," chances para tentar acertar \n")
count =0
while count < math.log(upper - lower +1, 2):
    count+= 1
    guess = int(input("tente um numero:- "))
    if x == guess:
        print("parabens você conseguiu!!!", count, "tentativas")
        break
    elif x < guess:
        print("você chutou muito alto!!!")
    elif x > guess:
        print("você chutou muito baixo")

if count >= math.log(upper - lower +1,2):
    print("\n O numero é %d"%x)
    print("\t melhor sorte na próxima!!")