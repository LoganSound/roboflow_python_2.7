import requests
import urllib

# Construct the URL
img_url = "https://i.imgur.com/PEEvqPN.png"
upload_url = "".join([
    "https://api.roboflow.com/dataset/your-dataset/upload",
    "?api_key=YOUR_API_KEY",
    "&name=201-956-1246.png",
    "&split=train",
    "&image=" + urllib.quote_plus(img_url)
])

# POST to the API
r = requests.post(upload_url)

# Output result
print(r.json())
