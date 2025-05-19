import os

# 假資料庫（帳號: test, 密碼: secret）
users = {
    "admin": {
        "username": "admin",
        "password": "admin"
    }
}

class Auths:
    def __init__(self):
        self.key = os.environ.get("AUTH_KEY")
        self.users = users

    def get_key(self):
        return self.key
    
    def get_users(self, username):
        return self.users

    def verify_password(self, username, password):
        isValid = True
        user_data = self.users.get(username)
        if(not user_data or user_data["password"] != password):
            isValid = False

        return isValid
    
auths = Auths()