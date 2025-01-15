class Albums:
    def __init__(self, dataPath: str):
        dataFile = self.read_file(dataPath)

        self.data = self.dataRead(dataFile)

    def read_file(self, file_name):
        with open(file_name, 'r', encoding="utf-8") as file:
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
        self.downloadNumber = items[4]
    
    def getArtist(self):
        return self.artist
    def getAlbum(self):
        return self.album
    def getSongsNumber(self):
        return self.songsNumber
    def getYear(self):
        return self.year
    def getDownloadNumber(self):
        return self.downloadNumber

    def toString(self):
        return f"{self.artist}\n{self.album}\n{self.songsNumber}\n{self.year}\n{self.downloadNumber}\n"
    


albums = Albums("Data.txt")

albums.dataPrint()