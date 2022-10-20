import requests

def get_newjoke():
    url= "https://api.chucknorris.io/jokes/random"  
    response=requests.get(url)

    data = response.json()

    return {
        "id": data["id"],
        "joke": data["value"]
    }