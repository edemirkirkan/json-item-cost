from urllib.request import urlopen
from json import loads


def main():
    # additional samples can be added to following set for testing purposes
    sample_urls = ['https://prod-storyly-media.s3.eu-west-1.amazonaws.com/test-scenarios/sample_1.json',
                   'https://prod-storyly-media.s3.eu-west-1.amazonaws.com/test-scenarios/sample_2.json',
                   'https://prod-storyly-media.s3.eu-west-1.amazonaws.com/test-scenarios/sample_3.json']

    run(sample_urls)


def run(sample_urls):
    for sample_number, url in enumerate(sample_urls, 1):
        json = retrieve_json(url)
        name = json['name']
        cost = evaluate_cost(json)
        print("Case {}: Cost of item '{}' is {} units.".format(sample_number, name, cost))


def retrieve_json(url):
    json_url = urlopen(url)
    json = loads(json_url.read())
    return json


def evaluate_cost(json):
    item_cost = 0
    for item in json['items']:
        if is_part(item):
            item_cost += item['price'] * item['count']
        else:
            item_cost += evaluate_cost(item)
    item_cost *= json['count']
    return item_cost


def is_part(item):
    try:
        item['price']
    except KeyError:
        return False
    return True


if __name__ == "__main__":
    main()
