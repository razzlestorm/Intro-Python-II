
class Item:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

    def __str__(self):
        ench_string = 'You can feel an aura of hidden magic emanating from it.'
        if 'enchanted' in self.name:
            return f'{self.desc} {ench_string}'
        else:
            return self.desc
