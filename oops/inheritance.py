# strcuture  of a ytchannel
class Ytchannel:
    def __init__(self , name):
        self.name = name 
        self.subscribercnt = 0 
        self.videos = []
    def subscriber(self):
        self.subscribercnt  += 1
    
    def unsubscriber(self):
        self.subscribercnt  -= 1

    def setName(self , name):
        self.name = name

    def getInfo(self):
        return { 'name':self.name , 'subscriber' : self.subscribercnt}
    
    def uploadVideo(self , video):
        self.videos.append(video)
    def listVideos(self):
        print("")
        for video in self.videos:
            print(video , end = " ")
        print("")
        
T = Ytchannel('Telsuko')
T.subscriber()
T.subscriber()
print(T.getInfo())

class CookingYtchanner(Ytchannel) : 
    def __init__(self , name) :
         Ytchannel.__init__(self , name)
         self.quality = 0 
        
    def Quality(self):
        self.quality = 360
    
    def setQuality(self, quality):
        self.quality = quality 

    def getQuality(self):
        return self.quality 
    def getInfo(self):
        print(self.quality)
        return Ytchannel.getInfo(self)

    def Cooking(self):
        print("Sravani is comfortable  in making recipes")
        

Cookie = CookingYtchanner("Sravans kitchen")
Cookie.uploadVideo("Ariselu recipe")
Cookie.uploadVideo("Gulab jam recipe")
Cookie.listVideos()
Cookie.setQuality(480)
print(Cookie.getInfo())
Cookie.Cooking()


    
