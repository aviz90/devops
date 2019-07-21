import urllib.request,json

# # Opening a web request
# url = urllib.request.urlopen("https://free.currconv.com/api/v7/convert?q=USD_ILS&compact=n&apiKey=632be25bf39e6e73f541")
# # Decoding response to str
# data = json.loads(url.read().decode()) # Decoding a web request
#
# # Parsing results
# results = data['results']
# USD_ILS = results['USD_ILS']
# val = USD_ILS['val']

url = urllib.request.urlopen("https://maps.googleapis.com/maps/api/place/textsearch/json?query=restaurants+in+Jerusalem&key=AIzaSyD2she6rJGiE9vDeJnEkl6hbwq6KheCXgE")
# Decoding response to str
data = json.loads(url.read().decode()) # Decoding a web request

# Parsing results
geometry = data['geometry']
location = geometry['location']
lat = location['lat']
lng = location['lng']
print(lat, lng)


# print("Welcome to currency converter")
# amount_to_convert = input("Please enter an amount of Shekeles to convert:")
# convert_result = int(amount_to_convert) * val
# print(convert_result)
# print("Thanks for using our currency converter.")

