import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.uic import loadUi

class Albums:
    '''
    nazwa funkcji:          __init__
    opis funkcji:           Jest to bazowy konstruktor klasy
    parametry:              dataPath to parametr przyjmujący ścieżke pliku z danymi o typie string
    zwracany typ i opis:    brak
    autor:                  00000000000
    '''
    def __init__(self, dataPath: str):
        dataFile = self.readFile(dataPath)

        self.data = self.dataRead(dataFile)

    
    '''
    nazwa funkcji:          readFile
    opis funkcji:           Metoda wczytująca dane z pliku tekstowego
    parametry:              file_name, parametr przyjmujący nazwę pliku/ścieżkę pliku typu tekstowego
    zwracany typ i opis:    string, dane odczytane z pliku
    autor:                  00000000000
    '''
    def readFile(self, fileName: str):
        with open(fileName, 'r', encoding="utf-8") as file:
            return file.read()

    def dataRead(self, dataFile: str):
        data: Album = []
        for el in dataFile.split("\n\n"):
            items = el.replace("ď»ż", "")[:-1].split("\n")
            data.append(Album(items))
        return data
    
    def dataPrint(self):
        for el in self.data:
            print(el.toString())
            

class Album:
    def __init__(self, items):
        self.artist = items[0]
        self.album = items[1]
        self.songsNumber = items[2]
        self.year = items[3]
        self.downloadNumber = int(items[4])
    
    def getArtist(self):
        return self.artist
    def getAlbum(self):
        return self.album
    def getSongsNumber(self):
        return self.songsNumber
    def getYear(self):
        return self.year
    def getDownloadNumber(self):
        return str(self.downloadNumber)
    
    def addDownloads(self):
        self.downloadNumber += 1

    def toString(self):
        return f"{self.artist}\n{self.album}\n{self.songsNumber}\n{self.year}\n{self.downloadNumber}\n"

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("design.ui", self)
        self.albums: Albums = Albums("Data.txt")
        self.albumN = 0
        self.setAlbum(self.albumN)

        self.left.clicked.connect(self.previous)
        self.right.clicked.connect(self.next)

        self.download.clicked.connect(self.addDownloads)

    def previous(self):
        if self.albumN-1 < 0: self.albumN = len(self.albums.data)-1
        else: self.albumN -= 1
        self.setAlbum(self.albumN)

    def next(self):
        if self.albumN >= len(self.albums.data)-1: self.albumN = 0
        else: self.albumN += 1
        self.setAlbum(self.albumN)
        
    def setAlbum(self, albumN):
        self.artist.setText(self.albums.data[albumN].getArtist())
        self.album.setText(self.albums.data[albumN].getAlbum())
        self.songsN.setText(self.albums.data[albumN].getSongsNumber())
        self.date.setText(self.albums.data[albumN].getYear())
        self.downloadN.setText(self.albums.data[albumN].getDownloadNumber())

    def addDownloads(self):
        self.albums.data[self.albumN].addDownloads()
        self.setAlbum(self.albumN)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())