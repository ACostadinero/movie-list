import imdb
import sys
import sqlite3
import fileinput
import os

filename = "D:\\Projects\\lista_filme.txt"

def meniu():

    print("------ Comenzi ------")
    print("|   l = lista ta    |")
    print("|   t = top filme   |")
    print("|   n = adauga nota |")
    print("|   a = adauga film |")
    print("|   s = sterge film |")
    print("|    q = iesire     |")
    print("----------A.C---------")
    

def topFilme():
    x = input('Alege topul filmelor IMDb pe care vrei sa il vezi: ')
    ia = imdb.IMDb()
    search = ia.get_top250_movies()
    for i in range(int(x)):
        print(str(int(i+1)) + '.' + ' ' + str(search[i]))
    

def adaugaNota():
    f = open(filename,"r+")
    film = input("Carui film vrei sa ii dai nota: ")
    nota = input("Ce nota vrei sa ii dai filmului: ")
    contents = f.read().replace(film, film + " " + nota + "/10")
    f.seek(0)
    f.truncate()
    f.write(contents)
        
def adaugaFilm():
    film = input("Ce film vrei sa adaugi in lista: ")
    f= open(filename,"a")
    f.write("\n" + film + "\n")
    f.close

def stergeFilm():
    f = open(filename,"r+")
    film = input("Ce film vrei sa stergi din lista: ")
    contents = f.read().replace(film, str(0))
    f.seek(0)
    f.truncate()
    f.write(contents)


def listaTa():   
    filehandle = open(filename,"r")
    filedata = filehandle.read()
    print(filedata)
    

while True:
    os.system('clear')
    meniu()
    choice = input('Ce vrei sa faci: ')
    if choice == "q":
        sys.exit()
    elif choice == "t":
        topFilme()
    elif choice == "l":
        listaTa()
    elif choice == "n":
        adaugaNota()
    elif choice == "a":
        adaugaFilm()
    elif choice =="s":
        stergeFilm()
    

