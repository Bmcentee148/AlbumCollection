import musiclib
from musiclib import Album
from musiclib import Album_Collection

#Attempt to get album collection from data_file
album_list = musiclib.get_albums_from_file('album_data.pkl')

if album_list :
    for album in album_list :
        album.to_string()

if not album_list :
    album_list.append(Album("Beatles","Sgt. Pepper", 1967))

album_list.append(Album("None","None",0000))
musiclib.save_albums_to_file('album_data.pkl', album_list)