from paralleldots.config import  set_api_key,get_api_key
import requests
import json

def get_keywords(text,api_key):
    print text
    print type(text)
    set_api_key("DRmg2bz8D85xI8Tm0pSCYOITFGx1EyirLk1nhhGduJs")
    if not api_key == None:
        if type(text) != str:
            return "Input must be a string."
        elif text == "":
            return "Input string cannot be empty."

        url = 'http://apis.paralleldots.com/keywords'
        response = requests.post(url, params={"apikey": api_key, "q": text})
        if response.status_code != 200:
            return ""
        response = {"keywords": json.loads(response.content)}
        return response['keywords']
    else:
        return "API key does not exist"