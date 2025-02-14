import bcrypt

from ports.password_hash import PasswordHashInterface


class HashBcrypt(PasswordHashInterface):

    def hash_password(self, password: str) -> str:
        salt = bcrypt.gensalt()
        hash_password = bcrypt.hashpw(password.encode("utf-8"), salt)
        return hash_password

    def compare_password(self, password: str, hash_password: str) -> bool:
        return bcrypt.checkpw(password.encode("utf-8"), hash_password.encode("utf-8"))
