import os
import json

# Global değişkenler
emtySlot = "emtySlot.json"
membersFileName = "members.json"
tracking = "tracking.json"
taksi = "taksi.json"
books = "kitap.json"


def loadData(file_name, data=[]):
    if os.path.exists(file_name):
        with open(file_name, "r+", encoding="utf-8") as file:
            return json.load(file)
    else:
        with open(file_name, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
            return data


def saveData(file, data):
    try:
        with open(file, "w+", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
            print(f"Veriler başariyla {file} dosyasina kaydedildi.")
    except Exception as e:
        print(
            f"Veriler {file} dosyasina eklenirken kayit sirasinda bir hata olustu.", e)
