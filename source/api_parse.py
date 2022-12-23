import requests


def get_map():
    map_id = 'faf7ef78-41b3-4a36-8423-688a61929c08'
    url = f'https://datsanta.dats.team/json/map/{map_id}.json'
    html = requests.get(url)
    html = html.text
    print(html)
    with open('../maps/map.json', 'w') as f:
        f.write(html)
    return html


def _main():
    map_ = get_map()
    print(map_)



if __name__ == '__main__':
    _main()
