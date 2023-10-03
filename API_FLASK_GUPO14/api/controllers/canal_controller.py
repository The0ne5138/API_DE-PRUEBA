
from ..model.canales import Canal
from flask import request
from flask import jsonify


class CanalController:

    @classmethod
    def get_canalesPorUsuario(cls, id_usuario, id_servidor):
        response_data = Canal.get_canalesPorUsuario(id_usuario, id_servidor)
        #json_data = json.dumps(response_data)
        #return json_data
        return jsonify(response_data), 200
    

    @classmethod
    def create_canal(self):
        canal = Canal(
        nombreCanal = request.args.get('nombreCanal', ''),
        descripcion = request.args.get('descripcion', ''),
        id_user_creo_canal = request.args.get('id_user_creo_canal', ''),
        id_server = request.args.get('id_server', ''),
        )

        Canal.create_canal(canal)
        return {'message': 'Canal creado con exito'}, 200












########### Se implementaron como practica #############################
    @classmethod
    def get_canal(cls, id_canal):
        canal_instance = Canal.get_canal(id_canal)

        if canal_instance:
            response_data = {"id_canal": canal_instance.id_canal,
                             "nombreCanal": canal_instance.nombreCanal,
                             "descripcion": canal_instance.descripcion,
                             "id_user_creo_canal" : canal_instance.id_user_creo_canal,
                             "id_server" : canal_instance.id_server,
                            }
            return jsonify(response_data), 200
        else:
            return {"msg": "No se encontró el Canal"}, 404
    
    @classmethod
    def update_canal(cls, id_canal):
        datos = request.json
        canal = Canal(
                        id_canal,
                        nombreCanal = datos.get('nombreCanal', ''),
                        descripcion = datos.get('descripcion', ''),
                        id_user_creo_canal = datos.get('id_user_creo_canal', ''),
                        id_server = datos.get('id_server', '')
                        )
        
        Canal.update_canal(canal)
        return {'message': 'Canal actualizado con exito'},200


    @classmethod
    def delete_canal(cls, id_canal):   # Warning: Hay q modificar la BD p/q si se elimina a un canal que tiene servidores (y seguramente canales, chats tambien) creados da ERROR
        Canal.delete_canal(id_canal)
        return {'message': 'Canal borrado con exito'},204

