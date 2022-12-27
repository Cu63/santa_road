import json


def get_present_id(cord, gifts):
    for g in gifts:
        if g['childID'] == cord:
            return g['giftID']


def get_w_v(id_, gifts):
    w = 0
    v = 0
    for g in gifts:
        if g['id'] == id_:
            return g['weight'], g['volume']


def create_routes(cords: list, bags: list, gifts):
    print('create routes')
    cords = [{'x': 0, 'y': 0}] + cords
    graph = make_graph(cords)
    routes = []
    presents = []
    visited = set() 
    cord = 0
    w = 0
    v = 0
    bag = []
    route = []
    cur = 0
    sum = 0
    while len(visited) < 1000:
        best = -1
        for i in range(1, len(graph)):
            if i in visited or i == cur:
                continue
            if best == -1 or graph[cur][best] > graph[cur][i]:
                best = i
        cur = best
        cord = (cords[best]['x'], cords[best]['y'])
        giftID = get_present_id(cord, bags)
        present_w, present_v = get_w_v(giftID, gifts)
        if w + present_w >= 200 or v + present_v >= 100:
            presents.append(bag.copy()[::-1])
            sum += len(bag)
            bag.clear()
            route.append({'x': 0,'y': 0})
            w = 0
            v = 0
            cur = 0
        else:
            w += present_w
            v += present_v
            bag.append(giftID)
            route.append({'x': cord[0],'y': cord[1]})
            visited.add(best)

    presents.append(bag[::-1])
    presents = presents[::-1]
    sum += len(bag)
    print(sum)
    return route, presents


def euclidean_distance(p, q):
    return ((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2) ** 1/2


def make_graph(cords: list):
    graph = []
    print(cords)
    for i in range(len(cords)):
        row = [] * len(cords)
        x_1 = cords[i]['x']
        y_1 = cords[i]['y']
        for j in range(len(cords)):
            x_2 = cords[j]['x']
            y_2 = cords[j]['y']
            row.append(euclidean_distance((x_1, y_1), (x_2, y_2)))
        graph.append(row)
    '''
    with open('graph', 'w') as f:
        for r in graph:
            print(*r, file=f)
    '''
    return graph


def _main():
    cords = [{'x': 1, 'y': 1}, {'x': 2, 'y': 2}, {'x': 3, 'y': 3}]
    bags = [[1],[2,3]]
    routes = create_routes(cords, bags)
    print(routes)


if __name__ == '__main__':
    _main()


