class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
    
    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, new_genre):
        cls.add_to_genre_count(new_genre)
        if new_genre not in cls.genres:
            cls.genres.append(new_genre)

    @classmethod
    def add_to_artists(cls, new_artist):
        cls.add_to_artist_count(new_artist)
        if new_artist not in cls.artists:
            cls.artists.append(new_artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if cls.genre_count.get(genre):
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if cls.artist_count.get(artist):
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1
