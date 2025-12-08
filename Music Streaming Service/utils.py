def find_track_by_title(tracks, title):
    if not title.strip():
        raise ValueError("Название трека не может быть пустым!")
    result = [t for t in tracks if title.lower() in t.title.lower()]
    if not result:
        raise LookupError(f"Трек с названием '{title}' не найден.")
    return result

def find_track_by_artist(tracks, artist):
    if not artist.strip():
        raise ValueError("Имя исполнителя не может быть пустым!")
    result = [t for t in tracks if artist.lower() in t.artist.lower()]
    if not result:
        raise LookupError(f"Исполнитель '{artist}' не найден.")
    return result
