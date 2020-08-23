# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 22:19:35 2019

@author: artur
"""
from math import *

def harjutus1():
    print("     /|")
    print("    / |")
    print("   /  |")
    print("  /   |") # Tulevikus võiks kirjutada sihukese programmi, mis joonistab ise automaatselt kolmnurga, kui talle alus ja kõrgus sisestada
    print(" /    |")
    print("/_____|")


def harjutus2():
    tegelase_nimi="Kevin"
    tegelase_vanus= str(35)
    print("Elas kord mees nimega " + tegelase_nimi + ",")
    print("kes oli " + tegelase_vanus + " aastat vana.")
    tegelase_nimi="Mikk"
    print("Talle meeldis nimi " + tegelase_nimi +",")
    print("kuid mitte tema vanus.")
    
def harjutus3():
    print("Tere \nPerestroika!")
    
def harjutus4():
    lause="Programmeerimine on lahe."
    print(len(lause))
    print(lause[4])
    print(lause.index("g"))
    print(lause.index("lah"))
    print(lause.replace("lahe","nõme"))
    
def harjutus5():
    
    print(2)
    print(2.0987)
    print(-2.45)
    
    print(3+4.5) #liitmine
    print(3-4.5) #lahutamine
    print(3*7.5) #korrutamine
    print(3/7.5) #jagamine
    print(10%3) #jäägiga jagamine
    print(3*4+5)
    print(3*(4+5))

def harjutus6():
    minu_number= -5
    print(minu_number)
    print(abs(minu_number))
    print(pow(3, 2))
    print(pow(minu_number, 5))
    print(max(4, 6))
    print(min(4, 6))
    print(round(4.2))
    print(round(4.5))
    print(round(4.51))
def harjutus7():
    print(floor(3.7))
    print(ceil(3.1))
    print(sqrt(36))
    
def harjutus8():
    nimi=input("Sisesta enda nimi: ")
    vanus=input("Sisesta enda vanus: ")
    print("Hei "+nimi+"! Sa oled "+vanus+" aastane!")
    
def kalkulaator():
    num1=input("Sisesta mõni number: ")
    num2=input("Sisesta mõni teine number: ")
    tulemus=num1+num2
    print(tulemus) #tulemus on stringina ehk andmetüübiks ei ole number vaid sõna.
    
    #komata arvutamiseks
    num1=input("Sisesta mõni number: ")
    num2=input("Sisesta mõni teine number: ")
    tulemus=int(num1)+int(num2)
    print(tulemus)
    
    #komaga arvutamiseks
    num1=input("Sisesta mõni number: ")
    num2=input("Sisesta mõni teine number: ")
    tulemus=float(num1)+float(num2)
    print(tulemus)
    
def kolmnurk():
    alus=float(input("Sisesta kolmnurga alus: "))
    kõrgus=float(input("sisesta kolmnurga kõrgus: ")) # küsime arvulisi väärtusi, aga "input" annab meile teksti tüüpi andmeid, 
                                                      # nii et tuleb andmed muuta numbriliseks floatiga
    
    valem=(alus*kõrgus)/2 #hetkel on see numbriline väärtus ehk float tüüp
    print("Kolmnurga pindala on: "+ str(valem)) #muuda saadud tulemus uuesti stringiks, sest tähti ja numbreid liita ei saa ju.
    
def harjutus9():
    sõbrad = ["Kevin","Hannah","Andrei", "Tony","Artur","Kristin","Martin"]
    #            0       1        2         3      4        5         6
    print(sõbrad)
    print(sõbrad[2])
    print(sõbrad[-1])
    print(sõbrad[1:4])
    
def harjutus10(): #listid
    õnne_numbrid=[4,8,15,16,23,42]
    sõbrad = ["Kevin","Hannah","Andrei", "Tony","Artur","Kristin","Martin"]
    sõbrad.extend(õnne_numbrid)
    print(sõbrad)
    
    sõbrad.append("Krõõt")
    print(sõbrad)
    
    sõbrad.insert(1,"Katrin")
    print(sõbrad)
    
    sõbrad.remove("Martin")
    print(sõbrad)
    
    sõbrad.clear()
    print(sõbrad)
    
    sõbrad = ["Kevin","Hannah","Andrei", "Tony","Artur","Kristin","Martin"]
    sõbrad.pop() #võtab viimase andmetüübi listist ära
    print(sõbrad)
    print(sõbrad.index("Kevin"))
    
    sõbrad = ["Kevin","Hannah","Andrei", "Tony","Artur","Kristin","Artur","Artur","Artur","Martin"]
    print(sõbrad.count("Artur"))
    
    sõbrad = ["Kevin","Hannah","Andrei", "Tony","Artur","Kristin","Martin"]
    sõbrad.sort()
    print(sõbrad)
    
def harjutus11(): #funktsiooni näide 1
    def ütle_tere():
        print("Tere!")
    print("Tipp") 
    ütle_tere()
    print("Põhi")
    
def harjutus12(): #funktsiooni näide 2
    def ütle_tere(nimi):
        print("Tere, "+ nimi)
    ütle_tere("Artur")
    
def harjutus13(): #funktsiooni näide 3
    def ütle_tere(nimi, vanus):
        print("Tere, "+nimi+"! Sa oled " + str(vanus)+ ". aastane")
    ütle_tere("Artur", "22")
    ütle_tere("Martin", 35)

def harjutus14(): #return statement
    def cube(num):
        return num*num*num # pärast returni käsku, enam midagi ei prindita.
                           # kui arvuti loeb return, katkestab tegevuse selle rea pealt.
        
    tulemus=cube(5)
    print(tulemus)
    
def harjutus15(): #if-statements
   #NÄIDE 1
    # Ma ärkan ülesse
    # kui ma olen näljane
        # siis ma söön hommikusööki
    
    #NÄIDE 2
    # Ma lahkun majast
    # KUI on pilvine
        # ma võttan kaasa vihmavarju
    # muul juhul
        # ma võttan kaasa päikseprillid
      
    #NÄIDE 3
    # Ma olen restoranis
    # KUI tahan liha
        # tellinn sealiha
    # muul juhul KUI ma soovin pastat
        # tellinn spaghetti juustu kastmega
    # muul juhul
        # tellin salati
        
        on_mees=False #toimib ainult kui väide on tõene, kui väär, ei prindi midagi
        if on_mees :
            print("Sa oled meestsoost.")
        else:
            print("Sa ei ole meestsoost.")
    
def harjutus16():
    on_mees=False
    on_pikk=False
    
    if on_mees or on_pikk:
        print("Sa oled, mees või pikk")
    else:
        print("Sa ei ole ei pikk ega mees.")
def harjutus17():
    on_mees=False
    on_pikk=False
    
    if on_mees and on_pikk:
        print("Sa oled pikka kasvu mees.")
    else:
        print("Sa ei ole pikk või ei ole mees.")
        
def harjutus18():
    on_mees=True
    on_pikk=False
    
    if on_mees and on_pikk:
        print("Sa oled pikka kasvu mees.")
    elif on_mees and not(on_pikk):
        print("Sa oled lühikest kasvu mees.")
    elif not(on_mees) and (on_pikk):
        print("Sa pole mees, aga oled pikk.")
    else:
        print("Sa ei ole ei pikk ega mees.")
        
    
def harjutus19():
    on_mees=input("Kas oled mees või naine?\n ")
    on_pikk=float(input("Mis kasvu oled? : "))
    
    if on_mees.capitalize()== "Mees" and on_pikk>=180:
        print("Sa oled pikka kasvu mees.")
    elif on_mees.capitalize()=="Mees" and(on_pikk<180):
        print("Sa oled lühikest kasvu mees.")
    elif not(on_mees.capitalize()=="Mees") and (on_pikk>=180):
        print("Sa pole mees, aga oled pikk.")
    else:
        print("Sa ei ole pikk ega mees.")
        
def parem_kalkulaator():
    num1=float(input("Sisesta esimene number: "))
    märk=input("sisesta tehte märk: ")
    num2=float(input("Sisesta kolmas number: "))
    if märk=="+":
        print(num1+num2)
    elif märk=="-":
        print(num1-num2)
    elif märk=="*":
        print(num1*num2)
    elif märk== "/":
        print(num1/num2)
    elif märk == ("astmes"):
        print(num1**num2)
    elif märk=="^":
        print(num1**num2)
    else:
        print("Sihukest tehet ei saa teha!")
    
def harjutus20(): #dictionaries
    kuuteisendus={"01":"Jaanuar",
                  "02":"veebruar",
                  "03":"märts",
                  "04":"aprill",
                  "05":"may",
                  "06":"juuni",
                  "07":"juuli",
                  "08":"august",
                  "09":"september",
                  "10":"oktoober",
                  "11":"november",
                  "12":"detsember",
    }
    print(kuuteisendus["02"])
    print(kuuteisendus.get("12"))
    print(kuuteisendus.get("Luv"))
    print(kuuteisendus.get("Luv","Sellist võtit ei ole olemas."))
    
def meetrid(): #ühikute teisendamine meetriteks, ruutmeetriteks, kuupmeetriteks jne.
    num=float(input("Sisesta suurus: "))
    ühik=input("Sisesta ühik: ")
    aste=int(input("Millises astmes on ühik?: "))
    meetrid=""
    
    if ühik=="cm" and aste==1:
        ühik="m"
        num=round(num*0.01, 5)
        meetrid=str(num)+ühik
    elif ühik=="cm" and aste==2:
        ühik="m^2"
        num=round(num*(0.01)**2, 5)
        meetrid=str(num)+ühik
    elif ühik=="cm" and aste==3:
        ühik="m^3"
        num=round(num*(0.01)**3, 5)#round(number, mitu kohta ümardan)
        meetrid=str(num)+ühik
    
    
    if ühik=="dm" and aste==1:
        ühik="m"
        num=round(num*0.1, 5)
        meetrid=str(num)+ühik
    elif ühik=="dm" and aste==2:
        ühik="m^2"
        num=round(num*(0.1)**2, 5)
        meetrid=str(num)+ühik
    elif ühik=="dm" and aste==3:
        ühik="m^3"
        num=round(num*(0.1)**3, 5)#round(number, mitu kohta ümardan)
        meetrid=str(num)+ühik
    
    
    if ühik=="km" and aste==1:
        ühik="m"
        num=round(num*1000, 5)
        meetrid=str(num)+ühik
    elif ühik=="km" and aste==2:
        ühik="m^2"
        num=round(num*(1000)**2, 5)
        meetrid=str(num)+ühik
    elif ühik=="km" and aste==3:
        ühik="m^3"
        num=round(num*(1000)**3, 5)#round(number, mitu kohta ümardan)
        meetrid=str(num)+ühik
    
    
    if ühik=="mm" and aste==1:
        ühik="m"
        num=round(num*0.001, 5)
        meetrid=str(num)+ühik
    elif ühik=="mm" and aste==2:
        ühik="m^2"
        num=round(num*(0.001)**2, 5)
        meetrid=str(num)+ühik
    elif ühik=="mm" and aste==3:
        ühik="m^3"
        num=round(num*(0.001)**3, 5)#round(number, mitu kohta ümardan)
        meetrid=str(num)+ühik
    print(meetrid)
    
def meetrid_vol2(): #ühikute teisendamine meetriteks, ruutmeetriteks, kuupmeetriteks jne.
    num=float(input("Sisesta suurus: "))
    ühik=input("Sisesta ühik (mm, cm, dm, km): ")
    aste=int(input("Millises astmes on ühik?: "))
    meetrid=""
    
    if ühik=="cm":
        ühik_cm=("m^"+str(aste))
        num_cm=round(num*(0.01)**(aste), 5)
        meetrid=str(num_cm)+ühik_cm
    elif ühik=="dm":
        ühik_dm=("m^"+str(aste))
        num_dm=round(num*(0.1)**(aste),5)
        meetrid=str(num_dm)+ühik_dm
    elif ühik=="km":
        ühik_km=("m^"+str(aste))
        num_km=round(num*(1000)**(aste), 5)
        meetrid=str(num_km)+ühik_km
    elif ühik=="mm":
        ühik_mm=("m^"+str(aste))
        num_mm=round(num*(1000)**(aste), 5)
        meetrid=str(num_mm)+ühik_mm
    print(str(num)+ühik+"^"+str(aste)+" on võrdne "+ meetrid) # Nagu näha, on see kood palju lühem kui eelmine.