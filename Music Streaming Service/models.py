class Track:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration  # в секундах

    def __str__(self):
        minutes = self.duration // 60
        seconds = self.duration % 60
        return f"{self.title} - {self.artist} ({minutes}:{seconds:02d})"

    def to_dict(self):
        return {"title": self.title, "artist": self.artist, "duration": self.duration}

    @staticmethod
    def from_dict(data):
        return Track(data['title'], data['artist'], data['duration'])


class Album:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.tracks = []

    def add_track(self, track):
        if isinstance(track, Track):
            self.tracks.append(track)

    def show_tracks(self):
        print(f"Альбом: {self.title} - {self.artist}")
        for track in self.tracks:
            print(track)

    def to_dict(self):
        return {"title": self.title, "artist": self.artist,
                "tracks": [t.to_dict() for t in self.tracks]}

    @staticmethod
    def from_dict(data):
        album = Album(data['title'], data['artist'])
        album.tracks = [Track.from_dict(t) for t in data['tracks']]
        return album


class Playlist:
    def __init__(self, title):
        self.title = title
        self.tracks = []

    def add_track(self, track):
        if isinstance(track, Track):
            self.tracks.append(track)

    def remove_track(self, track_title):
        for track in self.tracks:
            if track.title.lower() == track_title.lower():
                self.tracks.remove(track)
                return True
        return False

    def total_duration(self):
        return sum(track.duration for track in self.tracks)

    def show_tracks(self):
        print(f"Плейлист: {self.title}")
        for track in self.tracks:
            print(track)
        total_min = self.total_duration() // 60
        total_sec = self.total_duration() % 60
        print(f"Общая длительность: {total_min}:{total_sec:02d}")

    def to_dict(self):
        return {"title": self.title, "tracks": [t.to_dict() for t in self.tracks]}

    @staticmethod
    def from_dict(data):
        playlist = Playlist(data['title'])
        playlist.tracks = [Track.from_dict(t) for t in data['tracks']]
        return playlist


class User:
    def __init__(self, username):
        self.username = username
        self.playlists = []

    def create_playlist(self, title):
        playlist = Playlist(title)
        self.playlists.append(playlist)
        return playlist

    def show_playlists(self):
        print(f"Плейлисты пользователя {self.username}:")
        for pl in self.playlists:
            print(f"- {pl.title}")

    def to_dict(self):
        return {"username": self.username,
                "playlists": [p.to_dict() for p in self.playlists]}

    @staticmethod
    def from_dict(data):
        user = User(data['username'])
        user.playlists = [Playlist.from_dict(p) for p in data['playlists']]
        return user
