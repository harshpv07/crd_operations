import os,json,datetime,heapq,threading
from threading import Thread

class store:
    defloc = "" 
    def __init__(self ,  loc): #Constructor for file location
        if(os.path.exists(loc) == False): #Create a new file if not found
            with open(loc , 'w') as data:
                data.write("{}")
            self.defloc = loc #Initialize the constructor

        else:
            if(loc == None): #If file is present initialize the constructor
                self.defloc = str(os.getcwd()) + "\data_store.json"
            else:
                self.defloc = loc
    
    
    def ttl(self):
        while True:
            with open(self.defloc) as df:
                data = json.load(df)
            if(len(data) == 0):
                break
            for i,j in data.items():
                if("ttl" in j):
                    a = datetime.datetime(j["year"] , j["month"] ,j["date"] ,j["hour"] ,j["minute"] ,j["seconds"])
                    if(datetime.datetime.now() > a + datetime.timedelta(seconds = j["ttl"])):
                        self.delete(i)
                        print("Sucessfully deleted using TTL")
                        #print(str(i) + " " + "yes, time to delete")
                    else:
                        print(str(i) + " " + "no yet")
                # print(a , end = " ")
                # print(j["ttl"] , end = " ")
                # print()

                
    
    
    def create(self , key , value):
        dic = {}
        if(type(key) != str): #if key is not a string
            print("Enter a string as key")
        else:
            if(len(key)>32): #check if key size is greater than 32
                print("Enter a string that is less than 32 chars")
            else:
                
                if(int(len(str(value).encode("utf-8"))/1000) > 16): #check if value size is less than 16KB
                    print("Size of JSON object should be less than 16KB")
                else:
                    with open(self.defloc) as w:  #read the entire file and insert into the file
                        json_decoded = json.load(w)
                        for i,j in json_decoded.items():
                            dic[i] = j
                        if str(key) not in dic:
                            dic[key] = value 
                            dic[key]["year"] = datetime.datetime.now().year # Insert a mandatory key-val pair for time properties (time of insertion)
                            dic[key]["month"] = datetime.datetime.now().month
                            dic[key]["date"] = datetime.datetime.now().day
                            dic[key]["hour"] = datetime.datetime.now().hour
                            dic[key]["minute"] = datetime.datetime.now().minute
                            dic[key]["seconds"] = datetime.datetime.now().second
                            with open(self.defloc, 'w') as fp:
                                json.dump(dic, fp) #dump key-val pairs into .json file
                            print("Sucessfully inserted")
                        else:
                            print("Duplicate key found") #If duplicate key is found 
                            pass


        #print(dic)
    def read(self , key):
        with open(self.defloc, 'r') as data_file: #Read the .json file
            keyss = json.load(data_file)
        if(key in keyss): #Check if key is present
            print(keyss[key]) #return value of key
        else:
            print("Key not found") #If key not found 
    
    def delete(self , key):
        with open(self.defloc) as df: #Read the json file
            data = json.load(df)
        if(key not in data): #If key not found
            print("Key not found. Invalid Delete operation")
        else:
            del (data[key]) #If key is found
            print("Succesfully deleted")
            with open(self.defloc , 'w') as df:
                data = json.dump(data , df) #Write data without the deleted key

    
    


if __name__ == "__main__":
    cls = store("C:/Users/PREMRAJ/Desktop/crd_operations/data_store.json") #define the location of the file (or) keep it as "store(None)"
    cls.create("kumar" , {"age":20 , "height": 170 , "ttl" : 2})
    cls.create("raj" , {"age":80 , "height": 10 , "ttl" : 10})
    cls.create("bheem" , {"age":80 , "height": 10 , "ttl" : 5})
    cls.create("rajesh" , {"age":71 , "height": 10 })
    cls.read("raj")
    t1 = threading.Thread(cls.ttl())
    t1.start()
    
