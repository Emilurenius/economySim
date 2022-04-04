import sys

comodities = {
    'coal': {
        'neededEquipment': ['excavatorx0']
    },
    'excavator': {
        'neededEquipment': ['coal', 'iron'],
    },
    'iron': {
        'neededEquipment': ['excavatorx0']
    }
}

class tradeNode:
    def __init__(self, name, type, state, produces, _comodities):
        self.name = name
        self.type = type
        self.state = state
        self.produces = produces
        self.comodities = _comodities

    def produce(self):
        print(f'{self.name} Producing {self.produces}')
        self.comodities[comodities[self.produces]['neededEquipment'][0]] -= 1
        print

tradeNodes = [
    tradeNode('Coal Mine', 'ind', 'nom', ['coal'], {'coal': 40, 'excavator': 3}),
    tradeNode('Iron Mine', 'ind', 'nom', ['iron'], {'iron': 40, 'excavator': 3}),
    tradeNode('Excavator factory', 'ind', 'nom', ['excavator'], {'coal': 40, 'excavator': 10}),
]


def main():
    for x in tradeNodes:
        x.produce()

if __name__ == '__main__':
    main()