import random


class Playlist:
    def __init__(self, name, songs=None):
        if songs is None:
            songs = []
        self.name = name
        self.songs = songs

    def __str__(self):
        if len(self) == 0:
            return repr(self)
        str_prt = f"Playlist: {self.name}\n"
        for i, s in enumerate(self.songs):
            str_prt += f"{i + 1}. \t {s}\n"
        return str_prt

    def __repr__(self):
        return f"Playlist: {self.name}, {len(self)} songs"

    def __getitem__(self, index):
        return self.songs[index]

    def __setitem__(self, index, s):
        if index < len(self):
            self.songs[index] = s

    def __len__(self):
        return len(self.songs)


    def __eq__(self, other):
        if len(self) != len(other):
            return False
        for i in range(len(self)):
            if self[i] != other[i]:
                return False
        return True

    def __add__(self, other):
        return Playlist(self.name + other.name, self.songs + other.songs)

    def __contains__(self, s):
        return s in self.songs

    def __iter__(self):
        return iter(self.songs)

    def __bool__(self):
        if self.songs is None:
            return False
        if len(self) == 0:
            return False
        return True

    def __iadd__(self, song_or_playlist):
        if isinstance(song_or_playlist, Playlist):
            self.songs += song_or_playlist.songs
        elif isinstance(song_or_playlist, str):
            self.songs.append(song_or_playlist)
        return self

    def __delitem__(self, index):
        self.songs.pop(index)

    def add_song(self, s):
        self.songs.append(s)

    def remove_song(self, s):
        self.songs.remove(s)

    def shuffle(self):
        random.shuffle(self.songs)


# יצירת פלייליסטים
rock_playlist = Playlist("Rock Classics", ["Bohemian Rhapsody", "Straway to Heaven"])
pop_playlist = Playlist("Pop Hits", ["Shape of You", "Blinding Lights"])

# הדפסה
print(rock_playlist)
print(repr(pop_playlist))

# גישה ועדכון
print(rock_playlist[0])  # "Bohemian Rhapsody"
rock_playlist[1] = "Sweet Child O' Mine"

# אורך
print(len(rock_playlist))  # 2

# השוואה
print(rock_playlist == pop_playlist)  # False

# חיבור
all_music = rock_playlist + pop_playlist
print(all_music)

# בדיקות
print("Shape of You" in pop_playlist)  # True
print(bool(Playlist("Empty")))  # False

# איטרציה
for song in rock_playlist:
    print(f"Playing: {song}")

# הוספה למקום
rock_playlist += "Hotel California"
rock_playlist += pop_playlist

# הסרה
del rock_playlist[0]

# מתודות עזר
rock_playlist.add_song("November Rain")
rock_playlist.remove_song("Shape of You")
rock_playlist.shuffle()