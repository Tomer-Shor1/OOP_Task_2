from user import User


class SocialNetwork:
    __instance = None

    # def __new__(cls, body):
    #     if cls.__instancecheck__ is None:
    #         cls.__instance = super().__new__(cls)
    #     return cls.__instance

    def __init__(self, name):
        self.name = name
        self.users_list = []
        self.posts_list = []
        self.connected_users = 0
        print(f"The social network {self.name} was created!")

    def sign_up(self, username, password: str):
        if username in self.users_list: #initial checks
            raise ValueError("Username is already taken")
        if len(password) > 8 or len(password) < 4:
            raise ValueError("Password must be bew 4 and 8 characters")
        u = User(username, password)
        self.users_list.append(u)
        self.connected_users += 1
        return u
    
    def log_out(self, username):
        for user in self.users_list:
            if user.username == username:
                _user = user
                _user.is_connected = False
                print(f"{_user.username} disconnected")
                return
        raise Exception("user not found")
    
    def log_in(self, username, password):
     for user in self.users_list:
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
       ans = f"{self.name} social network: \n"
       for user in self.users_list: 
          user_info = str(user)
          ans += user_info + "\n"
       return ans 
          


        



    
