from api_parse import send_answer, get_result
import copy
import json


def get_dict():
    with open('../maps/gifts.json') as f:
        data = json.load(f)
    return data['children'], data['gifts']


def get_gifts_stats(gifts):
    stat = {}
    for gift in gifts:
        if gift['type'] not in stat:
            stat[gift['type']] = []
        stat[gift['type']].append({'id': gift['id'],
                                   'price': gift['price']})
    for s in stat:
        stat[s] = sorted(stat[s], key=lambda x: x['price'])
        print(f'{s}: {stat[s]}')
    return stat


def get_children_stats(children):
    stat = {}
    for child in children:
        if child['age'] not in stat:
            stat[child['age']] = {'male': [], 'female': []}
        stat[child['age']][child['gender']].append(child['id'])
    for s in sorted(stat):
        print(f'{s}: {stat[s]}')
    return stat


def give_presents(start, end, cat_male, cat_female, children_, gifts_):
    presentingGifts = []
    total_price = 0
    for i in range(start, end):
        print(len(presentingGifts))
        for id_ in children_[i]['male']:
            present = gifts_[cat_male].pop(0)
            presentingGifts.append({
                'giftID': present['id'],
                'childID': id_})
            total_price += present['price']
        for id_ in children_[i]['female']:
            present = gifts_[cat_female].pop(0)
            presentingGifts.append({
                'giftID': present['id'],
                'childID': id_})
            total_price += present['price']
    return presentingGifts, total_price



def create_answer(children, gifts):
    total_price = 0
    children_ = copy.deepcopy(children)
    gifts_ = copy.deepcopy(gifts)
    presentingGifts = []
    pairs = [
            (0, 1, 'sweets', 'sweets'),
            (1, 2, 'sweets', 'sweets'),
            (2, 3, 'sweets', 'sweets'),
            (3, 4, 'sweets', 'sweets'),
            (4, 5, 'books', 'books'),
            (5, 6, 'books', 'books'),
            (6, 7, 'books', 'books'),
            (7, 8, 'books', 'books'),
            (8, 9, 'pet', 'pet'),
            (9, 10, 'pet', 'pet'),
            (10, 11, 'pet', 'pet'),
    ]
    for p in pairs:
        group_gifts, price = give_presents(*p, children_, gifts_)
        total_price += price
        presentingGifts.extend(group_gifts)

    print(presentingGifts)
    print(total_price)
    return presentingGifts


def main():
    children, gifts = get_dict()
    children = get_children_stats(children)
    gifts = get_gifts_stats(gifts)
    presentingGifts = create_answer(children, gifts)
    # send_answer(presentingGifts)
    # get_result()


if __name__ == '__main__':
    main()
