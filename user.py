class User:
    users = {}
    user_id = 1
    def __init__(self, name, email, phone, location):
        self.user_id = User.user_id
        User.user_id += 1
        self.name = name
        self.email = email
        self.phone = phone
        self.location = location

