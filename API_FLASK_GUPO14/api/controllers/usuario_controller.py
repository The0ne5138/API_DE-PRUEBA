
from ..model.usuarios import Usuario
from flask import request, session
from flask import jsonify


class UsuarioController:
    @classmethod
    def login(cls):
        data = request.json
        user = Usuario(nombre_usuario = data.get('nombre_usuario'),clave = data.get('clave'))
        
        if Usuario.is_registered(user):
            session['nombre_usuario'] = data.get('nombre_usuario')
            tupla = user.retorna_id_usuario(session.get('nombre_usuario'))
            session['id_usuario'] = int(tupla[0])
            #print(session['nombre_usuario'])
            #print(session['id_usuario'])
            return {"message": "Sesion iniciada"}, 200
        else:
            return {"message": "Usuario o contraseña incorrectos"}, 401
    
    @classmethod
    def show_profile(cls):
        username = session.get('nombre_usuario')
        #user = Usuario.get_usuario_username(Usuario(nombre_usuario = username))
        user = Usuario.get_usuario_username(Usuario(nombre_usuario = username))
        
        if user is None:
            return {"message": "Usuario no encontrado"}, 404
        else:
            return user.serialize(), 200
    
    @classmethod
    def logout(cls):
        session.pop('nombre_usuario', None)
        return {"message": "Sesion cerrada"}, 200
    

    @classmethod
    def create_usuario(self):
        
        usuario = Usuario(
        nombre_usuario = request.args.get('nombre_usuario', ''),
        clave = request.args.get('clave', ''),
        email = request.args.get('email', ''),
        nombre = request.args.get('nombre', ''),
        apellido = request.args.get('apellido', ''),
        imagen_perfil = request.args.get('imagen_perfil', '')
        )

        Usuario.create_usuario(usuario)
        return {'message': 'Usuario creado con exito'}, 200
    
    @classmethod
    def get_usuario(cls, id_usuario):
        usuario_instance = Usuario.get_usuario(id_usuario)

        if usuario_instance:
            response_data = {"id": usuario_instance.id_usuario,
                             "nombre_usuario": usuario_instance.nombre_usuario,
                             "clave": usuario_instance.clave,
                             "email" : usuario_instance.email,
                             "nombre" : usuario_instance.nombre,
                             "apellido" : usuario_instance.apellido,
                             "imagen_perfil" : usuario_instance.imagen_perfil
                            }
            return jsonify(response_data), 200
        else:
            return {"msg": "No se encontró el usuario"}, 404
    
    @classmethod
    def update_usuario(cls, id_usuario):
        datos = request.json
        usuario = Usuario(
                        id_usuario,
                        nombre_usuario = datos.get('nombre_usuario', ''),
                        clave = datos.get('clave', ''),
                        email = datos.get('email', ''),
                        nombre = datos.get('nombre', ''),
                        apellido = datos.get('apellido', ''),        
                        imagen_perfil = datos.get('imagen_perfil', '')
                        )
        
        Usuario.update_usuario(usuario)
        return {'message': 'Usuario actualizado con exito'},200


    @classmethod
    def delete_usuario(cls, id_usuario):   # Warning: Hay q modificar la BD p/q si se elimina a un usuario que tiene servidores (y seguramente canales, chats tambien) creados da ERROR
        Usuario.delete_usuario(id_usuario)
        return {'message': 'Usuario borrado con exito'},204




    








    
    # @classmethod
    # def get_actors(self):
    #     results = Actor.get_actors
    #     actors = []
    #     for result in results:
    #         actors.append({
    #             "id": result[0],
    #             "nombre": result[1],
    #             "apellido": result[2],
    #             "ultima_actualizacion": result[3]
    #     })
    #     return actors, 200
        

    # @classmethod
    # def update_actor(self, actor):
    # #Implementación del método
    #     pass

    # @classmethod
    # def delete_actor(self, actor):
    # #Implementación del método
    #     pass

    # @classmethod
    # def delete_actors(self):
    # #Implementación del método
    #     pass