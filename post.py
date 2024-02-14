

class Post():
    def __init__(self, author):
        self.author = author
        self.likes = []
        self.comments = []

    def like(self, liker):
        self.likes.append(liker)
        notification = (liker.username + " liked your post")
        self.author.notifications.append(notification)
        print(f"notification to {self.author.username}:" + notification)
    
    def comment(self, commenter, body: str):
        notification = (commenter.username + " commented your post")
        self.author.notifications.append(notification)
        self.comments.append(body)
        print(f"notofication to {self.author.username}: " + notification + ":" + body)
    
    def print(self):
        pass 



class SalePost(Post):
    def __init__(self, author, body, price, location):
        self.body = body
        self.author = author
        self.location = location
        self.likes = []
        self.comments = []
        self.price = price
        self.is_available = True

    def print(self):
        print("The author is " + self.author.type.username)
        if self.type == "Text" or self.type == "Sale":
            print("The content of the post is:" + self.body)
        print("The post has:"+len(self.likes)+"likes")
        if self.type == "Sale":
            print("The price of the item is:" + str(self.price))

    def discount(self, discount, password):
        if self.type != "Sale":
            raise ValueError("You cant discount an unexciting item")
        else:
            self.price -= discount
            notification = ("Discount on" + self.author.username + "'s product! the new price is" + self.price)
            print(notification)
            self.author.notifications.append(notification)

    def sold(self):
        self.is_available = False



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

    def dispaly(self):
        pass

        



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


