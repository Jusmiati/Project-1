# -*- coding: utf-8 -*-

#PROGRAM UTAMA
from main import yangini
ulang=str("Y")
while(True):
    def kayaknya(n):
        api=yangini()
        if n==1 :
            from tugas1 import inisekalimi
        elif n==2:
                from hastag import masaweh
        elif n==3:
                from Tugas3 import yatawwa
        else :
                print("Salah inputki guys ")    
    print ("1. Soal Nomer 1\n2. Soal Nomer 2\n3. Soal Nomer 3")
    n = int(input('Silahkan Dipilih Guys : '))
    kayaknya(n)
    i = str(input('Ulangi program (Y/n): '))
    if i=="n" :
        break   


        
        
        
        
    