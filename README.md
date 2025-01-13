# Blackjack Game

Tento projekt obsahuje jednoduchou textovou implementaci hry Blackjack v Pythonu. Hra simuluje interakci mezi háčečem a dealerem, přičemž cílem je dosáhnout součtu 21 nebo co nejbližší hodnoty bez překročení tohoto čísla.

## Popis jednotlivých prvků kódu

### Import knihovny
```python
import random
```
Používá se k generování náhodných čísel, která reprezentují hodnoty jednotlivých karet.

### Inicializace hry
```python
D1 = random.randrange(1, 11)
D2 = random.randrange(1, 11)
D3 = random.randrange(1, 11)
D = D1 + D2
```
- `D1`, `D2` a `D3`: Náhodné hodnoty karet dealera (třetí karta může být použita později).
- `D`: Součet prvních dvou karet dealera.

```python
x1 = random.randrange(1, 11)
x2 = random.randrange(1, 11)
x = x1 + x2
```
- `x1` a `x2`: Náhodné hodnoty prvních dvou karet hráče.
- `x`: Součet hodnot karet hráče.

### Zahájení hry
```python
print("Blackjack")
print("dealer: ", D1)
print("vy: ",x1, "a", x2)
print("váš součet: ", x)
```
- Vypíše se úvadní informace o hodnotě první karty dealera a hodnotě karet hráče.

### Průběh hry
#### Možnost vzít další kartu
```python
while x < 21:
    A = input("další karta? ")
    y = random.randrange(1, 10)
    if A == "a":
        x = x + y
        print("------------------")
        print("karta otočena: ", y)
        print("součet", x)
        print("------------------")
```
- Pokud hráč zadá "a" (Ano), je mu přidělena nová karta s náhodnou hodnotou a součet se aktualizuje.

#### Ukončení tahu
```python
    elif A == "n":
        print("------------------")
        print("druhá karta dealera: ", D2 )
        print("součet dealera: ",D)
        break
```
- Pokud hráč zadá "n" (Ne), tah končí a dealer odhalí svou druhou kartu.

### Dealerova strategie
```python
if D < 17:
    print("Dealer si vezme kartu.")
    while D < 17:
        o = random.randrange(1, 11)
        D = D + o
        print("Dealer si vezme kartu: ", o)
```
- Dealer si bere další karty, dokud jeho součet nedosáhne 17 nebo více.

### Vyhodnocení výsledku
```python
if x > 21:
    print("Presahrali jste!!!")
```
- Pokud součet hráče překročí 21, hráč prohrává.

```python
if D > 21:
    print("Dealer přesáhl 21, VYHRÁLI JSTE!")
elif x > D:
    print("Vyhráli jste!")
elif x < D:
    print("Dealer vyhrál.")
else:
    print("Remíza.")
```
- Vyhodnocení, zda vyhrál hráč, dealer nebo zda hra skončila remízou.

## Jak spustit kód
1. Ujistěte se, že máte nainstalovaný Python 3.
2. Zkopírujte kód do souboru například `blackjack.py`.
3. Spusťte kód pomocí příkazu:
   ```bash
   python blackjack.py
   ```
4. Postupujte podle instrukcí na obrazovce.

## Poznámky
- Tento kód je jednoduchou implementací a nezahrnuje pokročilá pravidla Blackjacku (např. esa za 1 nebo 11 bodů, sázení atd.).
- Hru lze upravit a rozšířit o další funkce.
- Ješte bych chěl poděkovat Nathanu Mulengovi za dodání nápadu na tento projekt.
- A Vítězslavovi Zigáčkovi za vysvětleni jak funguje Github.

## Licence
Tento projekt je licencován pod licencí MIT.



## Nástroje: 

JetBrains s.r.o. (2000–2025). PyCharm. Dostupné z: https://www.jetbrains.com/pycharm/download/?section=windows [cit. 2025-1-5].

OpenAI. (2023). ChatGPT Language Model. Dostupné z: https://openai.com/chatgpt [cit. 2025-1-5].

## Literatura:

InterviewBit. (2021–2023). Python Commands List. Dostupné z: https://www.interviewbit.com/blog/python-commands/ [cit. 2025-1-5].
