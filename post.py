import matplotlib.pyplot as plt


#parent post class
class Post():
    def __init__(self, author):
        self.author = author
        self.likes = []
        self.comments = []

    def like(self, liker):
        if liker is self.author:   #if a user likes his post
            self.likes.append(liker)
            return
        self.likes.append(liker)
        notification = (liker.username + " liked your post")
        self.author.notifications.append(notification)
        print(f"notification to {self.author.username}: " + notification)
    
    def comment(self, commenter, body: str):
        notification = (commenter.username + " commented on your post")
        self.author.notifications.append(notification)
        self.comments.append(body)
        print(f"notification to {self.author.username}: " + notification + ": " + body)
    
    def print(self):
        pass 



class SalePost(Post):
    def __init__(self, author, body, price, location):
        self.body = body
        self.author = author
        self.price = price
        self.location = location
        self.likes = []
        self.comments = []
        self.is_available = True
        print(f"{self.author.username} posted a product for sale:\nFor sale! {self.body}, price: {self.price}, pickup from: {self.location}\n")


    def __str__(self):
        if self.is_available == True:
          return f"{self.author.username} posted a product for sale:\nFor sale! {self.body}, price: {self.price}, pickup from: {self.location}\n"
        return f"{self.author.username} posted a product for sale:\nSold! {self.body}, price: {self.price}, pickup from: {self.location}\n" 


    def discount(self, discount, password):
            if self.author.password != password:
                raise Exception("Wrong password")
            if self.is_available is False:
                raise Exception("item is not available")
            self.price *= (100-discount)/100
            notification = (f"Discount on {self.author.username} product! the new price is: {self.price}")
            print(notification)
            self.author.notifications.append(notification)

    def sold(self, password):
        if self.author.password != password:
            raise Exception("Wrong password")
        self.is_available = False
        print(f"{self.author.username}'s product is sold")



class TextPost(Post):
    def __init__(self, author, body):
        self.body = body
        self.author = author
        self.likes = []
        self.comments = []
        print(f"{self.author.username} published a post:\n\"{self.body}\"\n")

    def __str__(self):
        return f"{self.author.username} published a post:\n\"{self.body}\"\n"




class ImagePost(Post):
    def __init__(self, author, image_url):
        self.author = author
        self.image_url = image_url
        self.likes = []
        self.comments = []
        print(f"{self.author.username} posted a picture\n")

    def display(self):
        print("Shows picture")
        img = plt.imread(self.image_url)
        plt.axis('off')
        plt.imshow(img)
        plt.show(block=False)
        
        display_time = 1  # Display time in seconds
        plt.pause(display_time)
        plt.close()


    def __str__(self):
        return f"{self.author.username} posted a picture\n"
        

        

# post factory class
class PostFactory:
    def createPost(author, post_type, *info):
        if post_type == "Text":
            return TextPost(author, *info)
        if post_type == "Image":
            return ImagePost(author, *info)
        if post_type == "Sale":
            return SalePost(author, *info)
        else:
            raise Exception("Invalid post type")


