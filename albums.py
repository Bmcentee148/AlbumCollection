import time

class Album(object) :

    def __init__(self, artist, title, year) :
        self.artist = artist.lower()
        self.title = title.lower()
        self.year = year

    def get_age(self) :
        return time.gmtime().tm_year - self.year

    def get_title(self) :
        return self.title

    def get_artist(self) :
        return self.artist

    def get_year(self) :
        return self.year

    def to_string(self) :
        print "Album: ", self.title
        print "Artist: ", self.artist
        print "Year: ", self.year

    def __eq__(self, other) :
        return (self.artist == other.artist and
            self.title == other.title and
            self.year == other.year)

class Album_Collection(object) :
    # Class attributes for search key choices
    YEAR_SEARCH = 0
    ARTIST_SEARCH = 1
    TITLE_SEARCH = 2
    def __init__(self) :
        self.albums = []

    def add_album(self, album) :
        if album not in self.albums :
            self.albums.append(album)


    def add_albums(self, mult_albums) :
        for album in mult_albums :
            self.add_album(album)

    def get_albums(self) :
        return albums[:]

    def get_sorted_albums(self, key_type) :
        if key_type == Album_Collection.YEAR_SEARCH :
            search_key = lambda x: x.year
        elif key_type == Album_Collection.ARTIST_SEARCH :
            search_key = lambda x: x.artist
        elif key_type == Album_Collection.TITLE_SEARCH :
            search_key = lambda x: x.title
        return sorted(self.albums, key = search_key)


def main() :
    #-------------- CLASS TESTING ----------------------------------------------
    albs_coll = Album_Collection()
    albs_coll.add_album(Album('Beatles', 'Sgt. Pepper', 1967))
    albs_coll.add_album(Album('Beach Boys', 'Pet Sounds', 1966))
    albs_coll.add_albums([ Album('Beatles', 'Abbey Road', 1969),
        Album('Radiohead', 'Ok Computer', 1992) ])
    albs_coll.add_album(Album('Beatles', 'Sgt. Pepper', 1967))
    albums_sorted = albs_coll.get_sorted_albums(Album_Collection.TITLE_SEARCH)
    for album in albums_sorted :
        album.to_string()
    print '=' * 20
    albs_coll.albums.sort(key=lambda x: x.year)
    for album in albs_coll.albums :
        album.to_string()

if __name__ == "__main__" :
    main()

