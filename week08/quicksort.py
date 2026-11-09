class Quicksort():
    def sort(self, sequenza):
        if len(sequenza) <= 1:
            return sequenza
        else: #faccio la ricorsione
            # 1) scelgo il pivot
            pivot = sequenza[0]

            # 2) dividere la sequenza in sottosequenze
            sequenza_minori = []
            for i in range(1, len(sequenza)):
                if sequenza[i] < pivot:
                    sequenza_minori.append(sequenza[i])
            #posso/devo fare lo stesso per le sequenze maggiore e uguali
            sequenza_maggiori = [n for n in sequenza if n > pivot] #usando la list comprehension
            sequenza_uguali = [n for n in sequenza if n == pivot]

            # 3) chiamo sort() su sottoseqenza e riassemblo
            return self.sort(sequenza_minori) + sequenza_uguali + self.sort(sequenza_maggiori)

qs = Quicksort()
sequenza = [3, 7, 11, 2, 5, 9 , 4 ,7]
print(qs.sort(sequenza))