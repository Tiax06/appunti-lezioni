#parola palindroma

#lavoro per semplicità con lunghezza dispari
def is_palindrome(word):
    if len(word) == 1:
        return True #se sono arrivato qui è palindroma
    else: #se la lettera iniziale e finale sono uguali, allora vado a richiamare la funzione
        return word[0] == word[-1] and is_palindrome(word[1:-1]) #sottostringa da 1 a len-1


parola = input("Parola: ")
result = is_palindrome(parola)
print(result)