"""
ESERCIZIO 2 


INPUT: 
  - frase da arricchire
  - Il sentimento da usare, che è codificato come un valore numerico.
  - un dizionario di sentimenti, in cui si associa al codice numerico 
di ogni sentimento un dizionario contenente un espressione onomatopeica tipica per quel sentimento,
e la posizione in cui deve figurare all'interno di una frase. Le posizioni sono indicate come 'i'
per inizio e 'f' per fine.


OUTPUT

- La frase arricchita con l'espressione onomatopeica scelta in base al sentimento. L'espressione
  va aggiunta sempre prima o dopo la frase, e sempre separata da uno spazio. 



Per esempio

sentimenti = {
                1:  {
                        "espressione": "Gulp!",
                        "posizione": "i"
                    }
                2:  {
                        "espressione": "Sgaragulp !",
                        "posizione": "i"
                    }
                3:  {
                        "espressione": "Uff..",
                        "posizione": "f"
                    }
}


onomat("Ma quelli sono i bassotti!", 1, sentimenti) 

Deve tornare

"Gulp! Ma quelli sono i bassotti!"

Mentre 

onomat("Non voglio alzarmi dall'amaca.", 3, sentimenti) 

Deve tornare 

"Non voglio alzarmi dall'amaca. Uff.."


NOTA: Ricordarsi lo spazio tra espressione e frase!

"""
def onomat(frase, sentimento, sentimenti):
    
    # Scrivi qui



# INIZIO TEST - NON TOCCARE !!!


sentimenti = {
                1:  {
                        "espressione": "Gulp!",
                        "posizione": "i"
                    },
                2:  {
                        "espressione": "Sgaragulp!",
                        "posizione": "i"
                    },
                3:  {
                        "espressione": "Uff..",
                        "posizione": "f"
                    },
                4:  {
                        "espressione": "Yuk yuk!",
                        "posizione": "f"
                    },
                5:  {
                        "espressione": "Sgrunt!",
                        "posizione": "i"
                    },
                6:  {
                        "espressione": "Gasp!",
                        "posizione" : "i"
                    }
            }


assert onomat("Mi chiamo Pippo.", 4, sentimenti) == "Mi chiamo Pippo. Yuk yuk!"
assert onomat("Quel topastro mi ha rovinato un'altra rapina!", 5, sentimenti) == "Sgrunt! Quel topastro mi ha rovinato un'altra rapina!"
assert onomat("Non voglio alzarmi dall'amaca.", 3, sentimenti) == "Non voglio alzarmi dall'amaca. Uff.."

# FINE TEST
