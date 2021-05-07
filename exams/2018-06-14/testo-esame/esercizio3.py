'''
Esercizio 3

ATTENZIONE: IN QUESTO ESERCIZIO NUMPY NON DEVE ESSERE UTILIZZATO 

RESTITUISCE True se la matrice come lista di liste in input è Toeplitz, mentre RESTITUISCE False se non lo è.

Una matrice è Toeplitz se e solo se tutti gli elementi su ogni diagonale contiene gli stessi elementi.

assumiamo che la matrice contenga sempre almeno una riga di almeno un elemento


SUGGERIMENTO: usare due for, nel primo scorrere la matrice per righe, nel secondo per colonne

Chiedersi: 
- da che riga occorre partire per la scansione? La prima è utile?
- da che colonna occorre partire per la scansione? La prima è utile?
- se scorriamo le righe dalla prima verso l'ultima e stiamo esaminando un certo 
  numero ad una certa riga, che condizione deve rispettare quel numero
  affinchè la matrice sia toepliz ?

ESEMPIO:

matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]

1 2 3 4
5 1 2 3
9 5 1 2

Su ogni diagonale ci sono gli stessi numeri e quindi viene restituito True

1 2 3 4
5 1 4 3
9 3 1 2

Restituisce False. Ci sono due diagonali con numeri diversi: (5,3) e (2,4,2)

'''

def toepliz(matrix):
    # scrivi qui

  
  
# INIZIO TEST - NON TOCCARE !  
assert toepliz([[1]]) == True
assert toepliz([[3,7],
                [5,3]]) == True
assert toepliz([[3,7],
                [3,5]]) == False
assert toepliz([[3,7],
                [3,5]]) == False
assert toepliz([[3,7,9],
                [5,3,7]]) == True
assert toepliz([[3,7,9],
                [5,3,8]]) == False

assert toepliz([[1,2,3,4],
                [5,1,2,3],
                [9,5,1,2]]) == True

assert toepliz([[1,2,3,4],
                [5,9,2,3],
                [9,5,1,2]]) == False
# FINE TEST
