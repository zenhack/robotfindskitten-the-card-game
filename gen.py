# -*- coding: utf-8 -*-
import jinja2
import random

kitten = u'😸'
spade = u'♠'
club = u'♣'
heart = u'♥'
daimond = u'♦'

suits = [
    spade,
    club,
    heart,
    daimond,
]

colors = [
    'blue',
    'red',
    'green',
    'darkcyan',
    'purple',
    'brown',
    'darkgray',
    'darkorange',
    'yellowgreen',
]

phrases = [
    '''A discredited cosmology, relic of a bygone era.''',
    '''It's a big block of ice. Something seems to be frozen inside it.''',
    '''It's an Internet chain letter about sodium laureth sulfate.''',
    '''A smoking branding iron shaped like a 24-pin connector.''',
    '''It's a U.S. president.''',
    '''Just an autographed copy of the Kama Sutra.''',
    '''It is a cloud shaped like an ox.''',
    '''Conan O'Brian, sans jawbone.''',
    '''This is a large brown bear. Oddly enough, it's currently peeing in the woods.''',
    '''A copy of the Weekly World News. Watch out for the chambered nautilus!''',
    '''Roger Avery, persona un famoso de los Estados Unidos.''',
    '''It's the amazing self-referential thing that's not kitten.''',
    '''It's a solitary vacuum tube.''',
    '''A coupon for one free steak-fish at your local family diner.''',
    '''A digital clock. It's stuck at 2:17 PM.''',
    '''It's the local draft board.''',
    '''It's a business plan for a new startup, kitten.net.''',
    '''It's the proverbial wet blanket.''',
    '''Robot should not be touching that.''',
    '''An eminently forgettable zahir.''',
    '''It's an old Duke Ellington record.''',
    '''A coupon for one free steak-fish at your local family diner.''',
    '''It's the handheld robotfindskitten game, by Tiger.''',
    '''The swampy ground around you seems to stink with disease.''',
    '''Three half-pennies and a wooden nickel.''',
    '''It's an altar to the horse god.''',
    '''This copy of "Steal This Book" has been stolen from a bookstore.''',
    '''It's a squad of Keystone Kops.''',
    '''Another rabbit? That's three today!''',
    '''Just some stuff.''',
    '''Just a broken hard drive containg the archives of Nerth Pork.''',
    '''It's some compromising photos of Babar the Elephant.''',
    '''It's "Chicken Soup for the Kitten-seeking Soulless Robot."''',
    '''The Digital Millennium Copyright Act of 1998.''',
    '''It's a charcoal briquette, smoking away.''',
    '''A toenail? What good is a toenail?''',
    '''Someone has written "ad aerarium" on the ground here.''',
    '''Grind 'em up, spit 'em out, they're twigs.''',
    '''Hey, look, it's war. What is it good for? Absolutely nothing. Say it again.''',
    '''Ah, the uniform of a Revolutionary-era minuteman.''',
    '''A knight who says "Either I am an insane knave, or you will find kitten.".''',
    '''It's the phrase "and her", written in ancient Greek.''',
    '''A book: Feng Shui, Zen: the art of randomly arranging items that are not kitten.''',
    '''A kitten source (to match the kitten sink).''',
]

card_numbers = list('A23456789') + ['10'] + list('JQK')

characters = \
        "abcdefghijklmnopqrstuvwxyz" + \
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ" + \
        "0123456789" + \
        "(){}[]=+-_.,<>?/`~!@$%^&*;:'\"\\"

with open('templates/card.svg') as f:
    card_template = jinja2.Template(f.read())
with open('templates/page.svg') as f:
    page_template = jinja2.Template(f.read())

def generate_cards():
    for suit, color in zip(suits, colors[:len(suits)]):
        yield card_template.render(
            char=kitten,
            color=color,
            suit=suit,
            number='A',
            text='You found kitten! Way to go, robot.',
            kitten=True,
        )
        yield card_template.render(
            char='#',
            color=color,
            suit=suit,
            number='2',
            text='robot',
            kitten=False,
        )
    _phrases = list(phrases)
    random.shuffle(_phrases)
    for suit in suits:
        for number in card_numbers[2:]:
            yield card_template.render(
                # Some of the charcters, e.g. '&', need to be escaped -- we may
                # as well just do all of them:
                char='&#%d;' % ord(random.choice(characters)),
                color=random.choice(colors),
                suit=suit,
                number=number,
                text=_phrases.pop(),
                kitten=False,
            )

i = 0
for card in generate_cards():
    with open('cards/%d.svg' % i, 'w') as f:
        f.write(card.encode('utf-8'))
    i += 1

CARDS_PER_PAGE = 8
cardnums = range(i)
i = 0
while len(cardnums) >= CARDS_PER_PAGE:
    page = page_template.render(cards=cardnums[:CARDS_PER_PAGE])
    with open('pages/%d.svg' % i, 'w') as f:
        f.write(page.encode('utf-8'))
    i += 1
    cardnums = cardnums[CARDS_PER_PAGE:]
if cardnums != []:
    while len(cardnums) < CARDS_PER_PAGE:
        cardnums.append('../blank-card')
    page = page_template.render(cards=cardnums)
    with open('pages/%d.svg' % i, 'w') as f:
        f.write(page.encode('utf-8'))
