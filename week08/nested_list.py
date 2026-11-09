#le nested list non sono molto consigliate

#la funzione type vi dice che tipo sia un oggetto
def count_leaves(input_list): #conta le foglie(elmenti della lista)
    if len(input_list)==0:
        return
    else:
        counter = 0
        for element in input_list:
            if type(element) == list: #se ciò con cui sto lavorando è una lista di python
                counter = counter + count_leaves(element)
            else:
                counter+=1
        return counter
    

names = ["Adam", ["Bob", ["Chet", "Cat"], "Barb", "bert"], "Alex", ["Bea", "Bill"], "Ann"]

result = count_leaves(names)
print(result)