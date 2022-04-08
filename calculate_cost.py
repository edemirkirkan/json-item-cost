from urllib.request import urlopen
import json

def main():
    # Additional samples can be added to following set for testing purposes
    sample_urls = ['https://prod-storyly-media.s3.eu-west-1.amazonaws.com/test-scenarios/sample_1.json', 
    'https://prod-storyly-media.s3.eu-west-1.amazonaws.com/test-scenarios/sample_2.json', 
    'https://prod-storyly-media.s3.eu-west-1.amazonaws.com/test-scenarios/sample_3.json']

    for sample_number, url in enumerate(sample_urls, 1):
        json = retrieve_json(url)
        name = json['name']
        cost = calculate_cost(json)
        print("Case {}: Cost of item '{}' is {} units.".format(sample_number, name, cost))

def calculate_cost(json):
    item_cost = 0
    for item in json['items']:
        if (is_item_part(item)):
            item_cost += item['price'] * item['count']
        else:
            item_cost += calculate_cost(item)
    item_cost *= json['count']    
    return item_cost
        

def retrieve_json(url):
    json_url = urlopen(url)
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