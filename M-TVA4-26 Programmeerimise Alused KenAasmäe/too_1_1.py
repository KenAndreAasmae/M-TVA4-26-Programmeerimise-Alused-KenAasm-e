# ESIMENE PUNKT
print("Tere, maailm!")

nimi=input("Mis on sinu nimi?")
print(f"Tere, maailm! Tervitan sind {nimi}")
vanus=input("Kui vana sa oled=")
print(f"Tere, maailm! Tervitan sind {nimi}! Sa oled {vanus} aastat vana.")

# TEINE PUNKT

vanus = 18
eesnimi = "Jaak"
pikkus = 16.5
kas_käib_koolis = True

# KOLMAS PUNKT

from random import *

kommide_arv = randint(1, 200)
print(f"Laual on, {kommide_arv} kommi")

eemalda = int(input("Mitu kommi tahad laualt ära võtta?"))
kommide_arv_laual = kommide_arv - eemalda
print(f"Nüüd on laual {kommide_arv_laual} kommi")

# NELJAS PUNKT

from math import *
umbermoot = float(input("Mis on puu ümbermõõt?"))
diameeter = umbermoot / 3.14
print(f"Puu diameeter on {diameeter} m.")

# VIIES PUNKT

N = float(input("Mis on maatüki pikkus N: "))
M = float(input("Mis on maatüki laius M: "))
diagonaal = sqrt(N**2 + M**2)
print(f"Maatüki diagonaal on {diagonaal} m.")

# KUUES PUNKT   

aeg = float(input("Mitu tundi kulus sõiduks? "))
teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
kiirus = teepikkus / aeg   # Valem oli valepidi
print("Sinu kiirus oli " + str(kiirus) + " km/h")

# SEITSMES PUNKT

a = int(input("Sisesta esimene arv: "))
b = int(input("Sisesta teine arv: "))
c = int(input("Sisesta kolmas arv: "))
d = int(input("Sisesta neljas arv: "))
e = int(input("Sisesta viies arv: "))

summa = a + b + c + d + e
keskmine = summa / 5
print (f"Arvude summa on {summa} ja keskmine on {keskmine}.")

jagaja  = int(input("Sisesta arv, millega soovid keskmist jagada: "))
print (f"Keskmise jagamisel arvuga {jagaja} saad tulemuseks {keskmine / jagaja}.")  

# KAHEKSAS PUNKT

print("@..@")
print("(----)")
print("( \__/ )")
print("^^ "" ^^")   

# ÜHEKSAS PUNKT

a = 6
b = 3
c = 2
P = a + b + c
print(f"Kolmnurga ümbermõõt on {P} cm.")

# KÜMNES PUNKT

print("Pitsa maksab 12.90 eurot.")
isikute_arv = int(input("Mitu sõpra sul kaasas on? "))
print("Jätate teenindajale 10% jootraha.")
jootraha = (12.90 * 0.10) / isikute_arv
print(f"Igaüks maksab {jootraha:.2f} teenindajale")

