from abc import ABC, abstractmethod
from post import *
from post import PostFactory

class sender(ABC):

    @abstractmethod
    def notify(self, notification):
        pass


#reciever abstract class
class reciever(ABC):

    @abstractmethod
    def update(self, notify):
        pass         



class User(sender, reciever):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.is_connected = True
        self.followers = []
        self.following = []
        self.posts = []
        self.users_comments = []
        self.likes = []
        self.notifications = []

    def login_user(self):
     username = input("Enter your username")
     password = input("enter your password")
     if self.username == username and self.password == password:
         print("Login")
         self.is_connected = True
     else:
         print("Wrong username or password")

    def update(self, notification):
        self.notifications.append(notification)

    def notify(self, notification):
        for follower in self.followers:
            follower.update(notification)

    def disconnect_user(self):
        self.is_connected = False
        #SocialNetwork.connected_users = SocialNetwork.connected_users-1

    # follow user function
    def follow(self, other_user):
        if other_user in self.following:
            raise Exception("You already follow this user")
        if other_user is None:
            raise Exception ("you cant follow none existing user")
        else:
            self.following.append(other_user)
            other_user.followers.append(self)
            print(self.username + " started following " + other_user.username)

    # unfollow user
    def unfollow(self, other_user):
        if other_user not in self.following:
            raise Exception("you do not follow this user")
        else:
            self.following.remove(other_user)
            other_user.followers.remove(self)
            print(self.username + "unfollowed" + other_user.username)

    def like(self, post):
        post.like(post, self)

    def comment(self, post, body: str):
        post.comment(self, body)
        self.users_comments.append(body)

    def publish_post(self, type, *info):
        notification = (self.username + "has uploaded a new post")
        self.notify(notification)
        post = PostFactory.createPost(self.username, type, *info)
        return post

    def print(self):
        print("User's name is: " + self.username)
        print(self.username + "has" + self.followers + "followers")

    def print_notifications(self):
        for notification in self.notifications:
            print(notification)

    
        

    


    






    






