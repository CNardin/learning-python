
import numpy as np

"""
RESTITUISCE una NUOVA matrice numpy che ha i numeri della matrice numpy 
di input ruotati di una colonna. 

Per ruotati intendiamo che:
- se un numero nella matrice di input si trova alla colonna j, nella matrice 
di output si troverà alla colonna j+1 nella stessa riga.
- Se un numero si trova nell'ultima colonna, nella matrice di output 
si troverà nella colonna zeresima.

Esempio:

Se abbiamo come input 

np.array(   [
                [0,1,0],
                [1,1,0],
                [0,0,0],
                [0,1,1]
            ])

Ci aspettiamo come output

np.array(   [
                [0,0,1],
                [0,1,1],
                [0,0,0],
                [1,0,1]
            ])

"""
def matrot(matrice):
    # scrivi qui


# INIZIO TEST - NON TOCCARE !

m1 = np.array(  [
                    [1]
                ])
mat_attesa1 = np.array( [
                            [1]
                        ])

assert np.allclose(matrot(m1), mat_attesa1)

m2 = np.array(  [
                    [0,1]
                ])
mat_attesa2 = np.array( [
                            [1,0]
                        ])
assert np.allclose(matrot(m2), mat_attesa2)

m3 = np.array(  [
                    [0,1,0]
                ])
mat_attesa3 = np.array(
                [
                    [0,0,1]
                ])

assert np.allclose(matrot(m3), mat_attesa3)

m4 = np.array(  [ 
                    [0,1,0],
                    [1,1,0]
                ])
mat_attesa4 = np.array( [
                            [0,0,1],
                            [0,1,1]
                        ])
assert np.allclose(matrot(m4), mat_attesa4)


m5 = np.array([
                [0,1,0],
                [1,1,0],
                [0,0,0],
                [0,1,1]
              ])
mat_attesa5 = np.array([
                        [0,0,1],
                        [0,1,1],
                        [0,0,0],
                        [1,0,1]
                       ])
assert np.allclose(matrot(m5), mat_attesa5)
# FINE TEST
