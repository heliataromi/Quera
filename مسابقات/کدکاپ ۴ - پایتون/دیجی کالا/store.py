from models import Product, User


class Store:
    def __init__(self):
        self.products = dict()
        self.users = list()

    def add_product(self, product: Product, amount=1):
        self.products[product] = self.products.get(product, 0) + amount

    def remove_product(self, product, amount=1):
        if amount > self.products.get(product, 0):
            raise Exception('Not Enough Products')

        self.products[product] -= amount

        if self.products[product] == 0:
            del self.products[product]

    def add_user(self, username):
        for user in self.users:
            if username == user.username:
                return None

        self.users.append(User(username))

        return username

    def get_total_asset(self):
        total_asset = 0

        for product, amount in self.products.items():
            total_asset += product.price * amount

        return total_asset

    def get_total_profit(self):
        total_profit = 0

        for user in self.users:
            for product in user.bought_products:
                total_profit += product.price

        return total_profit

    def get_comments_by_user(self, user):
        comments_by_user = []

        for product, _ in self.products.items():
            for comment in product.comments:
                if comment.user == user:
                    comments_by_user.append(comment.text)

        return comments_by_user

    def get_inflation_affected_product_names(self):
        inflation_affected_product_names = set()

        for product, _ in self.products.items():
            for other_product, __ in self.products.items():
                if product.name == other_product.name and product.price != other_product.price:
                    inflation_affected_product_names.add(product.name)

        return list(inflation_affected_product_names)

    def clean_old_comments(self, date):
        for product, _ in self.products.items():
            product.comments = [comment for comment in product.comments if comment.date_added >= date]

    def get_comments_by_bought_users(self, product):
        comments_by_bought_users = []

        for comment in product.comments:
            if product in comment.user.bought_products:
                comments_by_bought_users.append(comment.text)

        return comments_by_bought_users
