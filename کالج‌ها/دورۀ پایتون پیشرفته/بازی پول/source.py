from re import fullmatch, search
import hashlib

class Site:
    def __init__(self, url_address):
        self.url = url_address
        self.register_users = []
        self.active_users = []

    def show_users(self):
        pass

    def register(self, user):
        if user in self.register_users:
            raise Exception('user already registered')

        self.register_users.append(user)
        return 'register successful'

    def login(self, **kwargs):
        for user in self.register_users:
            if 'username' in kwargs:
                if 'email' in kwargs:
                    if kwargs['username'] == user.username and kwargs['email'] == user.email:
                        if user in self.active_users:
                            return 'user already logged in'

                        password = kwargs['password'].encode("utf-8")
                        password_hash = hashlib.sha256(password).hexdigest()
                        if password_hash == user.password:
                            self.active_users.append(user)
                            return 'login successful'
                else:
                    if kwargs['username'] == user.username:
                        if user in self.active_users:
                            return 'user already logged in'

                        password = kwargs['password'].encode("utf-8")
                        password_hash = hashlib.sha256(password).hexdigest()
                        if password_hash == user.password:
                            self.active_users.append(user)
                            return 'login successful'
            else:
                if kwargs['email'] == user.email:
                    if user in self.active_users:
                        return 'user already logged in'

                    password = kwargs['password'].encode("utf-8")
                    password_hash = hashlib.sha256(password).hexdigest()
                    if password_hash == user.password:
                        self.active_users.append(user)
                        return 'login successful'

        return 'invalid login'


    def logout(self, user):
        if user not in self.active_users:
            return 'user is not logged in'

        self.active_users.remove(user)
        return 'logout successful'

    def __repr__(self):
        return "Site url:%s\nregister_users:%s\nactive_users:%s" % (self.url, self.register_users, self.active_users)

    def __str__(self):
        return self.url


class Account:
    def __init__(self, username, password, user_id, phone, email):
        self.username = self.username_validation(username)
        self.password = self.password_validation(password)
        self.user_id = self.id_validation(user_id)
        self.phone = self.phone_validation(phone)
        self.email = self.email_validation(email)


    def set_new_password(self, password):
        password = password.encode("utf-8")
        password_hash = hashlib.sha256(password).hexdigest()
        self.password = password_hash

    def username_validation(self, username):
        if not fullmatch('^[a-zA-Z]+_[a-zA-Z]+$', username):
            raise Exception('invalid username')

        return username

    def password_validation(self, password):
        if len(password) < 8:
            raise Exception('invalid password')

        if not (search('[A-Z]', password) or search('[a-z]', password) or search('[0-9]', password)):
            raise Exception('invalid password')

        password = password.encode("utf-8")
        password_hash = hashlib.sha256(password).hexdigest()
        return password_hash

    def id_validation(self, id):
        if len(id) != 10:
            raise Exception('invalid code melli')

        control_number = sum((10 - i) * int(x) for i, x in enumerate(id[:9])) % 11
        control_number = control_number if control_number < 2 else 11 - control_number
        if control_number != int(id[-1]):
            raise Exception('invalid code melli')

        return id

    def phone_validation(self, phone):
        if not fullmatch('^(0|\+98)9[0-9]{9}$', phone):
            raise Exception('invalid phone number')

        return phone

    def email_validation(self, email):
        if not fullmatch('^[a-zA-Z0-9\._-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]{2,5}$', email):
            raise Exception('invalid email')

        return email

    def __repr__(self):
        return self.username

    def __str__(self):
        return self.username


def show_welcome(func):
    def inner(user):
        full_name = user.username.replace('_', ' ').title()
        if len(full_name) > 15:
            full_name = full_name[:15] + '...'
        return func(full_name)
    return inner


def verify_change_password(func):
    def inner(user, old_pass, new_pass):
        password = old_pass.encode("utf-8")
        password_hash = hashlib.sha256(password).hexdigest()

        if password_hash == user.password:
            user.set_password(new_pass)

        return func(user, old_pass, new_pass)

    return inner


@show_welcome
def welcome(user):
    return ("welcome to our site %s" % user)


@verify_change_password
def change_password(user, old_pass, new_pass):
    return ("your password is changed successfully.")
