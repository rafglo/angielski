import random
#slowa = open(r"C:\Users\Rafal\OneDrive\Pulpit\AiSD\slowa.txt", "r", encoding='utf-8').read().split()
slowa2 = open(r"C:\Users\Rafal\OneDrive\Pulpit\AiSD\slowa3.txt", "r", encoding='utf-8').readlines()

"""slowa1 = []
for i in range(0,len(slowa), 3):
    slowa1.append(slowa[i])

defs = []
for i in range(2,len(slowa),3):
    defs.append(slowa[i])
"""

slowa3 = []
defs2 = []
for cos in slowa2:
    for i in range(len(cos)):
        if cos[i] == "-":
            slowa3.append(cos[:(i-1)])
            defs2.append(cos[(i+1):])


slowa_ost =  slowa3
defs_ost =  defs2

klik = ""
while klik == "":
    klik = input("wylosuj definicje")
    indeks = random.randint(0, len(slowa_ost)-1)
    print(defs_ost[indeks])
    klik2 = input("pokaz slowo")
    if klik2 == "":
        print(slowa_ost[indeks])
    else:
        break     




