from flask import Blueprint

from ..controllers.usuario_controller import UsuarioController

auth_bp = Blueprint('auth_bp', __name__)

auth_bp.route('/login', methods=['POST'])(UsuarioController.login)
auth_bp.route('/profile', methods=['GET'])(UsuarioController.show_profile)
auth_bp.route('/logout', methods=['GET'])(UsuarioController.logout)