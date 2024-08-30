import requests

class Detective:
    def login(self, username: str, password: str, login_url: str):
        my_data = {'username': username, 'password': password}
        post = requests.post(login_url, data=my_data)
        if post.status_code == 200:
            message = {'full_name': f'{post.json()["first_name"]} {post.json()["last_name"]}',
                       'email': post.json()['email']}
            return message
        raise Exception(f'[{post.status_code}]: Unable to log in with provided credentials.')

    def upload_clues(self):
        pass
        #TODO: Complete upload_clues Function

    def html_scraper(self):
        pass
        #TODO: Complete upload_clues Function
