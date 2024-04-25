
import random
while True:
    karakterler = "+-/ugdhfjdfıfvbnjdstu23570r2fg3h8t   6879ghfjdfkgyhmjkhvg"


    sifre_uzunluğu =int(input("SİFRENİN UZUNLUĞUNU GİR"))

    sifre = ""

    for i in range(sifre_uzunluğu):
    sifre = sifre + random.choice(karakterler)


    print(sifre)
