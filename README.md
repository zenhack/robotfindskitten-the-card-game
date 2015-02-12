# robotfindskitten: the card game.

I recently participated in a very belated DIY Secret Santa with some 
friends. I made a card-game variant of [robotfindskitten][1] for @xxv.  
Merry Christmas, Steve.

This repository contains the scripts I used in generating the cards.  
It's not great code, and I'm not going to bother cleaning it up anytime 
soon, but here it is. The scripts require python and the jijna2 
templating library.

* `gen.py` will randomly generate a deck of cards, and put the face-up 
  side of each in `cards/` as it's own svg. It will also build build a
  set of svgs suitable for printing on letter paper, with eight cards 
  per sheet. These will be placed in `pages/`
* `box.svg` Contains an outline of the box -- print this out, cut along 
  the line, and fold it up to form a box for the deck.
* `cards-final/` contains the set of cards (contents of the `cards/` 
  directory), for the deck I actually printed off and made.
* `backs.svg` is a sheet containing eight card backings. This should be 
  printed on the back of each of the sheets of cards.
* `templates/` contains jinja2 templates used by the gen.py script.

The svgs have only been tested successfully with Inkscape, which I used 
to print the cards. The standardization state of flowed-text in svg is a 
little awkward right now (or so I am told), so at least firefox doesn't 
display the text on these cards correctly.

The phrases which are printed on the card are borrowed from the original 
[robotfindskitten][1], which is GPL2-or-later. My work is in the public 
domain (CC0, see COPYING for details).

[1]: http://robotfindskitten.org
