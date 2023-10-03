from flask import Blueprint
from ..controllers.usuario_controller import UsuarioController

usuario_bp = Blueprint('usuario_bp',__name__)

usuario_bp.route('/usuarios/<int:id_usuario>', methods = ['GET'])(UsuarioController.get_usuario)         # Solicita los datos de el usuario.
usuario_bp.route('/usuarios', methods = ['POST'])(UsuarioController.create_usuario)                      # Crea un nuevo usuario
usuario_bp.route('/usuarios/<int:id_usuario>', methods = ['PUT'])(UsuarioController.update_usuario)     # Edita(modifica, actualiza) un usuario. SI HAY Q HACERLA
usuario_bp.route('/usuarios/<int:id_usuario>', methods = ['DELETE'])(UsuarioController.delete_usuario)  # Elimina un usuario SERIA EN PERFIL ELIMINAR CUENTA. # Warning: Hay q modificar la BD p/q si se elimina a un usuario que tiene servidores (y seguramente canales, chats tambien) creados da ERROR

usuario_bp.route('/usuarios/perfil', methods = ['GET'])(UsuarioController.show_profile)
usuario_bp.route('/usuarios/homeLog', methods = ['GET'])(UsuarioController.show_profile)


#usuario_bp.route('/usuarios', methods = ['DELETE'])(UsuarioController.delete_usuarios)                  # Elimina usuario todos los usuarios DENGER. NO LA VOY A IMPLEMENTAR.
#usuario_bp.route('/usuarios', methods = ['GET'])(UsuarioController.get_usuarios)                        # Solicia los datos de todos los usuarios. 

