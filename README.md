Just a cellular automaton engine made for my learning of pygame.

You can simulate various cellular automatons like Conway's game of life, and you can also try your own.

Usage:\
    `python3 main.py`\
    This will use the default Game of Life rules.\
    you can use others rules by passing them as parameters as follow: `B[Begin rules]/S[Survive rules]/[number of refractory states]`.\
    Else you can use the name of a predefined rules set:\
    - `life` default GoL\
    - `highlife` alternate life\
    - `replicator` reproduce any pattern every 7 generations\
    - `seeds` die every generation\
    - `maze` maze-like pattern\
    - `bbrain` simple refractory life rules\
    - `star_wars` replicate bases, spaceships and asteroids\
    - `star_wars2` alternate rules for star wars (I prefer this one)\
    - `wall` create solid shapes\
    - `coag` cover large areas slowly\
    - `assimilation` assimilate any nearby cells\
