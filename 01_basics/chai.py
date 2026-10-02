# from hello_chai import chai
# chai("Lemon Tea")
# list =[{'name':"Archit",'Lname':"Pathak"}]
# print({list['name']})
videos = [{'name':'Archit','lname':'Pathak'}]
for index ,video in enumerate(videos,start=1):
    print(f"{index}.{video['name']},Duration{video['lname']}")