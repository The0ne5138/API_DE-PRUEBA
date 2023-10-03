
from ..database import DatabaseConnection

class Chat:
    _keys = ['id_mensaje', 'contenido', 'fecha_creacion', 'id_user','id_canal']
    def __init__(self, id_mensaje = None, contenido = None, fecha_creacion = None, id_user = None, id_canal= None):
        self.id_mensaje = id_mensaje
        self.contenido = contenido
        self.fecha_creacion = fecha_creacion
        self.id_user = id_user
        self.id_canal= id_canal

    def to_dict(self):
        return self.__dict__
    
    @classmethod
    def create_chat(self, chat):
        query = "INSERT INTO DB_TIF_grupo_14.chats (contenido, fecha_creacion, id_user, id_canal) VALUES (%s,%s,%s,%s);"
        params = (chat.contenido, chat.fecha_creacion, chat.id_user, chat.id_canal)
        DatabaseConnection.execute_query(query, params)

    @classmethod
    def get_chat(self,id_mensaje):
        query = "SELECT contenido, fecha_creacion, id_user, id_canal FROM DB_TIF_Grupo_14.chats WHERE id_mensaje = %s;"
        params = (id_mensaje,)
        result = DatabaseConnection.fetch_one(query, params)
        
        if result is not None:
            return Chat(
                            id_mensaje = id_mensaje,
                            contenido = result[0],
                            fecha_creacion = result[1],
                            id_user = result[2],
                            id_canal= result[3]
                        )
        else:
            return None

    @classmethod
    def update_chat(self, chat):
        query = """
                UPDATE chats
                SET contenido = %s, fecha_creacion = %s, id_user = %s, id_canal = %s
                WHERE id_mensaje = %s
                """
        
        params = (chat.contenido, chat.fecha_creacion, chat.id_user, chat.id_canal, chat.id_mensaje)
        DatabaseConnection.execute_query(query, params)
        return None


    @classmethod
    def delete_chat(self,id_mensaje):  # Warning: Hay q modificar la BD p/q si se elimina a un chat que tiene servidores (y seguramente chates, chats tambien) creados da ERROR
        query = "DELETE FROM chats WHERE id_mensaje = %s"
        params = (id_mensaje,)
        DatabaseConnection.execute_query(query, params)
        return {'message': 'Chat borrado con exito'},204

############################################    
    @classmethod
    def get_chats(cls, id_canal = None):

        
        query = "SELECT contenido, fecha_creacion, id_user, id_canal FROM DB_TIF_Grupo_14.chats WHERE id_canal = %s;"
        params = (id_canal,)
        results = DatabaseConnection.fetch_all(query, params)
        chats = [cls(**dict(zip(cls._keys, row))) for row in results]
        return chats