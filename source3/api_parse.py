import json
import requests

def get_data():
    with open('../maps/s3.json') as f:
        data = json.load(f)
    return data['children'], data['gifts'], data['snowAreas']



def send_answer(moves, gifts):
    headers = {
            'X-API-Key': '6701fb9f-7149-43e5-aff4-19d0a8a2641f',
            }
    url = 'https://datsanta.dats.team/api/round'
    map_id = 'dd6ed651-8ed6-4aeb-bcbc-d8a51c8383cc'
    ans ={'mapID': map_id, 'moves': moves, 'stackOfBags': gifts}
    print(ans)
    r = requests.post(url, json=ans, headers=headers)
    print(r.text)
    r = json.loads(r.text)
    with open('solution_id.txt', 'a') as f:
        f.write(r['roundId'])


def get_map():
    map_id = 'dd6ed651-8ed6-4aeb-bcbc-d8a51c8383cc'
    url = f'https://datsanta.dats.team/json/map/{map_id}.json'
    html = requests.get(url)
    html = html.text
    print(html)
    with open('../maps/s3.json', 'w') as f:
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

