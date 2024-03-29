from user import User


class SocialNetwork:

    #singleton implementation
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.__initialized = False
        return cls._instance

    def __init__(self, name):
        if not self.__initialized:
            self.name = name
            self.users_list = []
            self.posts_list = []
            self.connected_users = 0
            print(f"The social network {self.name} was created!")
            self.__initialized = True

    def sign_up(self, username, password: str):
        if username in self.users_list: #initial checks
            raise ValueError("Username is already taken")
        if len(password) > 8 or len(password) < 4:
            raise ValueError("Password must be between 4 and 8 characters")
        u = User(username, password)
        self.users_list.append(u)
        self.connected_users += 1
        return u
    
    def log_out(self, username):
        for user in self.users_list:  #check if the user exists
            if user.username == username:
                _user = user
                _user.is_connected = False
                print(f"{_user.username} disconnected")
                return
        raise Exception("user not found")
    
    def log_in(self, username, password):
     for user in self.users_list:    #check if the user exists
         if user.username == username:
             _user = user
             if _user.username == username and _user.password == password:
               print(f"{_user.username} connected")
               self.is_connected = True
               return
             else:
               print("Wrong username or password")
               return
     raise Exception("user not found")
    

    def __str__(self):
       ans = f"{self.name} social network:\n"
       for user in self.users_list: 
          user_info = str(user)
          ans += user_info + "\n"
       return ans 
          


        



    
