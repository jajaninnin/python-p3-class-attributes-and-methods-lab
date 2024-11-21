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
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)
        
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artist(artist)
    
    @classmethod
    def add_song_to_count(cls):
        cls.count += 1
    
    @classmethod
    def add_to_genres(cls, new_genre):
        cls.genres.append(new_genre)
    
    @classmethod
    def add_to_artist(cls, new_artist):
        cls.artists.append(new_artist)

    @classmethod
    def add_to_genre_count(cls, curr_genre):
        if curr_genre in cls.genre_count:
             cls.genre_count[curr_genre] += 1
        else:
            cls.genre_count[curr_genre] = 1
        # for curr_genre in cls.genres:

            # if curr_genre in cls.genre_count:
            #     print('curr_genre', curr_genre)
            #     cls.genre_count[curr_genre] += 1
            # else:
            #     cls.genre_count[curr_genre] = 1

    @classmethod
    def add_to_artist_count(cls, curr_artist):
        if curr_artist in cls.artist_count:
            cls.artist_count[curr_artist] += 1
        else:
            cls.artist_count[curr_artist] = 1

    def __repr__(self):
        return f"<name={self.name}, artist={self.artist}, genre={self.genre}>"


# ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")
# print(ninety_nine_problems)
# print(ninety_nine_problems.name)
# print(ninety_nine_problems.artist)
# print(ninety_nine_problems.genre)