# # METODI
# "trento".capitalize()
# print("trento".capitalize())
# "trento".upper()
# print("trento".upper())
# "trento".count("t")
# print("trento".count("t"))


# def char3(phrase):
# 	print(phrase)
# 	subdiv = phrase.split(" ")
# 	lastword = subdiv[-1]
# 	numchar = int(subdiv[1])
# 	export = lastword[0:numchar]
# 	return export


# frase = "Prendi 4 lettere"       # lett
# a = char3(frase)
# print(a)

# frase = "Prendere 5 caratteri"  # carat
# a = char3(frase)
# print(a)

# frase = "Take 10 characters"    # characters
# a = char3(frase)
# print(a)

# # scrivi qui




arrivi = ['sedie', 'lampade', 'cavi']  # magazzino diventa:  {'B': 'sedie', 'C': 'lampade', 'F': 'cavi'}
#arrivi = ['caraffe', 'giardinaggio']  # magazzino diventa:  {'D': 'caraffe', 'E': 'giardinaggio'}
#arrivi = ['stufe']                    # magazzino diventa: {'A': 'stufe'}

catalogo = {'stufe' : 'A',
            'sedie' : 'B',
            'caraffe' : 'D',
            'lampade' : 'C',
            'cavi' : 'F',
            'giardinaggio' : 'E'}

magazzino = dict()
for oggetto in arrivi:
#	print("Oggetto: ", oggetto)
	if oggetto in catalogo:
#		print(catalogo[oggetto])
		magazzino[ catalogo[oggetto] ] = oggetto
print(magazzino)
# scrivi qui

