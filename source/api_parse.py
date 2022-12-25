import json
import requests


def send_answer(cords: list, bags: list):
    headers = {
            'X-API-Key': '6701fb9f-7149-43e5-aff4-19d0a8a2641f',
            }
    url = 'https://datsanta.dats.team/api/round'
    map_id = 'faf7ef78-41b3-4a36-8423-688a61929c08'
    moves = []
    for way in cords:
        for point in way:
            moves.append(point)

    bags = bags[::-1]
    ans ={'mapID': map_id, 'moves': moves, 'stackOfBags': bags}
    print(ans)
    r = requests.post(url, json=ans, headers=headers)
    print(r.text)
    r = json.loads(r.text)
    with open('solution_id.txt', 'a') as f:
        f.write(r['roundID'])



def get_map():
    map_id = 'faf7ef78-41b3-4a36-8423-688a61929c08'
    url = f'https://datsanta.dats.team/json/map/{map_id}.json'
    html = requests.get(url)
    html = html.text
    print(html)
    with open('../maps/map.json', 'w') as f:
        f.write(html)
    return html


def get_result():
    headers = {
            'X-API-Key': '6701fb9f-7149-43e5-aff4-19d0a8a2641f',
            }
    with open('solution_id.txt') as f:
        id_ = f.readlines()
    print(id_[-1][:-1])
    url = f'https://datsanta.dats.team/api/round/{id_[-1][:-1]}'
    ans = requests.get(url, headers=headers)
    print(ans.text)


def _main():
    # send_answer(routes, [])
    get_result()


if __name__ == '__main__':
    _main()
