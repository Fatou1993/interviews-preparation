import heapq

class Client :
    counter = 1

    def __init__(self, name="anonymous", credits=0):
        self.id = Client.counter
        self.name = name
        self.credits = credits
        Client.counter += 1

    def __str__(self):
        return "( name : "+self.name+", id: "+str(self.id)+" ,credits: "+str(self.credits)+")"

class ClientsCreditsInfo :
    def __init__(self):
        self.clients = []
        self.inc = 0
        self.client_finder = {}
        self.REMOVED = "<REMOVED>"
        self.num_clients = 0

    def insert(self, client):
        id, credits = client.id, client.credits
        if id in self.client_finder :
            self.remove(client)
        credits -= self.inc #this element has less than the previous ones
        entry = [-credits, client] #enter -credits to have a max_heap
        self.client_finder[id] = entry
        heapq.heappush(self.clients, entry)
        self.num_clients += 1

    def remove(self, client):
        id, credits = client.id, client.credits
        if id in self.client_finder :
            entry = self.client_finder.pop(id) #remove from entry_finder
            entry[1] = self.REMOVED
            self.num_clients -= 1

    def lookUp(self, client):
        id, credits = client.id, client.credits
        if id in self.client_finder :
            entry = self.client_finder[id]
            return ((-entry[0]+self.inc), client)
        return None

    def addToAll(self, inc):
        self.inc += inc

    def getMax(self):
        if not self.num_clients :
            self.clients = []
            self.client_finder = {}
            self.inc = 0
        else:       
            while self.clients :
                entry = heapq.heappop(self.clients)
                if entry[1] != self.REMOVED :
                    credits, id = entry[0], entry[1].id
                    self.client_finder.pop(id) #delete from client finder
                    self.num_clients -= 1
                    return (-credits+self.inc, entry[1])
        return None


    def isNotEmpty(self):
        return self.num_clients != 0

if __name__ == "__main__":
    names = ["A", "B", "C"]
    credits = [1,2,3]
    clients = []
    creditsInfo = ClientsCreditsInfo()
    for i in range(3):
        clients.append(Client(names[i], credits[i]))
    for c in clients :
        creditsInfo.insert(c)
        #print c
    creditsInfo.addToAll(5)

    while creditsInfo.isNotEmpty():
        c = creditsInfo.getMax()
        print c[0], c[1]



