from PIL import Image, ImageDraw
from api_parse import send_answer
from solution import create_routes, bag_packing, make_graph
import json


def draw_map(children, snow_a):
    img = Image.new(mode="RGB", size=(10000, 10000), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw.ellipse((-20, -20, 20, 20), fill='red')
    for s in snow_a:
        x = s['x']
        y = s['y']
        r = s['r']
        draw.ellipse((x-r, y-r, x+r, y+r), fill='blue')
        print(s)
    for c in children:
        x = c['x']
        y = c['y']
        draw.rectangle((x-20, y-20, x+20, y+20), fill='green')
        print(c)

    img.show()
    img.save('../maps/map.png')


def draw_routes(routes):
    img = Image.open('../maps/map.png')
    draw = ImageDraw.Draw(img)
    for route in routes:
        start_x = 0
        start_y = 0
        for point in route:
            x = point['x']
            y = point['y']
            draw.line((start_x, start_y, x, y), fill='red', width=5)
            start_x = x
            start_y = y
        draw.line((start_x, start_y, 0, 0), fill='red', width=5)
    img.show()
    img.save('../maps/routes.png')


def get_data():
    data = dict()
    with open('../maps/map.json') as f:
        data = json.load(f)
    return data['gifts'], data['snowAreas'], data['children'] 


def main():
    gifts, snowAreas, children = get_data()
    print('gifts:', gifts)
    print('children:', children)
    print('snowAreas:', snowAreas)
    # make_graph(children)
    # draw_map(children, snowAreas)
    bags = bag_packing(gifts)
    routes = create_routes(children, bags)
    # print(routes)
    # draw_routes([[(c['x'], c['y']) for c in children]])
    # draw_routes(routes)
    send_answer(routes, bags)


if __name__ == '__main__':
    main()
