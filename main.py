#Candidate -> Harsh PV
#Email -> harsh.pv07@gmail.com 
# Read README.md to run the file


import os,json,datetime,heapq,threading
from threading import Thread



class store:
    defloc = "" 
    del_cnt = 0
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
            if(len(data) == 0): #check if file is empty
                break
            for i,j in data.items():
                if("ttl" in j): #If TTL property of specified with the value
                    a = datetime.datetime(j["year"] , j["month"] ,j["date"] ,j["hour"] ,j["minute"] ,j["seconds"]) #Get the time of insertion from the 
                    if(datetime.datetime.now() > a + datetime.timedelta(seconds = j["ttl"])): #Check for the condition with current time,ttl and time of insertion
                        self.delete(i)
                        self.del_cnt -= 1
                        print(str(i) + " " + "sucessfully deleted using TTL")
            if(self.del_cnt == 0): #Break and Kill thread when all TTL Keys have expired
                print("______All operations done______")
                break
                
    
    
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
                            if("ttl" in value):
                                self.del_cnt += 1
                            dic[key] = value 
                            dic[key]["year"] = datetime.datetime.now().year # Insert a mandatory key-val pair for time properties (time of insertion)
                            dic[key]["month"] = datetime.datetime.now().month
                            dic[key]["date"] = datetime.datetime.now().day
                            dic[key]["hour"] = datetime.datetime.now().hour
                            dic[key]["minute"] = datetime.datetime.now().minute
                            dic[key]["seconds"] = datetime.datetime.now().second
                            with open(self.defloc, 'w') as fp:
                                json.dump(dic, fp) #dump key-val pairs into .json file
                            print(str(key) + " " + "sucessfully inserted")
                        else:
                            print("Duplicate key " + str(key)) #If duplicate key is found 
                            pass



    def read(self , key): #Return the value
        with open(self.defloc, 'r') as data_file: #Read the .json file
            keyss = json.load(data_file)
        if(key in keyss): #Check if key is present
            print(keyss[key]) #return value of key
        else:
            print("Key " + str(key) + " not found") #If key not found 
    

    
    def delete(self , key): #Delete the key-value pair
        with open(self.defloc) as df: #Read the json file
            data = json.load(df)
        if(key not in data): #If key not found
            print("Key "  + str(key) + " not found. Invalid Delete operation")
        else:
            del (data[key]) #If key is found
            print("Key " +  str(key) + " succesfully deleted")
            with open(self.defloc , 'w') as df:
                data = json.dump(data , df) #Write data without the deleted key

    
    


if __name__ == "__main__":
    
    cls = store("./data_store.json") #define the location of the json store file (or) keep it as "store(None)"
    
    
    #Perform all operations here
    cls.create("kumar" , {"age":20 , "height": 170}) #cls.create("key" ,"Json Object")
    cls.create("raj" , {"age":80 , "height": 10}) #Record creation Example
    cls.create("giriqwertyuiasdfghjkzxcvbnmsdfbsjdfb" , {"age":80 , "height": 10 , "ttl" : 5}) #Example of oversized key
    cls.create("rajesh" , {"age":71 , "height": 10 }) #Record creation Example
    cls.create("giri" , {"age":80 , "height": 10 , "ttl" : 5}) #Example of TTL
    cls.read("raj") #Data Read Example
    cls.read("jacob")  #Read unknown key Example
    cls.delete("kumar") #Delete Example
    cls.delete("kumar") #Delete for unknown data 
    

    t1 = threading.Thread(cls.ttl()) #Run a separate thread for TTL detection
    t1.start()
    
    
