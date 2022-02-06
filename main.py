import random

english_worlds = {
    'industrial': 'технологичный', 'capital': 'столица', 'cosmopolitan': 'всемирный',
    'overcrowded': 'переполненный', 'historic': 'историчный', 'market': 'магазин',
    'boom town': 'быстро растущий город', 'shanty': 'хижина', 'new': 'новый',
    'rubbish on the street': 'мусор на улице', 'lack of parks/trees': 'отсутствие парков/деревьев',
    'heavy traffic on the roads': 'интенсивное движение на дорогах', 'street hawkers': 'уличные торговцы',
    'stray animals': 'бездомные животные', 'overcrowded public transport': 'переполненный общественный транспорт',
    'smells and noise': 'запахи и шум', 'graffiti': 'графити',
    'beggars': 'нищие', 'dog/bird mess': 'беспорядок с собаками/птицами',
    'cars/motorbikes parked on the pavements': 'автомобили/мотоциклы припаркованные на тратуарах'
}


class PlayGame(object):

    def __init__(self):
        self.b = None
        self.a = None

    def game(self):
        self.a = random.choice(list(english_worlds.values()))
        print(self.a)
        self.b = input()
        for k, v in english_worlds.items():
            if self.b == k:
                if self.a == v:
                    print('Great\n')
                    self.game()
        self.check()

    def check(self):
        for k, v in english_worlds.items():
            if self.a == v:
                print(f'{k}\n')
                self.game()


if __name__ == '__main__':
    obj = PlayGame()
    obj.game()
