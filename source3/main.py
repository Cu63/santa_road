from PIL import Image, ImageDraw
from api_parse import send_answer, get_data
from solution import create_routes, make_graph
import json
from gifts_parse import (get_gifts_stats, get_children_stats, 
                        give_presents, create_answer)



def draw_map(children, snow_a):
    img = Image.new(mode="RGB", size=(10000, 10000), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw.ellipse((-20, -20, 20, 20), fill='red')
    for s in snow_a:
        x = s['x']
        y = s['y']
        r = s['r']
        draw.ellipse((x-r, y-r, x+r, y+r), fill='blue')
    for c in children:
        x = c['x']
        y = c['y']
        draw.rectangle((x-20, y-20, x+20, y+20), fill='green')

    img.show()
    img.save('../maps/map.png')


def draw_routes(routes):
    img = Image.open('../maps/map.png')
    draw = ImageDraw.Draw(img)
    start_x = 0
    start_y = 0
    for point in routes:
        x = point['x']
        y = point['y']
        draw.line((start_x, start_y, x, y), fill='red', width=5)
        start_x = x
        start_y = y
    img.show()
    img.save('../maps/routes.png')


def main():
    children, gifts, snowAreas = get_data()
    make_graph(children)
    # draw_map(children, snowAreas)
    gifts_s = get_gifts_stats(gifts)
    children_s = get_children_stats(children)
    presentingGifts = create_answer(children_s, gifts_s)
    # bags = bag_packing(gifts)
    routes, stackOfBags = create_routes(children, presentingGifts, gifts)
    draw_routes(routes)
    send_answer(routes, stackOfBags)


if __name__ == '__main__':
    main()
