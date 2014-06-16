class Song:
    def __init__(self, artist,title,minutes,seconds):
        self.artist=artist
        self.title=title
        self.minutes=minutes
        self.seconds=seconds
    def __str__(self):
        return self.artist+','+self.title+'('+str(self.minutes)+':'+str(self.seconds)+')'
if __name__ == '__main__':
    s1=Song("Kishor Kumar","Zindagi ka safar",7,34)
    s2=Song("Mukesh Kumar","tum yaad na aaye",5,23)
    print(s1)
    print(s2)
    
