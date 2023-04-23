#!/usr/bin/env python
#-*- coding:utf-8 -*-

class Cell(object):
    """
        A cell of a board
        
        attributes
        ----------
        posx : int
            the x coordinate
        posy : int
            the y coordinate
        alive : bool
            the state of the cell
        ref: int
            the refractory state of the cell
        board: Board
                the board that contain the cell
        
        methods
        -------
        change_state()
            invert the state of the cell
        pos()
            get the position of the cell
        alive_around()
            get the number of alive cells around
    """
    
    def __init__(self, board, posx, posy, alive=False):
        """
            Cell class' constructor
            
            parameters
            ----------
            board: Board
                the board that contain the cell
            posx : int
                the x coordinate
            posy : int
                the y coordinate
            alive : bool (optional, default False)
                the state of the cell
            ref: int
                the refractory state of the cell
            
            returns
            -------
            None
        """
        self.board = board
        self.posx = posx
        self.posy = posy
        self.alive = alive
        self.ref = 0
    
    def change_state(self):
        """
            change the state of the cell
            
            parameters
            ----------
            None
            
            returns
            -------
            None
        """
        self.alive = not self.alive
    
    def pos(self):
        """
            get the coordiniates of the cell
            
            parameters
            ----------
            None
            
            returns
            -------
            Tuple
                the coordinates
        """
        return (self.posx, self.posy)
    
    def alive_around(self):
        """
            get the number of alive cells in the 8 surrouning cells
            
            parameters
            ----------
            None
            
            returns
            -------
            int [0;8]
                the number of alive cells around
        """
        return self.board.nb_alive(self.posx, self.posy)
    
    def __str__(self):
        """
            allows to convert a cell to a string
            
            parameters
            ----------
            None
            
            returns
            -------
            str
                1 or 0 the state of the cell
        """
        return str(int(self.alive))


class Board(object):
    """
        a board that contain cells
        
        attributes
        ----------
        grid : list[list]
            the grid that actually contain cells
        width : int
            width of the board
        height : int
            height of the board
        
        methods
        -------
        neighborhood(x, y)
            get the 8 surrounding cells
        nb_alive(x, y)
            get the number of alive cells around
        clear()
            clear the board
    """
    
    def __init__(self, width, height):
        """
            Board class' constructor
            set up the attributes
            
            parameters
            ----------
            width : int
                width of the grid
            height : int
                height of the grid
            
            returns
            -------
            None
        """
        self.grid = [
                    [Cell(self, x, y) for x in range(width)]
                    for y in range(height)
                    ]
        self.width = width
        self.height = height
    
    def neighborhood(self, x, y):
        """
            get the 8 surrounding tiles from a given position
            eventually, there may beless than 8 tiles, when the pos
            is at the border
            
            parameters
            ----------
            x : int
                x pos of the cell
            y : int
                y pos of the cell
            
            returns
            -------
            result : list[Cell]
                the neighbors
        """
        result = list()
        for i in range(-1, 2, 1):
            for j in range(-1, 2, 1):
                if i == 0 and j == 0:
                    pass
                else:
                    abcsis = x + j
                    ordinate = y + i
                    if abcsis == self.width:
                        abcsis = 0
                    if ordinate == self.height:
                        ordinate = 0
                    result.append(
                        self.grid[ordinate][abcsis]
                        )
        return result
    
    def nb_alive(self, x, y):
        """
            get the nuber of cells alive around a given pos
            the number will be between 0 and 8
            
            parameters
            ----------
            x : int
                x pos of the cell
            y : int
                y pos of the cell
            
            returns
            -------
            nb : int
                number of alive cells around
        """
        nb = 0
        for cell in self.neighborhood(x, y):
            if cell.alive:
                nb += 1
        return nb
    
    def clear(self):
        """
            recreate the entire grid
            
            parameters
            ----------
            None
            
            returns
            -------
            None
        """
        self.grid = [
                    [Cell(self, x, y) for x in range(self.width)]
                    for y in range(self.height)
                    ]
    
    def __str__(self):
        """
            allows to convert the board to a string
            this will display all cells in rows
            
            parameters
            ----------
            None
            
            returns
            -------
            result : str
                the board
        """
        result = str()
        for row in self.grid:
            for cell in row:
                result += str(cell)
            result += '\n'
        return result
    
    def __getitem__(self, index):
        """
            allow to pick a row of the board with an index
            
            parameters
            ----------
            index: int
                the index
            
            returns
            -------
            list
                the row corresponding to the index
        """
        return self.grid[index]
    
    def __iter__(self):
        """
            allow the iteration of the board
            
            parameters
            ----------
            None
            
            returns
            -------
            each cell on the board, begin at top left
        """
        for row in self.grid:
            for cell in row:
                yield cell

if __name__ == '__main__':
    board = Board(5, 5)
    for cell in board:
        print(cell)

