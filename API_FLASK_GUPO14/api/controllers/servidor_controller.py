
from ..model.servidores import Servidor
from flask import request
from flask import jsonify
import json


class ServidorController:
    
    # Los dos siguientes son los que se usan en la API
    @classmethod
    def get_servidoresPorUsuario(cls, id_usuario):
        response_data = Servidor.get_servidoresPorUsuario(id_usuario)
        #json_data = json.dumps(response_data)
        #return json_data
        return jsonify(response_data), 200
    
    @classmethod
    def create_servidor(self):
        """ Crea un nuevo Servidor. """
        servidor = Servidor(
            nombreServidor = request.args.get('nombreServidor', ''), 
            descripcion = request.args.get('descripcion', '')
            )

        Servidor.create_servidor(servidor)
        return {'message': 'Servidor creado con exito'}, 200








########### Se implementaron como practica #############################
    @classmethod
    def get_servidor(cls, id_Servidor):
        """ Para cada servidor debe mostrar: Nombre del Servidor,
            Descripcion y Cantidad de usuarios en el servidor.
        """
        servidor_instance = Servidor.get_servidor(id_Servidor)

        if servidor_instance:
            response_data = {"id_Servidor": servidor_instance.id_Servidor,
                             "nombreServidor": servidor_instance.nombreServidor,
                             "descripcion": servidor_instance.descripcion,
                            }
            return jsonify(response_data), 200
        else:
            return {"msg": "No se encontró el servidor"}, 404

    @classmethod
    def update_servidor(cls, id_Servidor):
        datos = request.json
        servidor = Servidor(
                        id_Servidor,
                        nombreServidor = datos.get('nombreServidor', ''),
                        descripcion = datos.get('descripcion', ''),
                        )
        
        servidor.update_servidor(servidor)
        return {'message': 'servidor actualizado con exito'},200


    @classmethod
    def delete_servidor(cls, id_Servidor):   # Warning: Hay q modificar la BD p/q si se elimina a un servidor que tiene servidores (y seguramente canales, chats tambien) creados da ERROR
        Servidor.delete_servidor(id_Servidor)
        return {'message': 'Servidor borrado con exito'},204
    



"""
    @classmethod   ### ESTE LO ESTOY DESARROLLANDO Cual va a ser el parametro que se envia desde la VISTA PARA BUSCAR?.
    def get_servidores(cls, id_servidor):
        "" Muestra una lista Con todos los servidores resultantes de la busqueda.""
        servidores_instance = Servidor.get_servidor(id_servidor)

        if servidores_instance:
            for servidor in servidores_instance:
                servidor_instance = Servidor.get_servidor(id_servidor)
                servidor_data = {"id_servidor": servidor_instance.id_servidor,
                                "nombreServidor": servidor_instance.nombreServidor,
                                "descripcion": servidor_instance.descripcion,
                            }
            return jsonify(response_data), 200
        else:
            return {"msg": "No se encontró el servidor"}, 404
"""