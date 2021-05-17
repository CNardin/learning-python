import numpy as np

# Matrice di partenza
m = np.array( 
    [ 
#         0         1         2      
#        Gilberto   Rocky     Clelia
        [5.0,       8.0,      1.0],   # 0 Thè
        [7.0,       3.0,      2.0],   # 1 Caffè
        [9.0,       2.0,      8.0]    # 2 Ginseng
    ]
)

nomi = ["Gilberto","Rocky","Clelia"]
#print(nomi[0])
bevande = ["Thè","Caffè","Ginseng"]

print("-"*55)
print("Matrice Nomi vs Bevande \n",m)
print("-"*55)

# Spesa dei singoli fruitori di bevande
num_righe, num_colonne = m.shape
somma = []
for col in range(0, num_colonne):
  spesa_col = m[:,col:col+1]
  somma_temp = np.sum(spesa_col)
  somma.append(somma_temp)

print("Spesa di ciascuno: \n Gilberto, Rocky, Clelia \n" , somma)
print("-"*55)

# Alternativa 1: non piace print 
spendaccione = np.array(somma)
index_spendaccione = np.where(spendaccione.max())
print("Prima alternativa di output:\n")
print("Dei tre ha speso di più il numero:",index_spendaccione, ", per un totale di: ",spendaccione[index_spendaccione],"\n")

# Alternativa 2
#l = [1,2,3,4,5] # Python list
#a = np.array(l) # NumPy array
spesePC = np.array(somma)
indicePCmaggiore = spesePC.tolist().index(spesePC.max()) # return index of max PC
print("Seconda alternativa di output:\n")
print("Dei tre ha speso di più il numero:",indicePCmaggiore, ", per un totale di: ",spesePC[indicePCmaggiore],"\n")

# Alternativa 3
print("Dei tre ha speso di più:",nomi[indicePCmaggiore], ", per un totale di: ",spesePC[indicePCmaggiore],"\n")
print("-"*55)


# Spesa singole bevande
somma = []
for riga in m:
  somma_temp = np.sum(riga)
  somma.append(somma_temp)

print("Spesa per tipo: \n Thé, Caffé, Ginseng \n" , somma)
print("-"*55)

speseBEV = np.array(somma)
indiceBEV = speseBEV.tolist().index(speseBEV.max())
print("La bevanda preferita è la numero:",indiceBEV,", per un costo di: ",speseBEV[indiceBEV])
print("-"*55)

print("La bevanda preferita è:",bevande[indiceBEV],", per un costo di: ",speseBEV[indiceBEV])
print("-"*55)
