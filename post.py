

class Post():
    def __init__(self, author):
        self.author = author
        self.likes = []
        self.comments = []

    def like(self, liker):
        self.likes.append(liker)
        notification = (liker.username + " liked your post")
        self.author.notifications.append(notification)
        print(f"notification to {self.author.username}: " + notification)
    
    def comment(self, commenter, body: str):
        notification = (commenter.username + " commented your post")
        self.author.notifications.append(notification)
        self.comments.append(body)
        print(f"notofication to {self.author.username}: " + notification + ": " + body)
    
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
        print(f"{self.author.username} posted a product for sale! \nFor sale! {self.body}, price: {self.price}, pickup from: {self.location}")


    def __str__(self):
        if self.is_available == True:
          return f"{self.author.username} posted a product for sale! \nFor sale! {self.body}, price: {self.price}, pickup from {self.location}"
        return f"{self.author.username} posted a product for sale! \nSold! {self.body}, price: {self.price}, pickup from {self.location}" 


    def discount(self, discount, password):
            self.price -= discount
            notification = (f"Discount on {self.author.username}'s product! the new price is {self.price}")
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

    def print(self):
        print(self.body)




class ImagePost(Post):
    def __init__(self, author, image_url):
        self.author = author
        self.image_url = image_url
        self.likes = []
        self.comments = []

    def display(self):
        pass

        


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


