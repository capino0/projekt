import random

D1 = random.randrange(1, 11)
D2 = random.randrange(1, 11)
D3 = random.randrange(1, 11)
D = D1 + D2


x1 = random.randrange(1, 11)
x2 = random.randrange(1, 11)
x = x1 + x2

print("Blackjack")
print("dealer: ", D1)
print("vy: ",x1, "a", x2)
print("váš součet: ", x)

while x < 21:
    A = input("další karta? ")
    y = random.randrange(1, 10)
    if A == "a":
        x = x + y
        print("------------------")
        print("karta otočena: ", y)
        print("součet", x)
        print("------------------")
    elif A == "n":
        print("------------------")
        print("druhá karta dealera: ", D2 )
        print("součet dealera: ",D)
        break
    else:
        print("Prosím zadejte 'a' pro Ano nebo 'n' pro Ne.")

if x > 21:
    print("Presahli jste 21!!!")
else:

    if D < 17:
        print("Dealer si vezme kartu.")
        while D < 17:
            o = random.randrange(1, 11)
            D = D + o
            print("Dealer si vezme kartu: ", o)

print("Součet dealera")

if D > 21:
        print("Dealer přesáhl 21, VYHRÁLI JSTE!")
elif x > D:
        print("Vyhráli jste!")
elif x < D:
        print("Dealer vyhrál.")
else:
        print("Remíza.")
