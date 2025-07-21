import socket, json


class Network:

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.data = dict()

    def start(self):
        self.s.connect((self.host, self.port))
        raw_data = self.s.recv(4096).decode('ascii')
        with open('config.json', 'w') as f:
            f.write(raw_data)

        self.data = json.loads(raw_data)

    def send_data(self, keys):
        full_key = f"snake_{self.data['id']}_"
        full_key += keys[0] if len(keys) > 0 else "no_key"

        data = {
            "keys": [full_key],
            "dead": False
        }

        self.s.send(json.dumps(data).encode('ascii'))


    def get_data(self):
        data = self.s.recv(4096).decode('ascii').replace("'", '"')
        data = json.loads(data)
        return data
