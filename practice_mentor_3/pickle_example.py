import random
from copy import deepcopy
import json
import pickle


class Song:
    def __init__(self, title: str, artist: str):
        self.title = title
        self.artist = artist

    def __getstate__(self):
        return self.__dict__.copy()

    def __setstate__(self, state: dict):
        self.__dict__.update(state)

    def to_dict(self):
        return {"title": self.title, "artist": self.artist}

    @staticmethod
    def from_dict(song_dict: dict):
        return Song(song_dict['title'], song_dict['artist'])

    def __eq__(self, value) -> bool:
        return isinstance(value, Song) and self.title == value.title and self.artist == value.artist

    def __str__(self):
        return f'"{self.title}" by {self.artist}'

    def __repr__(self):
        return str(self)

    def __hash__(self):
        return hash((self.title, self.artist))


class Playlist:
    def __init__(self, songs=None):
        self.songs = songs if songs else []
        self.shuffle = False

    def __iter__(self):
        return ShuffleIterator(self.songs) if self.shuffle else PlaylistIterator(self.songs)

    def toggle_shuffle(self):
        self.shuffle = not self.shuffle

    def add_song(self, song: Song):
        self.songs.append(song)  # FIXED

    def to_dict(self):
        return {"songs": [song.to_dict() for song in self.songs]}

    @staticmethod
    def from_dict(playlist_dict: dict):
        songs = [Song.from_dict(song) for song in playlist_dict['songs']]
        return Playlist(songs)

    def __getstate__(self):
        return self.to_dict()

    def __setstate__(self, state):
        self.songs = [Song.from_dict(song) for song in state["songs"]]


class PlaylistIterator:
    def __init__(self, songs: list[Song]):
        self.current_index = 0
        self.songs = songs

    def __iter__(self):  # FIXED
        return self

    def __next__(self):
        if self.current_index < len(self.songs):
            song = self.songs[self.current_index]
            self.current_index += 1
            return song
        raise StopIteration


class ShuffleIterator:
    def __init__(self, songs: list[Song]):
        self.current_index = 0
        self.songs = deepcopy(songs)
        random.shuffle(self.songs)

    def __iter__(self):  # FIXED
        return self

    def __next__(self):
        if self.current_index < len(self.songs):
            song = self.songs[self.current_index]
            self.current_index += 1
            return song
        raise StopIteration


# Testing
songs = [
    Song('Thunderstruck', 'AC/DC'),
    Song('Smells Like Teen Spirit', 'Nirvana'),
]

playlist = Playlist(songs)

# JSON Serialization
with open('playlist.json', 'w') as json_file:
    json.dump(playlist.to_dict(), json_file, indent=4)

# JSON Deserialization
with open('playlist.json', 'r') as json_file:
    playlist_two = Playlist.from_dict(json.load(json_file))
    print("Loaded from JSON:", playlist_two.songs)

# Pickle Serialization
with open('playlist.pkl', 'wb') as pickle_file:
    pickle.dump(playlist, pickle_file)

# Pickle Deserialization
with open('playlist.pkl', 'rb') as pickle_file:
    playlist_three = pickle.load(pickle_file)
    print("Loaded from Pickle:", playlist_three.songs)

# Testing Iterators
playlist.toggle_shuffle()
for song in playlist:
    print("Playing:", song)
