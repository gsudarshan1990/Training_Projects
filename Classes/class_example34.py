#We've given you a class called "Song" that represents
#some basic information about a song. We also wrote a
#class called "Artist" which contains some basic
#information about an artist.
#
#Your job is to create three instances of the song class,
#called song_1, song_2, and song_3.
#

#Write a function called "get_song_string". It should accept
#one argument which will be a Song object. It should return
#a string in the following format:
#
# "<song name>" - <artist name> (<song year>)
# e.g:
# "You Belong With Me" - Taylor Swift (2008)

#


class Artist:
    """This class contains the basic information related to the Artist"""
    def __init__(self, name, label):
        """This is used to initialize the artists i.e sets the name and labels"""
        self.name = name
        self.label = label

    def __str__(self):
        """This represents the artists in the string format"""
        return "Artist Name:"+self.name+" label:"+self.label

class Song:
    """This class contains the basic information related to the Song"""
    def __init__(self, name, album, year, artist):
        """This is used to initialize the song i.e name of the song, song type,year of relaase and published by """
        self.name = name
        self.album = album
        self.year = year
        self.artist = artist

    def __str__(self):
        """This represents the song name"""
        return "Song name:"+self.name+" "*5+" Album:"+self.album+" "*5+" year:"+str(self.year)+" "*5+ " artist:"+str(self.artist)

def get_song_string(song_object):
    """This function returns the information related to the song"""
    song_name = song_object.name
    song_artist = song_object.artist.name
    song_year = song_object.year
    return '"'+song_name+'"'+" - "+song_artist+" ("+str(song_year)+")"

#song_-1 should have the following attributes:
#   name = "You Belong With Me"
#   album = "Fearless"
#   year = 2006
#   artist.name = "Taylor Swift"
#   artist.label = "Big Machine Records, LLC"
#

song1 = Song("You Belong With Me", "Fearless", 2008, Artist("Taylor Swift", "Big Machine Records, LLC"))

#song_1 should have the following attributes:
#   name = "All Too Well"
#   album = "Red"
#   year = 2012
#   artist.name = "Taylor Swift"
#   artist.label = "Big Machine Records, LLC"

artist2 = Artist("Taylor Swift","Big Machine Records, LLC")
song2 = Song("All Too Well", "Red", 2012, artist2)

#song_2 should have the following attributes:
#   name = "Up We Go"
#   album = "Midnight Machines"
#   year = 2015
#   artist.name = "LiGHTS"
#   artist.label = "Warner Bros. Records Inc."

song3 = Song("Up We Go", "Midnight Machines", 2016, Artist("LiGHTS","Warner Bros. Records Inc."))

print(song1)
print(song2)
print(song3)
print(get_song_string(song1))
