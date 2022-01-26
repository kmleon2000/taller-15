def es_par(n):
  """ Imprimir por pantalla si el número es par
  >>> es_par(1)
  False

  >>> es_par(2)
  True

  >>> es_par(3)
  False

  >>> es_par(4)
  True
  """
  return n % 2 == 0

def es_primo(n):
  """ Imprimir por pantalla si el número es primo
  >>> es_primo(2)
  True

  >>> es_primo(3)
  True

  >>> es_primo(4)
  False

  >>> es_primo(29)
  True

  >>> es_primo(30)
  False
  """
  
  for j in range(2,n):
    if n % j == 0:
      return False
  return True

def imprimir_secuencia(n):
  """ Imprimir por pantalla los número de 1 hasta:
  - 10 veces el número si este es menor a 50, excluyendo los múltiplos del número.
  - 5 veces el número si este es mayor a 50.

  >>> imprimir_secuencia(14)
  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139]

  >>> imprimir_secuencia(60)
  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300]

  >>> imprimir_secuencia(0)
  'Error: El número no debe ser menor a 1'
  """
  
  num = []

  if n > 0:
    if n < 50:
      for j in range(1, (10 * n) + 1):
        if not j % n == 0:
          num.append(j)
    else:
      for j in range(1, (5 * n) + 1):
        num.append(j)
    return num
  return 'Error: El número no debe ser menor a 1'

def imprimir_tabla(n):
  """ Imprimir la tabla de multiplicar de 1 hasta 50 de ese número.
  """
  print('Tabla del', n, 'del 1 hasta el 50:')
  for i in range(1,51):
    print(n, '*', i , '=', n * i)

number = int(input('Por favor digite un número: '))

print('Es par?',es_par(number))
print('Es primo?',es_primo(number))
print('Secuencia:',imprimir_secuencia(number))
imprimir_tabla(number)