import speedtest
import requests
import json
import pyrebase
import datetime
from . vars import api, auth, db, bucket, username, password


config = {
  "apiKey": api,
  "authDomain": auth,
  "databaseURL": db,
  "storageBucket": bucket,
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()
user = auth.sign_in_with_email_and_password(username, password)

servers = [21325]

def initSpeedtest():
    s = speedtest.Speedtest()
    s.get_servers()
    s.get_best_server()
    s.download()
    s.upload()
    res = s.results.dict()
    data = {
            "status": "success",
            "upload": int(res["upload"])/1000000,
            "download": int(res["download"])/1000000,
            "ping": res["ping"],
            "isp": res["client"]["isp"],
            "ip": res["client"]["ip"],
            "timestamp": str(datetime.datetime.now())
        }
    db.child("results").push(data, user['idToken'])

    return

def test():
    attempts = 10
    for i in range(attempts):
        print("Attempt number: " + str(i))
        try:


            initSpeedtest()

            return "OK"

        except Exception as e:
            if i < attempts - 1:
                pass

                return "error"
            else:
                raise

        break

test()



# /home/huis/jobs/speedtest/test/script.py

# /home/huis/jobs/speedtest/venv/bin

# */0 * * * * /home/huis/jobs/speedtest/venv/bin/python3 /home/huis/jobs/speedtest/test/script.py