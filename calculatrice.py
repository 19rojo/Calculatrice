def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

if __name__ == "__main__":
    print("--- Ma calculatrice ---")
    print("1. Addition")
    print("2. Soustraction")
    
    choix = input("Choisis une option (1/2):")
    
    try:
        num1 = float(input("Entrer le premier nombre : "))
        num2 = float(input("Entrer le deuxième nombre : "))
        
        if choix == '1':
            print(f"Résultat : {addition(num1, num2)}")
        elif choix == '2':
            print(f"Résultat :{soustraction(num1, num2)}")
        else :
            print("Option invalide.")
    except ValueError :
        print("Erreur : Veuillez entrer des nombres valides.")