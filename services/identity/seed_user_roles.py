from data.context import Context
from entities.identity.user_entity import UserModel
from entities.identity.roles_entity import RoleModel
from decouple import config
from werkzeug.security import generate_password_hash


class SeedUserRolesInitial:
    def __init__(self) -> None:
        self.conn = Context()

    def seed_roles(self):
        admin = 'ADMIN'
        if not self.conn.session.query(RoleModel).filter(RoleModel.role == admin).first():
            role_admin = RoleModel(admin)
            try:
                self.conn.session.add(role_admin)
                self.conn.save()
            except:
                pass
        
        user = 'USER'
        if not self.conn.session.query(RoleModel).filter(RoleModel.role == user).first():
            role_user = RoleModel(user)
            try:
                self.conn.session.add(role_user)
                self.conn.save()
            except:
                pass

    def seed_users(self):
        admin = 'admin@api'
        admin_pass = config('PASS_ADMIN')
        if not self.conn.session.query(UserModel).filter(UserModel.username == admin).first():
            role_admin = self.conn.session.query(RoleModel).filter(RoleModel.role == 'ADMIN').first()
            user_admin = UserModel(admin, generate_password_hash(admin_pass), 'ADMINISTRADOR', 'administrador@pythonflask.com', role_admin, ativo=True)
            try:
                self.conn.session.add(user_admin)
                self.conn.save()
            except:
                pass

        user = 'user@api'
        user_pass = config('PASS_USER')
        if not self.conn.session.query(UserModel).filter(UserModel.username == user).first():
            role_user = self.conn.session.query(RoleModel).filter(RoleModel.role == 'USER').first()
            user_user = UserModel(user, generate_password_hash(user_pass), 'USUARIO','usuario@pythonflask.com', role_user, lastname='TESTE', ativo=True)
            try:
                self.conn.session.add(user_user)
                self.conn.save()
            except:
                pass