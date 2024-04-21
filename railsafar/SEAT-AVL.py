# import http.client

# conn = http.client.HTTPSConnection("irctc1.p.rapidapi.com")

# headers = {
#     'X-RapidAPI-Key': "6e5848ff26msh078e0bbcc9c2691p18c25djsn0ae73263cbd8",
#     'X-RapidAPI-Host': "irctc1.p.rapidapi.com"
# }

# conn.request("GET", "/api/v1/searchStation?query=BJU", headers=headers)

# res = conn.getresponse()
# data = res.read()



# print(data.decode("utf-8"))




import http.client

conn = http.client.HTTPSConnection("irctc1.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "254aacaae3msh7efff0ed3b899bap13187cjsne9e1968c4df6",
    'X-RapidAPI-Host': "irctc1.p.rapidapi.com"
}

conn.request("GET", "/api/v1/checkSeatAvailability?classType=3A&fromStationCode=BPL&quota=GN&toStationCode=NZM&trainNo=12156&date=2024-04-13", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))


