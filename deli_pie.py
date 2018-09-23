#
# Modulo: deli_pi.py
# Descripcion: Modulo con toda la logica de negocio para realizar operaciones
#              CRUD a la base de datos SQLite 'fingers'.
# Autor: Alessandro Chavez
#
import sqlite3


class Fingers():
    '''Clase que maneja todas las operaciones CRUD a alguna base de datos 
    (fingers).'''

    def __init__(self, nombre_bd='fingers.db'):
        '''Constructor de clase Fingers

        Almacena nombre de la base de datos a utilizar, asi como la conexion
        a la base de datos.

        Args:
            nombre_bd (str): nombre del archivo de base de datos para el SQLite.

        Attributes:
            nombre_bd (str): nombre del archivo de base de datos para el SQLite.
            conn (obj): conexion a base de datos SQLite3
        '''
        self.nombre_bd = nombre_bd
        self.conn = sqlite3.connect(self.nombre_bd)

    def execute_query(self, query):
        '''Metodo para ejecutar un query y regresar un diccionario con los
        resultados.

        Args:
            query (str): query a ejecutar

        Returns:
            dict: diccionario con el resultado del query en la llave res
        '''
        tmp_res = self.conn.execute(query)
        res = []
        for item in tmp_res:
            res.append(item[0])
        return {'res': res}

    def get_tables(self):
        '''Metodo para mostrar todas las tablas almacenadas en la base de datos

        El metodo ejecuta un select a todas las tablas disponibles de la base
        de datos que se utilice para saber que tablas contiene

        Args:
            None

        Returns:
            dict: lista de tablas almacenada en la key de res
        '''
        query = "SELECT name FROM sqlite_master WHERE type='table';"
        return self.execute_query(query)


if __name__ == '__main__':
    tmp_obj = Fingers()
    print(tmp_obj.get_tables())
