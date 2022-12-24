import json


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
    res = sorted(res, key=lambda x: len(x), reverse=True)
    for c in res:
        print(len(c))
    return res


def create_routes(cords: list, bags: list):
    routes = []
    for bag in bags:
        route = []
        gifts_count = len(bag)
        for _ in range(gifts_count):
            p = cords.pop()
            route.append((p['x'], p['y']))
        routes.append(route)
    return routes


def euclidean_distance(p, q):
    return ((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2) ** 1/2


def _main():
    cords = [{'x': 1, 'y': 1}, {'x': 2, 'y': 2}, {'x': 3, 'y': 3}]
    bags = [[1],[2,3]]
    routes = create_routes(cords, bags)
    print(routes)


if __name__ == '__main__':
    _main()


