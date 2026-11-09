






class Fibonacci:
    #senza memoization
    def calcola_elemento(self, n):  # lo stato è in n
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.calcola_elemento(n - 1) + self.calcola_elemento(n - 2)

    #con memoization
    def __init__(self):
        # per ottimizzare il tutto è meglio usare la memoization
        #cache per ottimizzare la ricerca dei valori già calcolati
        self.cache = {} #mi creo il dizionario cache per memorizzare i valori ricorrenti
        self.cache[0] = 0
        self.cache[1] = 1

    def calcola_elemento_usando_cache(self, n): #lo stato è in n
        if self.cache.get(n) is not None:
            return self.cache[n]
        else:
            self.cache[n] = (self.calcola_elemento(n-1) + self.calcola_elemento(n-2))
            return self.cache[n]



fib = Fibonacci()
value = fib.calcola_elemento(3)
print(value)
value = fib.calcola_elemento_usando_cache(100)
print(value)


#NB: oppure faccio from functools import lru_cache (funzione vedi nella sua week08)