import pymongo

client = pymongo.MongoClient("mongodb://root:example@db:27017")

db = client["Kantondb"]
col = db["basel"]

basellist=[{"Bezeichung": "Basel"},{"Bezeichung": "basel"},{"Bezeichung": "Basel-Stadt"},{"Bezeichung": "basel-stadt"}]
print("Drucke die verschiedene Baselstadt Bezeichnungen")
col.insert_many(basellist)
#basel=[]
for doc in col.find():
    
    #basel.append(doc)
    print(doc)

#def flaeche(kosten):
#    print("Wie Gross sollte die Flaeche ihres Haus sein in Quadratmetern")
#    userFlaecheInput=input()
#    print("Sie wollen "+userFlaecheInput+" Quadratmeter Flaeche")
#    print("Die Flaeche des Hauses wuerde "+kosten*userFlaecheInput+" Fr. kosten.")

#print("Willkommen zum Hauskostenrechner")
#print("Bei Hauskostenrechner koennen Sie die Kosten der Haeuser transparent ansehen")
#print("Im System gibt es nur 3 Kantone Basel, Zuerich oder Baselland, wenn Sie keines vom dem nehmen, dann wird es automatisch die Schwiz gewaehlt")
#userKantonInput=input()
#print("Sie haben "+userKantonInput+" gewaehlt")

#if userKantonInput in basel:
 #   flaeche(10000)

#else:
 #    flaeche(6000)

#print("Schade Das Programm ist vorbei ^^)")