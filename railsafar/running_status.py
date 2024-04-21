import http.client

conn = http.client.HTTPSConnection("irctc1.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "254aacaae3msh7efff0ed3b899bap13187cjsne9e1968c4df6",
    'X-RapidAPI-Host': "irctc1.p.rapidapi.com"
}

conn.request("GET", "/api/v1/liveTrainStatus?trainNo=19038&startDay=1", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))