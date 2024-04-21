# # import http.client
# # import json

# # conn = http.client.HTTPSConnection("irctc1.p.rapidapi.com")

# # headers = {
# #     'X-RapidAPI-Key': "254aacaae3msh7efff0ed3b899bap13187cjsne9e1968c4df6",
# #     'X-RapidAPI-Host': "irctc1.p.rapidapi.com"
# # }

# # conn.request("GET", "/api/v1/getTrainSchedule?trainNo=20171", headers=headers)

# # res = conn.getresponse()
# # data = res.read()

# # # Parse JSON data
# # schedule = json.loads(data.decode("utf-8"))

# # # Print train information
# # print("Train Information:")
# # print("Train Name:", schedule["data"]["trainName"])
# # print("Train Number:", schedule["data"]["trainNumber"])
# # print("Train Type:", schedule["data"]["trainType"])
# # print("Operational Days:", ", ".join([day.capitalize() for day, value in schedule["data"]["runDays"].items() if value]))
# # print("\nAvailable Classes:")
# # for class_info in schedule["data"]["class"]:
# #     print(f"{class_info['name']}: {class_info['value']}")
# # print("\nAvailable Quotas:")
# # for quota_info in schedule["data"]["quota"]:
# #     print(f"{quota_info['name']}: {quota_info['value']}")
# # print("\nRoute Information:")

# # # Print schedule
# # for station in schedule["data"]["route"]:
# #     print("------------------------------------")
# #     print("Station Name:", station["station_name"])
# #     print("Station Code:", station["station_code"])
# #     print("State:", station["state_name"])
# #     print("Arrival Time:", station["today_sta"] if station["stop"] else "Not Scheduled")
# #     print("Departure Time:", station["std_min"] if station["stop"] else "Not Scheduled")
# #     print("Distance from Source:", station["distance_from_source"])
# #     print("------------------------------------")
# 
# import http.client
# import json
# conn = http.client.HTTPSConnection("indian-railway-irctc.p.rapidapi.com")

# headers = {
#     'x-rapid-api': "rapid-api-database",
#     'X-RapidAPI-Key': "8e7e93441amsh5f1bdf079a95a58p195ecdjsn102b315779d8",
#     'X-RapidAPI-Host': "indian-railway-irctc.p.rapidapi.com"
# }

# conn.request("GET", "/getTrainLiveStatusById?id=2519&date=Mon%2C%2031st%20Dec", headers=headers)
import json
import http.client

# Establish connection to the API
conn = http.client.HTTPSConnection("indian-railway-irctc.p.rapidapi.com")

# Set request headers
headers = {
    'x-rapid-api': "rapid-api-database",
    'X-RapidAPI-Key': "8e7e93441amsh5f1bdf079a95a58p195ecdjsn102b315779d8",
    'X-RapidAPI-Host': "indian-railway-irctc.p.rapidapi.com"
}

# Make a request to get the train ID
conn.request("GET", "/getTrainId?trainno=12156", headers=headers)

# Get the response
res = conn.getresponse()
data = res.read()

# Parse JSON response to extract train ID
response_data = json.loads(data.decode("utf-8"))

train_id=response_data[0]['id']
 

url = f"/getTrainLiveStatusById?id={train_id}&date=16april".replace(" ", "%20")  
conn.request("GET", url, headers=headers)
res = conn.getresponse()
data = res.read()

# Decode JSON response
response_data = json.loads(data.decode("utf-8"))

# Print the train details
train_details = response_data.get('details', {})
if train_details:
    print("Train Details:")
    print("Train ID:", train_details.get('id', ""))
    print("Train Number:", train_details.get('number', ""))
    print("Train Name:", train_details.get('name', ""))
    print("Source:", train_details.get('source', ""))
    print("Destination:", train_details.get('destination', ""))
    print("Type:", train_details.get('type', ""))
    print("Days:", train_details.get('daysStr', ""))
    print("\n")

# Print the train status
train_status = response_data.get('train', {})
if train_status:
    print("Train Status:")
    print("Scheduled Date:", train_status.get('trs_date', ""))
    print("Departed:", "Yes" if train_status.get('departed') == "1" else "No")
    print("Last Updated:", train_status.get('lastUpdated', ""))
    print("Source Name:", train_status.get('source_name', ""))
    print("Source Code:", train_status.get('source_code', ""))
    print("Late (mins):", train_status.get('lateMins', ""))
    print("\n")

# Print the station-wise details
stations = response_data.get('stations', [])
if stations:
    print("Station-wise Details:")
    for station in stations:
        print("Station Name:", station.get('source_name', ""))
        print("Arrival Time:", station.get('arrival_time', ""))
        print("Departure Time:", station.get('departure_time', ""))
        print("Actual Arrival Time:", station.get('actual_arrival_time', ""))
        print("Actual Departure Time:", station.get('actual_departure_time', ""))
        print("Day:", station.get('day', ""))
        print("Distance:", station.get('distance', ""))
        print("Delay Arrival:", station.get('delay_arrival', ""))
        print("Delay Departure:", station.get('delay_departure', ""))
        print("\n")
else:
    print("No station-wise details available.")
