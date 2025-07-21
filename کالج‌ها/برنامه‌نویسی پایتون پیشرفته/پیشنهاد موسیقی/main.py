all_users = {}
all_albums = {}


def add_user(username: str, age: int, city: str, albums: list, all_users: dict) -> None:
    new_user = {
        "age": age,
        "city": city,
        "albums": albums
    }
    all_users[username] = new_user


def add_album(name: str, artist: str, genre: str, tracks: int, all_albums: dict) -> None:
    new_album = {
        "artist": artist,
        "genre": genre,
        "tracks": tracks
    }
    all_albums[name] = new_album


def query_user_artist(username: str, artist: str, all_users: dict, all_albums: dict) -> int:
    result = 0

    for album in all_users[username]["albums"]:
        if all_albums[album]["artist"] == artist:
            result += all_albums[album]["tracks"]

    return result


def query_user_genre(username: str, genre: str, all_users: dict, all_albums: dict) -> int:
    result = 0

    for album in all_users[username]["albums"]:
        if all_albums[album]["genre"] == genre:
            result += all_albums[album]["tracks"]

    return result


def query_age_artist(age: int, artist: str, all_users: dict, all_albums: dict) -> int:
    result = 0

    for username, info in all_users.items():
        if info["age"] == age:
            for album in all_users[username]["albums"]:
                if all_albums[album]["artist"] == artist:
                    result += all_albums[album]["tracks"]

    return result


def query_age_genre(age: int, genre: str, all_users: dict, all_albums: dict) -> int:
    result = 0

    for username, info in all_users.items():
        if info["age"] == age:
            for album in all_users[username]["albums"]:
                if all_albums[album]["genre"] == genre:
                    result += all_albums[album]["tracks"]

    return result


def query_city_artist(city: str, artist: str, all_users: dict, all_albums: dict) -> int:
    result = 0

    for username, info in all_users.items():
        if info["city"] == city:
            for album in all_users[username]["albums"]:
                if all_albums[album]["artist"] == artist:
                    result += all_albums[album]["tracks"]

    return result


def query_city_genre(city: str, genre: str, all_users: dict, all_albums: dict) -> int:
    result = 0

    for username, info in all_users.items():
        if info["city"] == city:
            for album in all_users[username]["albums"]:
                if all_albums[album]["genre"] == genre:
                    result += all_albums[album]["tracks"]

    return result
