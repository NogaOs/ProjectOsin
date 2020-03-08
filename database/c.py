def get_x_axis_id(x): # when y = 0
    """ When y=0, get the id of a cell by the given x coordinate. """
    cell_id = 0
    step_size = 1
    for step in range(x):
        cell_id += step_size
        step_size += 1
    return cell_id

def solution2(x, y):
    """ After we have the id of the x axis, we start going up the y axis. 
    The first step size is equal to the given x coordinate, and grows by 1 with every step. """
    cell_id = get_x_axis_id(x)
    to_add = ( (y - 1) * (2 * x + (y - 2)) ) / 2
    return str(cell_id)


def solution(x, y):
    x_axis_id = ( y * (2 + (y - 1)) ) / 2
    wanted_cell_id = x_axis_id + 
    ( (y - 1) * (2 * x + (y - 2)) ) / 2
    return str(int(wanted_cell_id))

    
