import sys
while True:
    choice = input ("Ciao, qui puoi generare un nome per la band. Premi S per iniziare on N per uscire: ")
    if choice.lower() == "s":
        print("Sta iniziando...")
        hometown = input ("Come si chiama la tua citta' natale? ")
        pet = input ("Come si chiama la tuo animale domestico? ")
        print(f"Il nome della band generato per te e': {hometown} {pet}")
        break 
    elif choice.lower() == "n":
        print("Uscita...")
        break
    else:
    
        while True:
            retry = input ("Hai inserito un input non valido. Vuoi continuare?(S/N) ")
            if retry.lower() == "s":
                break
            elif retry.lower() == "n":
                sys.exit()       
            else:
                print("Inoltro...")         