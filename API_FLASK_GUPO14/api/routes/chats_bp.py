from flask import Blueprint
from ..controllers.chat_controller import ChatController

chat_bp = Blueprint('chat_bp',__name__)

chat_bp.route('/chat/<int:id_mensaje>', methods = ['GET'])(ChatController.get_chat)        # Solicita los datos de el chat.
chat_bp.route('/chat', methods = ['POST'])(ChatController.create_chat)                  # Crea un nuevo chat
chat_bp.route('/chat/<int:id_mensaje>', methods = ['PUT'])(ChatController.update_chat)     # Edita(modifica, actualiza) un chat. SI HAY Q HACERLA
chat_bp.route('/chat/<int:id_mensaje>', methods = ['DELETE'])(ChatController.delete_chat)  # Elimina un chat SERIA EN PERFIL ELIMINAR CUENTA. # Warning: Hay q modificar la BD p/q si se elimina a un chat que tiene servidores (y seguramente chats, chats tambien) creados da ERROR
chat_bp.route('/chats/<int:id_canal>', methods = ['GET'])(ChatController.get_chats)        # Solicita los datos de TODOS LOS chats asociados a un canal.