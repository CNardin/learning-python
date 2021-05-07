"""
Quando si analizza una frase, può essere utile processarla per rimuovere parole molto comuni, 
come articoli e le preposizioni:

Per esempio:

  "un libro su Python per principianti" 
   
  si può semplificare in 

      "libro Python principianti"

Le parole 'poco utili' vengono chiamate 'stopwords'. Questo processo è per esempio eseguito dai motori di ricerca per ridurre la complessità della stringa di input fornita dall'utente.

Implementare una funzione che prende una stringa e RITORNA la stringa di input senza le stopwords

SUGGERIMENTO 1: le stringhe in Python sono *immutabili* ! Per rimuovere le parole dovete creare una 
_nuova_ stringa a partire dalla stringa di partenza. 
 
SUGGERIMENTO 2: create una lista di parole così:
    lista = stringa.split(" ")

SUGGERIMENTO 3: operate le opportune trasformazioni su lista, e poi costruite la stringa da restituire con  
    " ".join(lista)
"""
def nostop(stringa, stopwords):
    # scrivi qui


# INIZIO TEST - NON TOCCARE !
assert nostop("un", ["un"]) == ""
assert nostop("un", []) == "un"
assert nostop("", []) == ""
assert nostop("", ["un"]) == ""
assert nostop("un libro", ["un"]) == "libro"
assert nostop("un libro su Python", ["un","su"]) == "libro Python"
assert nostop("un libro su Python per principianti", ["un","uno","il","su","per"]) == "libro Python principianti"
# FINE TEST