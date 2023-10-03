
from ..database import DatabaseConnection

class Usuario:
    _keys = ["id_usuario","nombre_usuario","clave","email","nombre","apellido","imagen_perfil"]
    def __init__(self, **kwargs):
        self.id_usuario = kwargs.get('id_usuario')
        self.nombre_usuario = kwargs.get('nombre_usuario')
        self.clave = kwargs.get('clave')
        self.email = kwargs.get('email')
        self.nombre = kwargs.get('nombre')
        self.apellido = kwargs.get('apellido')
        self.imagen_perfil = kwargs.get('imagen_perfil')

    def serialize(self):
        return {
            "id_usuario": self.id_usuario,
            "nombre_usuario": self.nombre_usuario,
            "clave": self.clave,
            "email": self.email,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "imagen_perfil": self.imagen_perfil
        }
    
    @classmethod
    def is_registered(cls, user):
        query = """SELECT id_usuario FROM db_tif_grupo_14.usuarios 
        WHERE nombre_usuario = %(nombre_usuario)s and clave = %(clave)s"""
        params = user.__dict__
        #print(params)
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return True
        return False
    
    @classmethod
    def get_usuario_id(self,id_usuario):
        """Retorna una instancia de Usuario con todos los atributos solo enviando 'id_usuario'."""
        query = "SELECT nombre_usuario, clave, email, nombre, apellido, imagen_perfil FROM TIF_Grupo_14.usuarios WHERE id_usuario = %s;"
        params = (id_usuario,)
        result = DatabaseConnection.fetch_one(query, params)
        if result is not None:
            return Usuario(
                            id_usuario = id_usuario,
                            nombre_usuario = result[0],
                            clave = result[1],
                            email = result[2],
                            nombre = result[3],
                            apellido = result[4],        
                            imagen_perfil = result[5]
                            )
        else:
            return None
        
    @classmethod
    def get_usuario_username(cls, user):
        """Retorna una instancia de Usuario con todos los atributos solo enviando 'nombre_usuario'."""
        
        query = """SELECT * FROM db_tif_grupo_14.usuarios 
        WHERE nombre_usuario = %(nombre_usuario)s"""
        params = user.__dict__
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return cls(
                id_usuario = result[0],
                nombre_usuario = result[1],
                clave = result[2],
                email = result[3],
                nombre = result[4],
                apellido = result[5],
                imagen_perfil = result[6]
                )
        return None

    @classmethod
    def retorna_id_usuario(self, nombre_usuario):
        query = "SELECT id_usuario FROM DB_TIF_Grupo_14.usuarios WHERE nombre_usuario = %(nombre_usuario)s"
        params = {"nombre_usuario":nombre_usuario}
        return DatabaseConnection.fetch_one(query,params)
    
    @classmethod
    def create_usuario(self, usuario):
        query = "INSERT INTO TIF_grupo_14.usuarios (nombre_usuario, clave, email, nombre, apellido, imagen_perfil) VALUES (%s,%s,%s,%s,%s,%s);"
        params = (usuario.nombre_usuario, usuario.clave, usuario.email, usuario.nombre, usuario.apellido, usuario.imagen_perfil)
        DatabaseConnection.execute_query(query, params)



"""
############### GET SIMULTANEO #######################
    @classmethod
    def get1(cls, user = None):
        if user is not None and user.id_usuario is not None:
#            query = """#SELECT id_usuario, nombre_usuario, clave, email, nombre, apellido, imagen_perfil
                        #FROM DB_TIF_Grupo_14.usuarios WHERE id_usuario = %(id_usuario)s
"""
            params = user.__dict__
            result = DatabaseConnection.fetch_one(query,params)
            if result:
                return cls(**dict(zip(cls._keys, result)))
            else:
                return None
        else:
            query = "SELECT id_usuario, nombre_usuario, clave, email, nombre, apellido, imagen_perfil FROM DB_TIF_Grupo_14.usuarios"
            result = DatabaseConnection.fetch_all(query)
            users =[]
            for row in result:
                users.append(cls(**dict(zip(cls._keys, row))))
            return users
        
# EXTRA Delete
    @classmethod
    def delete (cls, user):
        query = "DELETE FROM DB_TIF_Grupo_14.usuarios WHERE id_usuario = %(id_usuario)s"
        params = user.__dict__
        DatabaseConnection.execute_query(query, params)
        return {'message': 'Usuario borrado con exito'},204




    @classmethod
    def delete_usuario(self,id_usuario):  # Warning: Hay q modificar la BD p/q si se elimina a un usuario que tiene servidores (y seguramente canales, chats tambien) creados da ERROR
        query = "DELETE FROM usuarios WHERE id_usuario = %s"
        params = (id_usuario,)
        DatabaseConnection.execute_query(query, params)
        return {'message': 'Usuario borrado con exito'},204
    
    @classmethod
    def update_usuario(self, usuario):
        query = """
#                UPDATE usuarios
#                SET nombre_usuario = %s, clave = %s, email = %s, nombre = %s, apellido = %s, imagen_perfil = %s
#                WHERE id_usuario = %s
#                """
#        params = (usuario.nombre_usuario, usuario.clave, usuario.email, usuario.nombre, usuario.apellido, usuario.imagen_perfil, usuario.id_usuario)
#        DatabaseConnection.execute_query(query, params)
#        return None
