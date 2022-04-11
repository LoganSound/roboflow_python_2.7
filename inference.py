import requests
import urllib

# Construct the URL
img_url = "https://i.imgur.com/PEEvqPN.png"
upload_url = "".join([
    "detect.roboflow.com/your-model/42",
    "?api_key=YOUR_KEY",
    "&image=" + urllib.quote_plus(img_url)
])

# POST to the API
r = requests.post(upload_url)

# Output result
print(r.json())
