from urllib.request import urlopen
import json

def main():
 
   


def calculate_cost(json):
    item_cost = 0
    for item in json['items']:
        if (is_item_part(item)):
            item_cost += item['price'] * item['count']
        else:
            item_cost += calculate_cost(item)
    item_cost *= json['count']    
    return item_cost
        

def retrieve_json(URL):
    json_url = urlopen(URL)
    data = json.loads(json_url.read())
    return data

def is_item_part(item):
    try:
        item['price']
    except KeyError:
        return False
    return True

if __name__ == "__main__":
    main()