# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 15:04:01 2020

@author: artur
"""


import random

def Harjutus_1():
    # Display 10 random numbers from interval [0,1)
    for i in range(10):
        print(random.random())
    

def Harjutus_2():
    # Generate random numbers from an interval of [3,7)
    # Lets write a function for this. Kuigi on täitsa olemas eraldi funktsioon selle jaoks, nimelt: random.uniform()
    
    def my_random():
        # Random, scale, shift, return...
        return 4*random.random()+3 #valime random numbri, korrutame 4-ga et scale'ida. Liidame kolme juurde et nihutada väärtusi 3 ühiku võrra.
    for i in range(10):
        print(my_random())
        
def Harjutus_3():
    # Kasutame seekord random.uniform() käsku.
    for i in range(10):
        print(random.uniform(3,7))
        
def Harjutus_4(): # Normal Distribution ehk "Bell Curve".
    # Kasutame normalvariate(müü, sigma) funktsiooni. Kus "müü" on keskväärtus ning "sigma" on standardhälve.
    
    for i in range(20):
        print(random.normalvariate(0, 1))
    print("")
    print("Jaotame need 5 ümber.\n")
    for i in range(20):
        print(random.normalvariate(5, 1))
    
def Harjutus_4_1(): # Siin tahtsin leida 20 random numbri keskväärtuse.
    minu_list=[]
    for i in range(20):
        a=random.normalvariate(7, 0.1)
        print(a)
        minu_list.append(a)
    print("Minu keskväärtus on: "+ str(sum(minu_list)/len(minu_list))) # Katse standardhälvet. On lihtne näha, et kui standardhälve on suurem, siis on keskväärtus ka rohkem mööda pandud. Proovi näiteks standardhälvet 0.1 ja 10.
    
def Harjutus_5(): # Uurime diskreetseid suurusi. Ehk ainult täisarvud.
    for i in range(20):
        print(random.randint(1,6))
    
def Harjutus_6(): #Pick random objects from a list.
    # for i in range(10):
    #     tulemus=random.randint(1,3)
    #     if tulemus == 1:
    #         print("Kivi")
    #     elif tulemus==2:
    #         print("Paber")
    #     elif tulemus==3:
    #         print("Käärid")
    #     else:
    #         print("Midagi läks valesti!")   # See on alternatiivne lahendus, aga veidi pikkem!
            
    tulemused=["Kivi", "Käärid", "Paber"]
    for i in range(10):
        print(random.choice(tulemused))
        
def Projekt_Sündmused():
    from matplotlib import pyplot as plt
    
    # Koostame sündmuste jaotus graafikud. Kasuta selle jaoks matplotlib libraryt.
    katsed= 10
    tulemused=[]
   
    for i in range(katsed):
        a=random.randint(1,6) # Täringut veeretades random tulemus.
        tulemused.append(a) #Lisame järjest tulemused listi.
    # print(tulemused)
    plt.hist(x=tulemused, bins=[1,2,3,4,5,6,7], edgecolor="black")
    plt.tight_layout()
    plt.show()


def KiviPaberKääridJaotus():
    from matplotlib import pyplot as plt
    from collections import Counter
    katsed=10000
    valikud=["Kivi","Paber","Käärid"]
    kogum=[]
    for i in range(katsed):
        a=random.choice(valikud)
        kogum.append(a)
    loend=Counter(kogum)
    uusloend=loend.most_common(3)
    
    x=[]
    y=[]
    for item in uusloend:
        x.append(item[0])
        y.append(item[1])
        
    plt.bar(x, y, edgecolor="black")
    plt.tight_layout()
    plt.show()
    
def KiviPaberKäärid_text_kuju():
    
    from matplotlib import pyplot as plt
    from collections import Counter
    

    valikud=["Kivi", "Paber", "Käärid"]
    
    for i in range(10):
        player1_valik=random.choice(valikud)
        player2_valik=random.choice(valikud)
        
        if player1_valik=="Kivi":
            if player2_valik=="Paber":
                print("Mängija 2 võitis!")
            elif player2_valik=="Käärid":
                print("Mängija 1 võitis!")
            elif player2_valik==player1_valik: #Võib ka lihtsalt lõpetada else käsuga.
                print("1. Jäite viiki!")
                
        elif player1_valik== "Paber":
            if player2_valik=="Kivi":
                print("Mängija 1 võitis!")
            elif player2_valik=="Käärid":
                print("Mängija 2 võitis!")
            else:
                print("2. Jäite viiki!")
                
        elif player1_valik=="Käärid":
            if player2_valik=="Paber":
                print("Mängija 1 võitis!")
            elif player2_valik=="Kivi":
                print("Mängija 2 võitis!")
            else:
                print("3. Jäite viiki!")
                
def KiviPaberKäärid_distribution():
    
    from matplotlib import pyplot as plt
    from collections import Counter
    
    valikud=["Kivi", "Paber", "Käärid"]
    tulemused=[]
    for i in range(1000):
        player1_valik=random.choice(valikud)
        player2_valik=random.choice(valikud)
        
        if player1_valik=="Kivi":
            if player2_valik=="Paber":
                tulemused.append("Player 2")
            elif player2_valik=="Käärid":
                tulemused.append("Player 1")
            elif player2_valik==player1_valik: #Võib ka lihtsalt lõpetada else käsuga.
                tulemused.append("Viik")
                
        elif player1_valik== "Paber":
            if player2_valik=="Kivi":
                tulemused.append("Player 1")
            elif player2_valik=="Käärid":
                tulemused.append("Player 2")
            else:
                tulemused.append("Viik")
                
        elif player1_valik=="Käärid":
            if player2_valik=="Paber":
                tulemused.append("Player 1")
            elif player2_valik=="Kivi":
                tulemused.append("Player 2")
            else:
                tulemused.append("Viik")
    # print(tulemused)
    tulemused=Counter(tulemused)
    graafiku_andmed=tulemused.most_common(3)
    print(graafiku_andmed)
    
    x=[]
    y=[]
    for asi in graafiku_andmed:
        x.append(asi[0])
        y.append(asi[1])
    plt.bar(x,y,edgecolor="black")
    plt.tight_layout()
    plt.show()    
    

def KiviPaberKäärid3():
    
    
    from matplotlib import pyplot as plt
    from collections import Counter
    
    valikud=["Kivi", "Paber", "Käärid"]
    tulemused=[]
    for i in range(100000):
        player1_valik=random.choice(valikud)
        player2_valik=random.choice(valikud)
        player3_valik=random.choice(valikud)
        if player1_valik=="Kivi":
            if player2_valik=="Paber":
                if player3_valik=="Paber":
                    tulemused.append("Viik") # NB! loogika
                elif player3_valik=="Käärid":
                    tulemused.append("Viik")
                elif player3_valik=="Kivi":
                    tulemused.append("Player 2")
                    
            elif player2_valik=="Käärid":
                if player3_valik=="Paber":
                    tulemused.append("Viik")
                elif player3_valik=="Kivi":
                    tulemused.append("Viik") #NB! Loogika!
                elif player3_valik=="Käärid":
                    tulemused.append("Player 1")
                    
            elif player2_valik=="Kivi":
                if player3_valik=="Kivi":
                    tulemused.append("Viik")
                elif player3_valik=="Paber":
                    tulemused.append("Player 3")
                elif player3_valik=="Käärid":
                    tulemused.append("Viik") # Siin on loogika viga, player 3 langeks välja, aga esimesed 2 jääksid viiki. Ehk player 1 ja player 2 re-rollivad?
                
        elif player1_valik== "Paber":
            if player2_valik=="Kivi":
                if player3_valik=="Kivi":
                    tulemused.append("Player 1")
                elif player3_valik=="Paber":
                    tulemused.append("Viik") # NB! Loogika!
                elif player3_valik=="Käärid":
                    tulemused.append("Viik")
            elif player2_valik=="Käärid":
                if player3_valik=="Kivi":
                    tulemused.append("Viik")
                elif player3_valik=="Käärid":
                    tulemused.append("Viik") #NB! Loogika!
                elif player3_valik=="Paber":
                    tulemused.append("Player 2")
            elif player2_valik=="Paber":
                if player3_valik=="Kivi":
                    tulemused.append("Viik") #NB! Loogika!
                elif player3_valik=="Käärid":
                    tulemused.append("Player 3")
                elif player3_valik=="Paber":
                    tulemused.append("Viik")
                
        elif player1_valik=="Käärid":
            if player2_valik=="Paber":
                if player3_valik=="Kivi":
                    tulemused.append("Viik")
                elif player3_valik=="Käärid":
                    tulemused.append("Viik") #NB! Loogika!
                elif player3_valik=="Paber":
                    tulemused.append("Player 1")
            elif player2_valik=="Kivi":
                if player3_valik=="Kivi":
                    tulemused.append("Viik") #NB! Loogika!
                elif player3_valik=="Käärid":
                    tulemused.append("Player 2")
                elif player3_valik=="Paber":
                    tulemused.append("Viik")
            elif player2_valik=="Käärid":
                if player3_valik=="Kivi":
                    tulemused.append("Player 3")
                elif player3_valik=="Käärid":
                    tulemused.append("Viik") 
                elif player3_valik=="Paber":
                    tulemused.append("Viik") #NB! Loogika
                
    # print(tulemused)
    tulemused=Counter(tulemused)
    graafiku_andmed=tulemused.most_common(4)
    print(graafiku_andmed)
    
    x=[]
    y=[]
    for asi in graafiku_andmed:
        x.append(asi[0])
        y.append(asi[1])
    plt.bar(x,y,edgecolor="black")
    plt.tight_layout()
    plt.show()
    

    