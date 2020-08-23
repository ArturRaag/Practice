# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 14:33:16 2019

@author: artur
"""

def kalkulaator():
    num1=input("Sisesta mõni number: ")
    num2=input("Sisesta mõni teine number: ")
    tulemus=num1+num2
    print(tulemus) #tulemus on stringina ehk andmetüübiks ei ole number vaid sõna.
    
    #komata arvutamiseks
    num1=input("Sisesta mõni number: ") #Proovige siin sisestada komaga arve nt 3.6 vms. Selgub, et python ümardab need täisarvuks. Ehk kui kirjutasite 3.6 siis ümardab 3-ks.
    num2=input("Sisesta mõni teine number: ")
    tulemus=int(num1)+int(num2)  # int funktsioon teisendab meie praegused sisestatud "string" tüüpi numbrid tõelisteks numbriteks, millega on võimalik arvutusi teha. Paraku aga, ümardab "int" meie numbrid väiksemaks täisarvuks.
    print(tulemus)
    
    #komaga arvutamiseks
    num1=input("Sisesta mõni number: ")
    num2=input("Sisesta mõni teine number: ")   # Siin proovige ka komaga arve. Leiate, et siin komaga arvutamine on täitsa võimalik.
    tulemus=float(num1)+float(num2) #koma arvuks "teisendab" numbri meie funktsioon nimega "float".
    print(tulemus)
    
def kolmnurk():
    alus=float(input("Sisesta kolmnurga alus: "))
    kõrgus=float(input("sisesta kolmnurga kõrgus: ")) # küsime arvulisi väärtusi, aga "input" annab meile teksti tüüpi andmeid, 
                                                      # nii et tuleb andmed muuta numbriliseks floatiga
    
    valem=(alus*kõrgus)/2 #hetkel on see numbriline väärtus ehk float tüüp
    print("Kolmnurga pindala on: "+ str(valem)) #muuda saadud tulemus uuesti stringiks, sest tähti ja numbreid liita ei saa ju.
    
def harjutus1(): #if-statements TRUE/FALSE statements
    # NÄIDE 1
    # Ärkasin ülesse
    # KUI/IF (ma olen näljane)
        # siis ma söön hommikusööki
    # MUUL JUHUL KUI (ei ole näljane ja on kiire)
        # ma ei söö hommikusööki ja lähen otse kooli
    # MUUL JUHUL (ei ole näljane ja kiiret ei ole)
        # kuulan enne tööle minekut raadiot/vaatan telekat/teen trenni
    
    #NÄIDE 2
    # Ma lahkun majast
    # KUI on pilvine
        # ma võttan kaasa vihmavarju
    # muul juhul
        # ma võttan kaasa päikseprillid
      

    on_mees=False                                        #toimib ainult kui väide on tõene, kui väär, ei prindi midagi
    if on_mees :
        print("Sa oled meestsoost.")
    else:
        print("Sa ei ole meestsoost.")
        
def harjutus2():
    sugu=input("Mis sugu oled? Mees või Naine?: ")               #sugu.capitalize() ja sugu.strip(" ")
      #== tähendab IDENTNE                                                           # sugu.strip() võtab ära ees ja taga olevad tühikud.
    if sugu =="Mees":                                             # sugu.replace(" ", "") asendab kõik string tüüpi tühikud tühjade stringidega. Tühi, sest "" sees ei ole ühtegi sümbolit, aga str tüüp ikkagi.
        print("Sa oled meestsoost!")
    elif sugu=="Naine":
        print("Sa oled naissoost!")
    else:
        print("Oled mingi suguta elukas.")
    

def harjutus3():
    sugu=input("Mis sugu oled?: ")     #sugu.capitalize() ja sugu.strip(" ")
    sugu=sugu.capitalize()
    sugu=sugu.replace(" ","") 
                                
    # selline lahend on tegelikult ka vale, sest kui jätta ette tühik, siis see .capitalize funktsioon rakendub tühikule ja sõna jääbki väikse tähega.
       
    if sugu=="Mees":
        print("Sa oled meestsoost!")
    elif sugu=="Naine":
        print("Sa oled naisssoost!")
    else:
        print("Sa oled sugutu elukas...")
    
    
    
    
def harjutus4(): #while loop
    
    i=1
    while i<=10: #hakkab tsüklit täitma, NII KAUA kui väärtus on tõene.
        print(i)
        i =i+1 #tegelikult võib ka kasutada (i += 1) varianti. lühem versioon, aga sama tehe.
    print("Tsükkel on läbitud.")
    
    
def arva_ära():
    
    salasõna="Olevik"
    pakkumine=""
    
    while pakkumine != salasõna:
        pakkumine = input("Lahenda mõistatus: \n\nOlen lõpmata lühike, ja samas lõpmata pikk.\nKes ma olen?: ")            
    print("Tubli!")
    
    
    
    
def arva_ära_vol2():
        
    salasõna="Olevik"
    pakkumine=""
    
    while pakkumine != salasõna:
        pakkumine = input("Lahenda mõistatus: \n\nOlen lõpmata lühike, ja samas lõpmata pikk.\nKes ma olen?: ")
        pakkumine=pakkumine.replace(" ","")
        pakkumine=pakkumine.capitalize()
        if pakkumine != salasõna:
            print("\n Arvasid valesti! Proovi uuesti!\n")
            
    print("Tubli!")

    
    
    
    
    
    
    
    
    
    
    
    
    
    