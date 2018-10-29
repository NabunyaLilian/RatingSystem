user_db = []

class User():
    def __init__(self,email,name,password,role):
        self.email = email
        self.name = name
        self.password = password
        self.role = role
        self.logged_in = False

    def signup(self):
        user_data = {
                        'user_email':self.email,
                        'user_name':self.name,
                        'user_password':self.password,
                        'user_role':self.role,
                        'logged_in':self.logged_in
                    }

        user_db.append(user_data)
me = User(print(user_db)
'sanya','ken',123,'LF')
me.signup()
