
from chucknoris_api import get_newjoke
from s3_bucket import upload_joke_s3

joke_data_to_save= get_newjoke()
upload_joke_s3(joke_data_to_save)


"""joke_data_as_string = json.dumps(joke_data_to_save) 
        if rating > 4:
        with open("joke.json", 'w') as f:
            f.write(joke_data_as_string) 
    print(joke_data_as_string)      

    get_joke()
    # aws s3
    s3.meta.client.upload_file('joke.json', 'chucks3bucket', 'joke.json')
"""



