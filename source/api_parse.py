import requests
import json


def send_answer(cords: list, bags: list):
    map_id = 'faf7ef78-41b3-4a36-8423-688a61929c08'
    cords = [[(1, 2), (1, 3), (1, 4)]]
    moves = []
    ans ={'moves': moves}
    for way in cords:
        for point in way:
            moves.append({"x": point[0], "y": point[1]})
        moves.append({"x": 0, "y": 0})
    ans = json.dumps(ans)
    print(ans)



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
    # map_ = get_map()
    send_answer([], [])


if __name__ == '__main__':
    _main()
