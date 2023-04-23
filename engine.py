#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
    engine for life-like cellular automatons
    
    funcions
    --------
    
    begin(nb)
        the rule for a cell's birth
    
    stay(nb)
        the rule for a cell's survival
    
    step(board)
        simulate a step
    
    update(board)
        update the board in-place
    
    CONSTANTS
    ---------
    BEGIN: str
        the birth rule
    STAY: str
        the suvival rule
    REFRACTORY: int
        the number of refractory states
    RULES: dict
        a dict that contain some pre-sets for rules
"""
#Rules:
BEGIN = "3"
STAY = "23"
REFRACTORY = 0

#pre-sets:
RULES = {
    "life": "B3/S23",
    "highlife": "B36/S23",
    "34 life": "B34/S34",
    "no death": "B3/S012345678",
    "replicator": "B1357/S1357",
    "seeds": "B2/S",
    "maze": "B3/S12345",
    "bbrain": "B2/S/3",
    "star_wars": "B2/S345/4",
    "star_wars2": "B278/S3456/6",
    "walls": "B45678/S2345",
    "coag": "B378/S235678",
    "assimilation": "B345/S4567"
}

def set_rules(rules):
    """
        set up the rules contants
        
        parameters
        ----------
        rule : str
            the rule like B[begin rule]/S[stay rule]/[refractory]
            or the name of a rule (e.g Maze, Highlife...)
        
        returns
        -------
        None
    """
    global BEGIN
    global STAY
    global REFRACTORY
    
    if rules.lower() in RULES.keys():
        rules = RULES[rules.lower()]
    
    rules = rules.split("/")
    if len(rules) == 3 and int(rules[2]) > 2:
        REFRACTORY = int(rules[2]) - 2
    BEGIN = rules[0].split("B")[1]
    STAY = rules[1].split("S")[1]

def begin(nb):
    """
        rule for the birth of a cell
        
        parameters
        ----------
        nb : int [0;8]
            the number of alive cells around the cell
        
        returns
        -------
        bool
            True if the cells need to birth
    """
    return str(nb) in BEGIN

def stay(nb):
    """
        rule for the survival of a cell
        
        parameters
        ----------
        nb : int [0;8]
            the number of alive cells around the cell
        
        returns
        -------
        bool
            True if the cell survive
    """
    return str(nb) in STAY

def step(board):
    """
        simulate a step of the game of life
        
        parameters
        ----------
        board : Board
            the board
        
        returns
        -------
        births : list[Cell]
            the list of all cells that will birth
        deaths : list[Cell]
            the list of all cells that wall die
        refractory : list[Cell]
            the list of cells on cooldown
    """
    births = list()
    deaths = list()
    refractory = list()
    for cell in board:
        nb_alive = cell.alive_around()
        if (cell.alive and
        not stay(nb_alive)):
            deaths.append(cell.pos())
        elif (not cell.alive and
        begin(nb_alive) and
        not cell.ref):
            births.append(cell.pos())
        if cell.ref:
            refractory.append(cell.pos())
    return (births, deaths, refractory)

def update(board, births, deaths, refractory):
    """
        apply the stet and update the board
        
        parameters
        ----------
        board : Board
            the board to update
        births : list[Cell]
            the list of all cells that will birth
        deaths : list[Cell]
            the list of all cells that wall die
        refractory : list[Cell]
            the list of cells on cooldown
        
        returns
        -------
        None
    """
    for x, y in refractory:
        board[y][x].ref -= 1
    for x, y in births:
        board[y][x].change_state()
    for x, y in deaths:
        board[y][x].change_state()
        board[y][x].ref = REFRACTORY

if __name__ == '__main__':
    print(BEGIN, STAY, REFRACTORY)
    set_rules("Maze")
    print(BEGIN, STAY, REFRACTORY)

