import json
from api_parse import send_answer
from PIL import Image, ImageDraw


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
    img.save('1.png')


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
    draw_map(children, snowAreas)
    send_answer()


if __name__ == '__main__':
    main()
