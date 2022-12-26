import json
import requests


def send_answer(gifts: list):
    headers = {
            'X-API-Key': '6701fb9f-7149-43e5-aff4-19d0a8a2641f',
            }
    url = 'https://datsanta.dats.team/api/round2'
    map_id = 'a8e01288-28f8-45ee-9db4-f74fc4ff02c8'
    ans ={'mapID': map_id, 'presentingGifts': gifts}
    print(ans)
    r = requests.post(url, json=ans, headers=headers)
    print(r.text)
    r = json.loads(r.text)
    with open('solution_id.txt', 'a') as f:
        f.write(r['roundId'])



def get_map():
    map_id = 'a8e01288-28f8-45ee-9db4-f74fc4ff02c8'
    url = f'https://datsanta.dats.team/json/map/{map_id}.json'
    html = requests.get(url)
    html = html.text
    print(html)
    with open('../maps/gifts.json', 'w') as f:
        f.write(html)
    return html


def get_result():
    headers = {
            'X-API-Key': '6701fb9f-7149-43e5-aff4-19d0a8a2641f',
            }
    with open('solution_id.txt') as f:
        id_ = f.readlines()
    print(id_[-1][:-1])
    url = f'https://datsanta.dats.team/api/round2/{id_[-1][:-1]}'
    ans = requests.get(url, headers=headers)
    print(ans.text)


def _main():
    # map_ = get_map()
    pass


if __name__ == '__main__':
    _main()
