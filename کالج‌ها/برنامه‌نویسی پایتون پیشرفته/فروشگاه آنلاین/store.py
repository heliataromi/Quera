from models import Product, User


class Store:
    def __init__(self):
        self.products = dict()
        self.users = list()

    def add_product(self, product, amount=1):
        self.products[product] = self.products.get(product, 0) + amount

    def remove_product(self, product, amount=1):
        if product not in self.products or self.products[product] < amount:
            raise Exception('Not Enough Products')
        self.products[product] -= amount
        if self.products[product] == 0:
            self.products.pop(product)

    def add_user(self, username):
        new_user = User(username)
        for user in self.users:
            if user == new_user:
                return None
        self.users.append(new_user)
        return username

    def get_total_asset(self):
        total_asset = 0
        for product in self.products:
            total_asset += self.products[product] * product.price
        return total_asset

    def get_total_profit(self):
        total_profit = 0
        for user in self.users:
            for product in user.bought_products:
                total_profit += product.price
        return total_profit

    def get_comments_by_user(self, user):
        comments = []
        for product in self.products:
            for comment in product.comments:
                if comment.user == user:
                    comments.append(comment.text)
        return comments

    def get_inflation_affected_product_names(self):
        product_names = []
        for product in self.products:
            for other_product in self.products:
                if product.name == other_product.name and product.price != other_product.price:
                    product_names.append(product.name)
        return list(set(product_names))

    def clean_old_comments(self, date):
        for product in self.products:
            for comment in product.comments:
                if comment.date_added <= date:
                    product.comments.remove(comment)

    def get_comments_by_bought_users(self, product):
        comments = []
        for comment in product.comments:
            if product in comment.user.bought_products:
                comments.append(comment.text)
        return comments
