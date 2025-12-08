from models import Track, Album, User
from storage import load_users, save_users, load_albums, save_albums
from utils import find_track_by_title, find_track_by_artist

def main():
    users = load_users()
    albums = load_albums()

    # Пример начальных данных
    if not albums:
        track1 = Track("Shape of You", "Ed Sheeran", 240)
        track2 = Track("Blinding Lights", "The Weeknd", 200)
        track3 = Track("Levitating", "Dua Lipa", 210)
        track4 = Track("Save Your Tears", "The Weeknd", 215)
        album1 = Album("Хиты 2020", "Разные исполнители")
        album1.add_track(track1)
        album1.add_track(track2)
        album1.add_track(track3)
        album1.add_track(track4)
        albums.append(album1)
        save_albums(albums)

    print("=== Музыкальный сервис ===")
    while True:
        print("\nВыберите действие:")
        print("1. Просмотреть альбомы")
        print("2. Создать пользователя")
        print("3. Просмотреть плейлисты пользователя")
        print("4. Создать плейлист")
        print("5. Добавить трек в плейлист")
        print("6. Удалить трек из плейлиста")
        print("7. Поиск трека по названию")
        print("8. Поиск трека по исполнителю")
        print("0. Выход")

        choice = input("Введите номер действия: ")

        if choice == "1":
            for alb in albums:
                alb.show_tracks()

        elif choice == "2":
            username = input("Введите имя пользователя: ")
            if username.strip():
                user = User(username)
                users.append(user)
                save_users(users)
                print(f"Пользователь {username} создан.")
            else:
                print("Ошибка: имя пользователя не может быть пустым.")

        elif choice == "3":
            username = input("Введите имя пользователя: ")
            user = next((u for u in users if u.username == username), None)
            if user:
                user.show_playlists()
            else:
                print("Пользователь не найден.")

        elif choice == "4":
            username = input("Введите имя пользователя: ")
            user = next((u for u in users if u.username == username), None)
            if user:
                pl_name = input("Название плейлиста: ")
                if pl_name.strip():
                    user.create_playlist(pl_name)
                    save_users(users)
                    print(f"Плейлист {pl_name} создан.")
                else:
                    print("Ошибка: название плейлиста не может быть пустым.")
            else:
                print("Пользователь не найден.")

        elif choice == "5":
            username = input("Введите имя пользователя: ")
            user = next((u for u in users if u.username == username), None)
            if user:
                pl_name = input("Название плейлиста: ")
                playlist = next((p for p in user.playlists if p.title == pl_name), None)
                if playlist:
                    print("Доступные треки:")
                    for alb in albums:
                        for t in alb.tracks:
                            print(f"- {t.title} ({t.artist})")
                    track_name = input("Название трека для добавления: ")
                    track = next((t for alb in albums for t in alb.tracks if t.title == track_name), None)
                    if track:
                        playlist.add_track(track)
                        save_users(users)
                        print("Трек добавлен.")
                    else:
                        print("Трек не найден.")
                else:
                    print("Плейлист не найден.")
            else:
                print("Пользователь не найден.")

        elif choice == "6":
            username = input("Введите имя пользователя: ")
            user = next((u for u in users if u.username == username), None)
            if user:
                pl_name = input("Название плейлиста: ")
                playlist = next((p for p in user.playlists if p.title == pl_name), None)
                if playlist:
                    track_name = input("Название трека для удаления: ")
                    if playlist.remove_track(track_name):
                        save_users(users)
                        print("Трек удален.")
                    else:
                        print("Трек не найден в плейлисте.")
                else:
                    print("Плейлист не найден.")
            else:
                print("Пользователь не найден.")

        elif choice == "7":
            title = input("Название трека: ")
            try:
                found = find_track_by_title([t for alb in albums for t in alb.tracks], title)
                for t in found:
                    print(t)
            except (ValueError, LookupError) as e:
                print(f"Ошибка: {e}")

        elif choice == "8":
            artist = input("Имя исполнителя: ")
            try:
                found = find_track_by_artist([t for alb in albums for t in alb.tracks], artist)
                for t in found:
                    print(t)
            except (ValueError, LookupError) as e:
                print(f"Ошибка: {e}")

        elif choice == "0":
            print("Выход из программы...")
            break

        else:
            print("Некорректный ввод. Попробуйте снова.")

if __name__ == "__main__":
    main()
