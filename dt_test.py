import datetime
print(datetime.datetime.now())











# import os,json,datetime,heapq

# class store:
#     defloc = ""
#     def __init__(self ,  loc):
#         if(os.path.exists(loc) == False):
#             with open(loc , 'w') as data:
#                 data.write("{}")
#             self.defloc = loc

#         else:
#             if(loc == None):
#                 self.defloc = str(os.getcwd()) + "\data_store.json"
#             else:
#                 self.defloc = loc
    
#     def create(self , key , value):
#         dic = {}
#         if(type(key) != str):
#             print("Enter a string as key")
#         else:
#             if(len(key)>32):
#                 print("Enter a string that is less than 32 chars")
#             else:
                
#                 if(int(len(str(value).encode("utf-8"))/1000) > 16):
#                     print("Size of JSON object should be less than 16KB")
#                 else:
#                     with open(self.defloc) as w:
#                         json_decoded = json.load(w)
#                         for i,j in json_decoded.items():
#                             dic[i] = j
#                         if str(key) not in dic:
#                             dic[key] = value
#                             dic[key]["year"] = datetime.datetime.now().year
#                             dic[key]["month"] = datetime.datetime.now().month
#                             dic[key]["date"] = datetime.datetime.now().day
#                             dic[key]["hour"] = datetime.datetime.now().hour
#                             dic[key]["minute"] = datetime.datetime.now().minute
#                             dic[key]["seconds"] = datetime.datetime.now().second
#                             with open(self.defloc, 'w') as fp:
#                                 json.dump(dic, fp)
#                             print("Sucessfully inserted")
#                         else:
#                             print("Duplicate key found")
#                             pass


#         #print(dic)
#     def read(self , key):
#         with open(self.defloc, 'r') as data_file:
#             keyss = json.load(data_file)
#         if(key in keyss):
#             print(keyss[key])
#         else:
#             print("Key not found")
    
#     def delete(self , key):
#         with open(self.defloc) as df:
#             data = json.load(df)
#         if(key not in data):
#             print("Key not found. Invalid Delete operation")
#         else:
#             del (data[key])
#             print("Succesfully deleted")
#             with open(self.defloc , 'w') as df:
#                 data = json.dump(data , df)

    
#     def ttl(self):
#         with open(self.defloc) as df:
#             data = json.load(df)
#         for i,j in data.items():
#             if("ttl" in j):
#                 a = datetime.datetime(j["year"] , j["month"] ,j["date"] ,j["hour"] ,j["minute"] ,j["seconds"])
#                 if(datetime.datetime.now() > a + datetime.timedelta(seconds = j["ttl"])):
#                     print("yes, time to delete")
#                 else:
#                     print("no yet")
#                 # print(a , end = " ")
#                 # print(j["ttl"] , end = " ")
#                 # print()


# if __name__ == "__main__":
#     cls = store("C:/Users/PREMRAJ/Desktop/fworks/data_store.json") #define the location of the file (or) keep it as "store(None)"
#     cls.create("kumar" , {"age":20 , "height": 170 , "ttl" : 2})
#     cls.create("raj" , {"age":80 , "height": 10 , "ttl" : 10})
#     cls.create("bheem" , {"age":80 , "height": 10 })
#     cls.create("rajesh" , {"age":71 , "height": 10 })
#     cls.read("raj")
#     cls.delete("kumar")
#     cls.ttl()
