import json
import requests

if __name__ == "__main__":
    
    song = input("Give me an album to search for:")

    url = "https://spotify23.p.rapidapi.com/search"

    querystring = {"type": "album", "q": song}  # Replace "Born in the U.S.A." with the name of the album you want to search for

    headers = {
        "X-RapidAPI-Key": "e354a39aecmsh2c967112f19af0dp10dd88jsn9435c59da7e1",
        "X-RapidAPI-Host": "spotify23.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    print(response.json())

    
