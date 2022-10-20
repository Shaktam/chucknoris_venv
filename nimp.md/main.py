import requests
import json
import boto3

s3 = boto3.resource("s3")

def get_joke():
    url="https://api.chucknorris.io/jokes/random"  
    response=requests.get(url)
    data = response.json()

    joke = data["value"]
    rating = int(input("Please give us your Rating: "))
    joke_data_to_save = {
        "id": data["id"],
        "joke": data["value"],
        "rating": rating
    }
    joke_data_as_string = json.dumps(joke_data_to_save) 
    if rating > 4:
        with open("joke.json", 'w') as f:
            f.write(joke_data_as_string) 
    print(joke_data_as_string)      

    get_joke()
    # aws s3
    s3.meta.client.upload_file('joke.json', 'chucks3bucket', 'joke.json')




