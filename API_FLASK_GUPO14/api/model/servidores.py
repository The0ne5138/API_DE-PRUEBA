
from ..database import DatabaseConnection

class Servidor:
    _keys = ["id_Servidor","nombreServidor","descripcion"]
    def __init__(self, id_Servidor = None, nombreServidor = None, descripcion = None):
        self.id_Servidor = id_Servidor
        self.nombreServidor = nombreServidor
        self.descripcion = descripcion

    # Los dos siguientes son los que se usan en la API
    @classmethod
    def get_servidoresPorUsuario(cls, id_usuario):
        query = """SELECT servidores.* FROM DB_TIF_Grupo_14.servidores 
                    INNER JOIN DB_TIF_Grupo_14.usuario_Servidor
                   ON servidores.id_Servidor = usuario_Servidor.id_server 
                   WHERE usuario_Servidor.id_user = %s;"""
        params=(id_usuario,)
        result = DatabaseConnection.fetch_all(query,params=params)  # Retorna una lista de tuplas, donde cada tupla es una fila que cumple el llamado a la BD.
        servers = []
        for row in result:
            server_dict = dict(zip(cls._keys, row))
            servers.append(server_dict)
            #servers.append(cls(**dict(zip(cls._keys, row))))
        return servers
    
    @classmethod
    def create_servidor(self, servidor):
        query = "INSERT INTO DB_TIF_Grupo_14.servidores (nombreServidor, descripcion) VALUES (%s,%s);"
        params = (servidor.nombreServidor, servidor.descripcion)
        DatabaseConnection.execute_query(query, params)



########### Se implementaron como practica #############################
    @classmethod
    def get_servidor(self,id_servidor):
        query = "SELECT nombreServidor, descripcion FROM DB_TIF_Grupo_14.servidores WHERE id_Servidor = %s;"
        params = (id_servidor,)
        result = DatabaseConnection.fetch_one(query, params)
        if result is not None:
            return Servidor(
                            id_Servidor = id_servidor,
                            nombreServidor = result[0],
                            descripcion = result[1]
                            )
        else:
            return None
      
    @classmethod
    def update_servidor(self, servidor):
        query = """
                UPDATE servidores
                SET nombreServidor = %s, descripcion = %s
                WHERE id_servidor = %s
                """
        params = (servidor.nombreServidor, servidor.descripcion, servidor.id_Servidor)
        DatabaseConnection.execute_query(query, params)
        return None


    @classmethod
    def delete_servidor(self,id_servidor):  # Warning: Hay q modificar la BD p/q si se elimina a un servidor que tiene usuarios (y seguramente canales, chats tambien) creados da ERROR
        query = "DELETE FROM servidores WHERE id_servidor = %s"
        params = (id_servidor,)
        DatabaseConnection.execute_query(query, params)
        return {'message': 'Servidor borrado con exito'},204
   
    """
    @classmethod
    def get_servidoresPorUsuario(cls, id_usuario):
        query = ""SELECT servidores.* FROM DB_TIF_Grupo_14.servidores INNER JOIN DB_TIF_Grupo_14.usuario_Servidor
                   ON servidores.id_Servidor = usuario_Servidor.id_server WHERE usuario_Servidor.id_user = %s;""
        params = (id_usuario,)
        result = DatabaseConnection.fetch_all(query, params)
        listaServidores =[]
        if result is not None:
            for server in result:
                listaServidores.append(
                Servidor(
                id_Servidor = server[0],
                nombreServidor = server[1],
                descripcion = server[2]
                ))
                
            return listaServidores
        else:
            return None
"""