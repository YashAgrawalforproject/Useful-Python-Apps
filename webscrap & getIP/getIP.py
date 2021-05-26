import socket
from ip2geotools.databases.noncommercial import DbIpCity
while True:
    url = input("Insert a URL: ")
    IP = socket.gethostbyname(url)

    response = DbIpCity.get(IP, api_key='free')
    print("IP: ", IP)
    print("City: ", response.city)
    print("Region: ", response.region)
    print("Country: ", response.country)
    print("Latitude: ", response.latitude)
    print("Longitude: ", response.longitude)
