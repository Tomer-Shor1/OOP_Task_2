from user import User


class Post:
    def __init__(self, author, post_type: str, body: str = None, image_url=None, price: int = None, location: str = None, is_available: bool = None):
        if post_type != "Text" or post_type != "Image" or post_type != "Sale":
            raise ValueError("invalid post type")
        self.type = post_type
        self.body = body
        self.image_url = image_url
        self.author = author
        self.location = location
        self.likes = []
        self.comments = []
        self.price = price
        self.is_available = is_available

    def like(self, liker: User):
        self.likes.append(liker)
        notification = (liker.username + " has liked your post")
        print(notification)
        self.author.notifications.append(notification)

    def unlike(self, liker: User):
        self.likes.remove(liker)
        notification = (liker.username + "unliked your post")
        print(notification)
        self.author.notifications.append(notification)

    def comment(self, commenter: User, body: str):
        notification = (commenter.username + " has commented your post")
        print(notification)
        self.author.notifications.append(notification)
        self.comments.append(body)

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





