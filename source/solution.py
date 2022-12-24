def bag_packing():
    pass


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


def _main():
    cords = [{'x': 1, 'y': 1}, {'x': 2, 'y': 2}, {'x': 3, 'y': 3}]
    bags = [[1],[2,3]]
    routes = create_routes(cords, bags)
    print(routes)


if __name__ == '__main__':
    _main()
