#binomiale

c = 0

def binomial(n, m):
    if m==n or m==0:
        return 1
    else:
        global c
        c = c+1
        return binomial(n-1,m-1) + binomial(n-1, m)

b = binomial(7, 5)
print(b)


#il prof ha installato il pacchetto scipy e poi ha importato. vedi nella week08 il codice