import json
from models import User, Album

def save_users(users, filename="users.json"):
    data = [u.to_dict() for u in users]
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def load_users(filename="users.json"):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            return [User.from_dict(u) for u in data]
    except FileNotFoundError:
        return []

def save_albums(albums, filename="albums.json"):
    data = [a.to_dict() for a in albums]
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def load_albums(filename="albums.json"):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            return [Album.from_dict(a) for a in data]
    except FileNotFoundError:
        return []
