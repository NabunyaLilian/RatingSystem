"""login.py"""
import datetime
from signup import User
class Login(User):
  """class shows methods for a user"""
  def __init__(self, email, password, name, role)
    super.__init__(email, password, name, role)

  def login_user(self, email, password):
    """method to login a user"""
    self.email = input('Enter email')
    self.password = input('Enter password')
    if self.email not in user_db and password not in user_db:
      print ("Email " + self.email + " and "+ self.password+" doesnot exist. Please create register email")

    if self.email in user_db:
      self.logged_in = True
      TIMESTAMP = datetime.datetime.now()
      print("User logged in successfully")
      return "User logged in successfully"

  def logout_user(self):
    """logs out the user"""
    if self.logged_in == True:
      self.logged_in == False
      print("User logged out successfully")
      return "User logged out successfully"
