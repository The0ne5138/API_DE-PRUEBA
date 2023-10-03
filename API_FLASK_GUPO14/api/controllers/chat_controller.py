
from ..model.chats import Chat
from flask import request
from flask import jsonify
import datetime


class ChatController:
    @classmethod
    def create_chat(self):
        fecha_creacion = datetime.datetime.now()
        chat = Chat(
        contenido = request.args.get('contenido', ''),
        fecha_creacion = fecha_creacion, #request.args.get('fecha_creacion', ''),
        id_user = request.args.get('id_user', ''),
        id_canal = request.args.get('id_canal', ''),
        )

        Chat.create_chat(chat)
        return {'message': 'Chat creado con exito'}, 200
    
    @classmethod
    def get_chat(cls, id_mensaje):
        chat_instance = Chat.get_chat(id_mensaje)

        if chat_instance:
            response_data = {"id_mensaje": chat_instance.id_mensaje,
                             "contenido": chat_instance.contenido,
                             "fecha_creacion": chat_instance.fecha_creacion,
                             #"id_user" : chat_instance.id_user,
                             #"id_canal" : chat_instance.id_canal
                            }
            return jsonify(response_data), 200
        else:
            return {"msg": "No se encontró el Chat"}, 404
    
    @classmethod
    def update_chat(cls, id_mensaje):
        fecha_modificacion = datetime.datetime.now()
        datos = request.json
        chat = Chat(
                        id_mensaje,
                        contenido = datos.get('contenido', ''),
                        fecha_creacion = fecha_modificacion,#datos.get('fecha_creacion', ''),
                        id_user = datos.get('id_user', ''),
                        id_canal = datos.get('id_canal', '')
                        )
        
        Chat.update_chat(chat)
        return {'message': 'chat actualizado con exito'},200


    @classmethod
    def delete_chat(cls, id_mensaje):   # Warning: Hay q modificar la BD p/q si se elimina a un chat que tiene servidores (y seguramente chats, chats tambien) creados da ERROR
        Chat.delete_chat(id_mensaje)
        return {'message': 'Chat borrado con exito'},204
#####################################################
    """@classmethod
    def get_chats(cls,id_canal=None):
        chats = []
        if id_canal:
            chats = Chat.get_chats(id_canal)
        #if request.args.get('id_canal'):
        #    #chat_obj = Chat(id_canal=request.args.get('id_canal'))
        #    chats = Chat.get_chats(id_canal = request.args.get('id_canal'))#chats = Chat.get_chat(chat_obj)
        else:
            chats = Chat.get_chat()
        return [chat_item.to_dict() for chat_item in chats], 200
    """

    @classmethod
    def get_chats(cls, id_canal):
        chats = []
        if id_canal:
            chats = Chat.get_chats(id_canal)
        #if request.args.get('id_canal'):
        #    #chat_obj = Chat(id_canal=request.args.get('id_canal'))
        #    chats = Chat.get_chats(id_canal = request.args.get('id_canal'))#chats = Chat.get_chat(chat_obj)
        else:
            chats = Chat.get_chats()
        return chats#[chat_item.to_dict() for chat_item in chats], 200
