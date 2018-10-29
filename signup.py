user_db = [] #list to hold users

class User():
    """
    Class to create the user object

    :params email, name, password, role:

    """
    def __init__(self,email,name,password,role):
        self.email = email
        self.name = name
        self.password = password
        self.role = role
        self.logged_in = False

    def signup(self):
        """
        Method to signup a user
        """
        user_data = {
                        'user_email':self.email,
                        'user_name':self.name,
                        'user_password':self.password,
                        'user_role':self.role,
                        'logged_in':self.logged_in
                    }

        user_db.append(user_data)

