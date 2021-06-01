import json
import requests
import time
import datetime

url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict'

params = {
        "district_id": "",
        "date": ""
    }

header = {  
    "Content-Type": "application/json", 
    "User-Agent": "PostmanRuntime/7.26.8", 
    "Accept": "*/*", 
    "Accept-Encoding": "Accept-Encoding", 
    "Connection": "keep-alive"
    }

MIN_AGE_LIMIT = 18
districts = {}
DISTRICT_FILE = 'district-data.json'
with open(DISTRICT_FILE, 'r') as district:
    districts = json.loads(district.read())
    
def main():
    response = requests.get(url = url, params = params)
    centers = response.json()["centers"]
    for center in centers:
        for session in center["sessions"]:
            if session["min_age_limit"] == MIN_AGE_LIMIT:
                if session["available_capacity_dose1"] > 0 or session["available_capacity_dose2"] > 0:
                    print('Vaccine Available in : ',center["name"], center["address"], center["block_name"], center["pincode"])
                    print('Number of Vaccine Available : ', session["available_capacity_dose1"] + session["available_capacity_dose2"])
    time.sleep(15)

if __name__ == "__main__":
    print("======You will have to provide the script the where you want to search the vaccine district========")
    print("======The script will run forever press clt+c to stop the script from running on your terminal=====")
    print("======The script will update the details after every 10 seconds, please twick the code to change===")
    print("======The script searches only for 18+ by default change the const to change values================")
    params["district_id"] = districts[input("Enter the district : ")]
    params["date"] = input("Enter the date (leave empty if want todays day) (format : DD-MM-YYYY) : ")
    if params["date"] == "":
        params["date"] =  "-".join(str(datetime.datetime.now()).split(' ')[0].split('-')[::-1])
    print("The script is running and will update whenever vaccine is availble, press clt+c to stop the script")
    while True:
        main()
