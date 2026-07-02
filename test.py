import requests

API_KEY = "32f8ac1a21f52f177d724040cdf7a57d"

url = f"https://api.themoviedb.org/3/movie/7450?api_key=32f8ac1a21f52f177d724040cdf7a57d"

response = requests.get(url)

print(response.status_code)
print(response.json())