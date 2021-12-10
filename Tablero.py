from Vacio import Vacio

class Tablero(object):

  """
  :version:
  :author:
  """

  """ ATTRIBUTES

  celdas  (private)

  """

  def __init__(self, filas, columnas):
    self.__filas = filas
    self.__columnas = columnas
    self.__celdas =  [[Vacio("_")  for x in range(filas)] for i in range(columnas)]

  
  def get_celdas(self):
        return self.__celdas 

  def mostrarTablero(self):
        str = ""
        for i in range(self.__filas):
              for j in range(self.__columnas):
                  str+=(self.__celdas[i][j].mostrarImagen())
                  if(j == self.__columnas-1):
                        str += "\n"
        print(str)

  def ponerObjetoPosicion(self, obj, i, j):
        if((i < self.__filas) and (j < self.__columnas)):
              self.__celdas[i][j] = obj
        else:
              print("Esta fuera de rango")

  def moverObjeto(self, i_inicial, j_inicial, i_final, j_final):
    """
     

    @param Objeto estado_inicial : 
    @param Objeto estado_final : 
    @return  :
    @author
    """
    pass



