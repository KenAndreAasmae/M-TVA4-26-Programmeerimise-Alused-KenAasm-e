# . Juku
# a) Programm küsib eesnime. Kui nimi on Juku, kuvatakse „Lähme Jukuga kinno!“, muidu teatatakse, et täna kinno ei minda.

# Programm peab Juku ära tundma ka siis, kui nimi on kirjutatud suurtähtedega (JUKU) või väiketähtedega (juku).
# Kui nimi on kirjutatud ainult suurtähtedega, lisa märkus „Ära karju, Juku!“.
# from curses.ascii import isupper


eesnimi=input("Sisesta oma eesnimi: ")
if eesnimi.lower() == "juku":   #"JUKU".lower() => "juku"
    print("Lähme Jukuga kinno!")
    if eesnimi.isupper():
        print("Ära karju, Juku!")
    # b) Kui kinno läheb Juku, küsi tema vanus ja otsusta, millist piletit on vaja osta:
    # Kontrolli enne, kas sisestatud vanus on täisarv. Kui ei ole, kuva veateade.
        vanus = input("Sisesta oma vanus: ")
        if not vanus.isdigit():
            print("Palun sisesta kehtiv vanus täisarvuna.")
        else:
            vanus = int(vanus)
            if vanus < 6:
                print("Filmi saab tasuta vaadata.")
            if vanus <= 14:
                print("Filmi vaatamiseks osta lastepilet")
            if vanus <= 65:
                print("Filmi vaatamiseks osta täispilet")
            else:
                print("Filmi vaatamiseks osta sooduspilet")
            
else:
    print("Täna kinno ei minda.")
    

