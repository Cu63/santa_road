import json

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


if __name__ == '__main__':
    main()
