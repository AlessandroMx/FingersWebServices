#
# Modulo: deli_pi.py
# Descripcion: Modulo con toda la logica de negocio para realizar operaciones
#              CRUD a la base de datos SQLite 'fingers'.
# Autor: Alessandro Chavez
#
import datetime
import sqlite3


class Fingers():
    """Clase que maneja todas las operaciones CRUD a alguna base de datos 
    (fingers)."""

    def __init__(self, nombre_bd='fingers.db'):
        """Constructor de clase Fingers

        Almacena nombre de la base de datos a utilizar, asi como la conexion
        a la base de datos.

        Args:
            nombre_bd (str): nombre del archivo de base de datos para el SQLite.

        Attributes:
            nombre_bd (str): nombre del archivo de base de datos para el SQLite.
            conn (obj): conexion a base de datos SQLite3
        """
        self.nombre_bd = nombre_bd
        self.conn = sqlite3.connect(self.nombre_bd)

    def execute_query(self, query):
        """Metodo para ejecutar un query y regresar un diccionario con los
        resultados.

        Args:
            query (str): query a ejecutar

        Returns:
            dict: diccionario con el resultado del query en la llave res
        """
        tmp_res = self.conn.execute(query)
        res = []
        for item in tmp_res:
            res.append(item[0])
        return {'res': res}

    def get_tables(self):
        """Metodo para mostrar todas las tablas almacenadas en la base de datos

        El metodo ejecuta un select a todas las tablas disponibles de la base
        de datos que se utilice para saber que tablas contiene

        Args:
            None

        Returns:
            dict: lista de tablas almacenada en la key de res
        """
        query = "SELECT name FROM sqlite_master WHERE type='table';"
        return self.execute_query(query)

    def get_users(self):
        """Metodo para mostrar todos los usuarios registrados en la base de 
        datos

        El metodo ejecuta un select a todos los registros disponibles de la 
        base de datos que se utilice para saber que usuarios existen

        Args:
            None

        Returns:
            dict: lista de tablas almacenada en la key de res
        """
        query = "SELECT * FROM Usuarios;"
        return self.execute_query(query)

    def get_user(self, id):
        """El método ejecuta un select al usuario con el id otorgado

        Args:
            id (int): identificador del usuario a obtener

        Returns:
            dict: lista de tablas almacenada en la key de res
        """
        query = f"SELECT * FROM Usuarios WHERE id = {id};"
        return self.execute_query(query)

    def add_user(self, nombre='', apellido_paterno='', apellido_materno='',
                 nivel_acceso=0):
        """El método agrega un usuario a la tabla Usuarios

        Args:
            nombre (str):
                Nombre del usuario a registrar
            apellido_paterno (str):
                Apellido paterno del usuario a registrar
            apellido_materno (str):
                Apellido materno del usuario a registrar
            fecha_registro (datetime):
                Contiene la fecha actual en la que se registró el usuario
            nivel_acceso (int):
                Número que indica el nivel de acceso que tiene un usuario

        Returns:
            None
        """
        query = f"""
        INSERT INTO Usuarios(
            nombre, 
            apellido_paterno, 
            apellido_materno,
            nivel_acceso
        ) VALUES (
            {nombre},
            {apellido_paterno}, 
            {apellido_materno},
            {nivel_acceso}
        )
        """
        self.execute_query(query)


if __name__ == '__main__':
    tmp_obj = Fingers()
    print(tmp_obj.get_tables())
    print(tmp_obj.get_users())
