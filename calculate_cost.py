from urllib.request import urlopen
import json

def main():
 

def retrieve_json(URL):
    json_url = urlopen(URL)
    data = json.loads(json_url.read())
    return data

if __name__ == "__main__":
    main()