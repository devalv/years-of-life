# -*- coding: utf-8 -*-
import datetime

def draw_squares(screen_width: int = 156, 
                 square_size: int = 3, 
                 outline_size: int = 1, 
                 squares_count: int = 300):
    
    print('*' * screen_width)
    
    squares_in_row_count: int = screen_width // (outline_size + square_size)
    outline_str = ' ' * screen_width
    squares_in_current_row = 0
    line = ' '
    
    print(outline_str)
    for i in range(squares_count):
        
        if squares_in_current_row < squares_in_row_count:
            line += '[x]' + ' '
            squares_in_current_row += 1
        
        if squares_in_current_row == squares_in_row_count:
            print(line)
            print(outline_str)
            line = ' '
            squares_in_current_row = 0
    
    else:
        print(line)
        print(outline_str)
    
    print('*' * screen_width)

def squares_count(to_date: str) -> int:
    to_date_date = datetime.datetime.strptime(to_date, '%Y-%m-%d')
    delta = to_date_date - datetime.datetime.today()
    return delta.days

count = squares_count('2022-09-22')    
draw_squares(count)    
