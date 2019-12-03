import random
import statistics

menu = ['Generuj nowa tablice','Zaladuj tablice','Wyjdz']

while True:
    print ("1. Generuj nowa tablice", "\n2. Zaladuj tablice", "\n3. Wyjdz", "\n")
    
    wybor = int(input("Twój wybór: "))
    
    opcja = list(range(1, 4))
    if wybor in opcja:
        
        if wybor == 1:
            
            print ("\nWybrano nowa tablice")
            
            n = int(input("\nPodaj rozmiar tablicy:"))
            
            my_randoms = random.sample(range(1, 100), n)
            
            print (my_randoms)
            
            print (sorted(my_randoms))

            srednia = statistics.mean(my_randoms)

            print("Max:", max(my_randoms), "\nMin:", min(my_randoms),"\nAverage:", srednia)
            
            print ("\nCzy chcesz zachowac ta tablice? tak/nie")
            
            zapis = input()
            
            if zapis == "tak":
                for line in my_randoms:
                    f = open("tablica.txt", "w+")
                    f.write(str(my_randoms))
                f.close()
                print("tablica zapisana!")
                
            if zapis == "nie":
                continue
              
        if wybor == 2:
            f = open("tablica.txt", "r")
            stara_tablica = f.read()
            print(stara_tablica)
    
        if wybor == 3:
            print("\nDo widzenia!")
            quit(0)
    else:
        print ("Niepoprawna komenda!")