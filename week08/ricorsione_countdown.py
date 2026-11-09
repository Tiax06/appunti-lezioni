#countdown

from time import sleep

def countdown(n):
    if n==0:
        return
    else:
        print(n)
        sleep(1)
        print(f"chiamo la funzione con {n-1}")
        countdown(n-1)
        print("esco dalla funzione")     #questo verrà printato alla fine per tutte le volte che ho richiamato la funzione

countdown(10)
print("finito")



