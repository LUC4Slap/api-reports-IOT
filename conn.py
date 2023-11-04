from pymongo import MongoClient
import os
from dotenv import load_dotenv
load_dotenv()

class GetReposts:
    def __init__(self):
        self.cliente = MongoClient("mongodb://localhost:27017/radar-pt") # PARA RODAR NO LOCALHOST
        # self.password = os.getenv("PASSWORD_DB")
        # SE FOR RODAR NO LOCAL COMENTAR A LINHA DE BAIXO
        # self.cliente = MongoClient(f"mongodb+srv://lucasalmeida:{self.password}@radar-pt.3rljncc.mongodb.net/")
        self.db = self.cliente["radar-pt"]
        self.collection = self.db.reports
        self.results = None
        self.results_array = []

    def getReportDB(self):
        # query
        pipeline = [
            {
                "$sort": {
                    "date_report": -1
                }
            },
            {
                "$group": {
                    "_id": "$imei",
                    "latest_record": {
                        "$first": "$$ROOT"
                    }
                }
            },
            {
                "$replaceRoot": {
                    "newRoot": "$latest_record"
                }
            }
        ]

        try:
            self.results = list(self.collection.aggregate(pipeline))
        except Exception as error:
            print("erro para inserir")
            print(error)

    def returnDB(self):
      self.getReportDB()
      self.results_array = []
      for doc in self.results:
          self.results_array.append(doc)
      return self.results_array