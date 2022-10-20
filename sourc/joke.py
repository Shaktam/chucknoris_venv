"""
from chucknoris_api import get_newjoke
from s3_bucket import upload_joke_s3

joke_data_to_save= get_newjoke()
upload_joke_s3(joke_data_to_save)"""

from sourc.chucknoris_api import get_newjoke
from s3_bucket import upload_joke_s3

while True:
    joke_data_to_save= get_newjoke()
    print(joke_data_to_save["joke"])
    rating = int(input("Did you like this joke? \n Scale 1-5: "))

    if (rating >3):
        print("GREAT! I'll store this joke")
        upload_joke_s3(joke_data_to_save)
    else:
        print("BAD! I'll change this")


    new_joke = input("new joke? (yes/no")
    if new_joke != "yes":   
        no_new_joke = input("Are you sure ? yes \n")
        if no_new_joke == "yes":
            break






"""joke_data_as_string = json.dumps(joke_data_to_save) 
        if rating > 4:
        with open("joke.json", 'w') as f:
            f.write(joke_data_as_string) 
    print(joke_data_as_string)      

    get_joke()
    # aws s3
    s3.meta.client.upload_file('joke.json', 'chucks3bucket', 'joke.json')
"""



