import sqlite3
import sys
#Sqlite path c:\\sqlite\\chinook.db
#Database manually must started before use.

def open_db_artist():
    artist_list = []
    conn = sqlite3.connect("C:\\sqlite\\chinook.db")
    cur = conn.cursor()
    member_data = cur.execute("SELECT * FROM artists")

    for rivi in member_data:
        artist_list.append(rivi)

    return artist_list
    conn.close()


def open_db_albums():
    Album_list = []
    conn = sqlite3.connect("C:\\sqlite\\chinook.db")
    cur = conn.cursor()
    member_data = cur.execute("SELECT * FROM albums")

    for rivi in member_data:
        Album_list.append(rivi)


    return Album_list
    conn.close()


def artist_id():
    artist_id = int(input("Give artist id number: "))
    jono = open_db_artist()


    for rivi in jono:
        if artist_id == rivi[0]:
            print("Artist name =" + str(rivi[1]) + "." + " Artist has id number: ", str(rivi[0]))
            name = str(rivi[1])
    albums = open_db_albums()

    print("")
    i = 0
    for rivi in albums:
        if artist_id == rivi[2]:
            print(str(name)+" album = " + str(rivi[1]))
            i = i + 1
    print("")
    print("Found " + str(i) + " " + name + " albums in database. \n")


def artist_name():
    Artist_name = str(input("Give  artist name  "))
    jono = open_db_artist()

    counter = 0
    for rivi in jono:
        if Artist_name == rivi[1]:
            print("Artist id =" + str(rivi[0]) + " and" + " name  =", str(rivi[1]))
            id = rivi[0]
            counter = counter + 1

    albums = open_db_albums()

    print()
    i = 0
    for rivi in albums:
        if id == rivi[2]:
            print("Album = " + str(rivi[1]))
            i = i + 1
    print("")
    print("Found " + str(i) + " " + Artist_name + " albums in database. \n")


def album_name(name):
    jono = open_db_artist()


    for rivi in jono:
        if name == rivi[1]:
            print("Artist name =" + str(rivi[1]) + "and" + " Artist id =", str(rivi[0]))


def main():
    print("Welcome to use  Chinook_db.\n")
    number_of_albums = open_db_albums()
    print("Albums in database " + str(len(number_of_albums)) + ".")
    number_of_artist = open_db_artist()
    print("Artist in database " + str(len(number_of_artist)) + ".")
    print("")
    while True:
        print("")
        print("Actions:\n1) List albums by Artist id. \n2) List Albums by artist name. \n0) for ending program.\n")
        valinta = int(input("Your choice > "))
        if valinta == 1:
            artist_id()

        elif valinta == 2:

            artist_name()
        elif valinta == 3:

            open_db_albums()
        elif valinta == 0:
            print("Thanks for use, bye")
            break


if __name__ == "__main__":
    main()
