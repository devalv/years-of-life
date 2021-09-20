# -*- coding: utf-8 -*-

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
    
draw_squares()    
