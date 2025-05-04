class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

    def save(self):
        pass

    @classmethod
    def get_user_by_username(cls, username):
        pass