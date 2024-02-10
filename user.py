from SocialNetwork import SocialNetwork
from post import Post


class User:
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
     password =input("enter your password")
     if self.username == username and self.password == password:
         print("Login")
         self.is_connected = True
     else:
         print("Wrong username or password")

    def disconnect_user(self):
        self.is_connected = False
        SocialNetwork.connected_users = SocialNetwork.connected_users-1

    # follow user function
    def follow(self, other_user):
        if other_user in self.following:
            raise Exception("You already follow this user")
        else:
            self.following.append(other_user)
            other_user.followers.append(self)
            print(self.username + "started following" + other_user.username)

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

    def unlike(self, post):
        post.unlike(post, self)

    def comment(self, post, body: str):
        post.comment(self, body)
        self.users_comments.append(body)

    def publish_post(self, title, description, img_url,  price, location, is_available):
        notification = (self.username + "has uploaded a new post")
        for follower in self.followers:
            self.send_notification(follower, notification)
        return Post(self, title, description, img_url, price, location, is_available)

    def print(self):
        print("User's name is: " + self.username)
        print(self.username + "has" + self.followers + "followers")

    def print_notifications(self):
        for notification in self.notifications:
            print(notification)

    def send_notification(self, other, content):
        if other in self.followers:
            other.notifications.append(content)









