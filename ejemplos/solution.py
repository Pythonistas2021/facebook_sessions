import imageio
import numpy as np


def leer_imagen(ruta):
    """
    La función leer_imagen recibe un string con la ruta
    de una imagen en formato BMP y retorna una lista de
    tres dimensiones con el mapa de bits de la imagen.
    Asimismo, convertimos la lista de numpy a una lista
    común y corriente.
    """
    np_array = np.array(imageio.imread(ruta), dtype='int')
    # noinspection PyTypeChecker
    lista_3d = np_array.tolist()
    return lista_3d


def guardar_imagen(ruta, lista_3d):
    """
    La función guardar_imagen recibe una lista de 3
    dimensiones con el mapa de bits de la imagen
    y retorna la imagen en formato bmp.
    """
    return imageio.imwrite(ruta, np.array(lista_3d, dtype='uint8'))

class Solution:

    def aplicar_escala_de_grises(self, lista_3d=leer_imagen('foto_utec.bmp')):
        result = lista_3d
        
        # SU SOLUCION EMPIEZA AQUI
        for matrix_2d in result:
          for matrix_1d in matrix_2d:
            suma = round(sum(matrix_1d)/3, 0)
            matrix_1d[0] = suma
            matrix_1d[1] = suma
            matrix_1d[2] = suma

        # SU SOLUCION TERMINA AQUI
        return result

    def aplicar_sepia(self, lista_3d=leer_imagen('foto_utec.bmp')):
        result = lista_3d
        # SU SOLUCION EMPIEZA AQUI
        for matrix_2d in result:
          for matrix_1d in matrix_2d:
            sepia_R = round(0.393*matrix_1d[0] + 0.769 * matrix_1d[1] + 0.189 * matrix_1d[2],0)
            sepia_G = round(0.349*matrix_1d[0] + 0.686 * matrix_1d[1] + 0.168 * matrix_1d[2],0)
            sepia_B = round(0.272*matrix_1d[0] + 0.534 * matrix_1d[1] + 0.131 * matrix_1d[2],0)

            if sepia_R > 255:
              sepia_R = 255
            if sepia_G > 255:
              sepia_G = 255
            if sepia_B > 255:
              sepia_B = 255
            matrix_1d[0] = sepia_R
            matrix_1d[1] = sepia_G
            matrix_1d[2] = sepia_B
        # SU SOLUCION TERMINA AQUI
        return result

    def aplicar_reflejo_horizontal(self, lista_3d=leer_imagen('foto_utec.bmp')):
        result = lista_3d
        
        # SU SOLUCION EMPIEZA AQUI
        for i in range(len(result)):
          result[i] = result[i][::-1]

        # SU SOLUCION TERMINA AQUI
        return result

    def aplicar_difuminado(self, lista_3d=leer_imagen('foto_utec.bmp')):
        result = lista_3d
        # SU SOLUCION EMPIEZA AQUI
        matriz = []
        for i in range(len(result)):
          matriz2d = []
          for j in range(len(result[i])):
            fila = []
            for k in range(len(result[i][j])):
              if i == 0 and j == 0:
                suma = round((result[i][j][k] + result[i][j+1][k] + result[i+1][j][k] + result[i+1][j+1][k])/4, 0)
                fila.append(suma)
              elif i == 0 and j == len(result[i]) - 1:
                suma = round((result[i][j][k] + result[i+1][j][k] + result[i][j-1][k] + result[i+1][j-1][k])/4, 0)
                fila.append(suma)
              elif i == len(result) - 1 and j == 0:
                suma = round((result[i][j][k] + result[i-1][j][k] + result[i][j+1][k] + result[i-1][j+1][k])/4, 0)
                fila.append(suma)
              elif i == len(result) - 1 and j == len(result[i]) - 1:
                suma = round((result[i][j][k] + result[i-1][j][k] + result[i][j-1][k] + result[i-1][j-1][k])/4, 0)
                fila.append(suma)
              elif i == 0 and j  > 0 and j < len(result[i]) - 1:
                suma = round((result[i][j][k] + result[i][j+1][k] + result[i+1][j][k] + result[i][j-1][k] + result[i+1][j-1][k]+result[i+1][j+1][k])/6, 0)
                fila.append(suma)
              elif i > 0 and j  == 0 and i < len(result) - 1:
                suma = round((result[i][j][k] + result[i-1][j+1][k] + result[i][j+1][k] + result[i+1][j+1][k] + result[i+1][j][k]+result[i][j][k])/6, 0)
                fila.append(suma)
              elif i == len(result) - 1 and j  > 0 and j < len(result[i]) - 1:
                suma = round((result[i][j][k] + result[i-1][j-1][k] + result[i-1][j][k] + result[i-1][j+1][k] + result[i][j+1][k]+result[i][j][k])/6, 0)
                fila.append(suma)

              elif i > 0 and j  == len(result[i]) - 1 and i < len(result) - 1:
                suma = round((result[i][j][k] + result[i-1][j-1][k] + result[i][j-1][k] + result[i+1][j-1][k] + result[i+1][j][k]+result[i][j][k])/6, 0)
                fila.append(suma)
              else:
                suma = round((result[i][j][k] + result[i-1][j][k] + result[i-1][j+1][k] + result[i][j+1][k] + result[i+1][j+1][k]+result[i+1][j][k] + \
                result[i+1][j-1][k] + result[i][j-1][k] + result[i][j][k])/9, 0)
                fila.append(suma)
            matriz2d.append(fila)
        matriz.append(matriz2d)
        # SU SOLUCION TERMINA AQUI
        return result
