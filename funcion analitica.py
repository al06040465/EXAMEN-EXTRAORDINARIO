def es_palindromo(texto):
  texto = texto.lower().replace(" " , "")
  texto_invertido = texto[::-1]
  return texto == texto_invertido

cadena = input("ingresa un texto: ")

if es_palidromo(cadena)
   print("es un palidromo")
else:
  print("no es un palidromo")
