import random

def direction(tut):
    # import random
    # direction = random.choice(['left', 'right'])
    angle = random.choice([0, 90, 180, 270])
    return tut.left(angle)
    # if direction == 'left':
    #     return tut.left(angle)
    # else:
    #     return tut.right(angle)
    
def line_len(tut):
    # import random
    leng = random.choice([10, 20, 30])
    return tut.forward(leng)

def colour():
    # import random
    # colours = ['navy', 'black', 'dark slate gray', 'saddle brown', 'seagreen', 'seashell', 'indigo']
    # colours = [random.randint(0, 255) for i in range(3)]
    colours = tuple(random.randint(0, 255) for i in range(3))
    # return random.choice(colours)
    return colours

# def circle():



