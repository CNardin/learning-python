# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------
# # ESERCIZIO 4:

# def max_len_str(phrase):
# 	parser = frase.split(" ")
# 	length_parser = []
# 	for word in parser:
# 		lenword = len(word)
# 		length_parser.append(lenword)

# 	print(length_parser)
# 	max_value = max(length_parser)
# 	print(max_value)
# 	return max_value

# frase = "La strada si inerpica lungo il ciglio della montagna" # 8
# frase = "Il temibile pirata Le Chuck dominava spietatamente i mari del Sud"  # 13
# frase = "Praticamente ovvio" # 12

# max_len_str(frase)

# max([len(parola) for parola in frase.split()])

# # -------------------------------------------------------------------------------------
# # -------------------------------------------------------------------------------------
# # # ESERCIZIO 4:

# lista = [0, 0, 0, 0, 4, 0, 0, 0, 0] # -> [0, 1, 2, 3, 4, 3, 2, 1, 0]
# #lista = [0, 0, 0, 3, 0, 0, 0]      # -> [0, 1, 2, 3, 2, 1, 0]
# #lista = [0, 0, 2, 0, 0]            # -> [0, 1, 2, 1, 0]
# #lista = [0]  # -> [0]

# value = max([numero for numero in lista])
# pos = lista.index(value)
# print("Valore: ",value," in posizione: ",pos)
# nlista = []
# l1 = list(range(0,value)) + list(range(value,0,-1))
# print(l1)


# # -------------------------------------------------------------------------------------
# # -------------------------------------------------------------------------------------
# # # ESERCIZIO 4:

stringa,car1,car2 = "accatastare la posta nella stiva", 's','t'  # True
stringa,car1,car2 = "dadaista entusiasta", 's','t'    # False
# stringa,car1,car2 = "barbabietole", 't','o'           # True
# stringa,car1,car2 = "barbabietole", 'b','a'           # False
# stringa,car1,car2 = "a", 'a','b'                      # False
# stringa,car1,car2 = "ab", 'a','b'                     # True
# stringa,car1,car2 = "aa", 'a','b'                     # False

res = True
start_string = stringa
chars_i_want = (car1,car2)
print(chars_i_want)
final_string = ''.join(c for c in start_string if c in chars_i_want)
print(final_string)

if final_string[0] == car2:
	final_string=final_string[1:]

check2 = car1+car2
print(check2)

car = 0
while car+1<len(final_string) and res: 
#for car in range(0,len(final_string),2):
	try:
		temp = final_string[car] + final_string[car+1]		
		car += 1
		if temp != check2:
			res = False
		elif temp == check2:
			res = True
	except Exception:
		res = False

print(res)



# i = 0

# res = True

# if len(stringa) == 1:
#     res = False

# while i + 1 < len(stringa) and res:
#     if stringa[i] == car1 and stringa[i+1] != car2:
#         res = False
#     i += 1

# res