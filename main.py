#!/usr/bin/env python
#-*- coding:utf-8 -*-

import pygame as pg
import sys
from engine import step, update, set_rules
from board import Board


pg.init()
#set up constants
size = width, height = 1800, 1000
white = (255, 255, 255)
black = (0, 0, 0)
#set up the screen and other important things
pg.display.init()
screen = pg.display.set_mode(size)
icon = pg.image.load('icon.png')
pg.display.set_icon(icon)
pg.display.set_caption('Game of Life')
board = Board(width // 10, height // 10)
#set up the rules
if len(sys.argv) > 2:
    print("usage:\n\tpython Gol.py [rules]")
    sys.exit()
elif len(sys.argv) == 2:
    set_rules(sys.argv[1])

running = True
pause = True
#then launch the main loop
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        
        if event.type == pg.MOUSEBUTTONDOWN:
            posx = round(event.__dict__['pos'][0]-5, -1)
            posy = round(event.__dict__['pos'][1]-5, -1)
            board[posy//10][posx//10].change_state()
            if board[posy//10][posx//10].alive:
                color = white
            else:
                color = black
            pg.draw.rect(screen, color, pg.Rect(posx+1, posy+1, 8, 8))
            
        if (event.type == pg.KEYDOWN and
        event.__dict__['unicode'] == 'c'):
            screen.fill(black)
            board.clear()
        
        if (event.type == pg.KEYDOWN and
        event.__dict__['unicode'] == ' '):
            pause = not pause
        
        if (event.type == pg.KEYDOWN and
        event.__dict__['unicode'] == 's' and
        pause):
            births, deaths, ref = step(board)
            for x, y in births:
                pg.draw.rect(screen, white, pg.Rect(x*10+1, y*10+1, 8, 8))
            for x, y in deaths:
                pg.draw.rect(screen, black, pg.Rect(x*10+1, y*10+1, 8, 8))
            update(board, births, deaths, ref)
    
    if not pause:
        births, deaths, ref = step(board)
        for x, y in births:
            pg.draw.rect(screen, white, pg.Rect(x*10+1, y*10+1, 8, 8))
        for x, y in deaths:
            pg.draw.rect(screen, black, pg.Rect(x*10+1, y*10+1, 8, 8))
        update(board, births, deaths, ref)
    pg.display.flip()

