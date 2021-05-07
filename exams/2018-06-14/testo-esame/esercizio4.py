

'''
Esercizio 4

ATTENZIONE: IN QUESTO ESERCIZIO DEVE ESSERE UTILIZZATO NUMPY

Data una matrice 2n * 2n, dividere la matrice in 4 parti quadrate uguali 
(vedi esempio per capire meglio) e RESTITUIRE una NUOVA matrice 2 * 2
contente la media di ogni quadrante

Si assume che la matrice sia sempre di dimensioni pari

SUGGERIMENTO: per dividere per 2 e ottenere un numero intero, usare l'operatore // 


Esempio:

 1, 2 , 5 , 7
 4, 1 , 8 , 0
 2, 0 , 5 , 1 
 0, 2 , 1 , 1 

si divide in 

  1, 2 | 5 , 7
  4, 1 | 8 , 0
----------------- 
  2, 0 | 5 , 1 
  0, 2 | 1 , 1 

e si restituisce 

  (1+2+4+1)/ 4  | (5+7+8+0)/4                        2.0 , 5.0 
  -----------------------------            =>        1.0 , 2.0 
  (2+0+0+2)/4   | (5+1+1+1)/4  


'''

import numpy as np

def quadranti(matrice):
    
    # scrivi qui


    
         
# INIZIO TEST - NON TOCCARE !

assert np.allclose(
    quadranti(np.array([
                          [3.0, 5.0],
                          [4.0, 9.0],
                       ])),
              np.array([
                          [3.0, 5.0],
                          [4.0, 9.0],
                       ])
      )

assert np.allclose(
    quadranti(np.array([    
                         [1.0, 2.0 , 5.0 , 7.0],
                         [4.0, 1.0 , 8.0 , 0.0],
                         [2.0, 0.0 , 5.0 , 1.0], 
                         [0.0, 2.0 , 1.0 , 1.0]    
                       ])), 
              np.array([ 
                         [2.0, 5.0],
                         [1.0, 2.0]
                       ])) 

# FINE TEST
