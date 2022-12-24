import json

def get_data():
    with open('../maps/map.json') as f:
        data = json.load(f)
    return data['gifts']


def bag_packing(gifts: list) -> list[list]:
    res = list()
    bag = list()
    bag_weight = 0
    bag_volume = 0
    for d in gifts:
        if bag_weight + d['weight'] > 200 or bag_volume + d['volume'] > 100:
            res.append(bag.copy())
            print(bag_weight, bag_volume)
            bag.clear()
            bag_weight = d['weight']
            bag_volume = d['volume']
            bag.append(d['id'])
        else:
            bag_weight += d['weight']
            bag_volume += d['volume']
            bag.append(d['id'])

    res.append(bag)
    return res

print(bag_packing(get_data()))