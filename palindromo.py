word = input("Inserta una palabra")
if str(word) == "".join(reversed(word)):
    print("Es un Palindromo")
else:
    print("No es un Palindromo")



# el codigo de abajo es de cisco:

#text = input("Ingresa un texto: ")

# Quitar todos los espacios...
#text = text.replace(' ','')

# ... y revisar si la palabra es igual en ambos sentidos
#if len(text) > 1 and text.upper() == text[::-1].upper():
	#print("Es un palíndromo")
#else:
	#print("No es un palíndromo")
