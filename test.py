import pytest
from Bucket_Grid_Generator import Grid_Generator


def test_creategenerator():
    Grid_Generator(10,[3,3,4,4])

def test_first_steps():
    grid_generator = Grid_Generator(10, [3, 3, 4, 4])
    gg_array = grid_generator.take_step()
    assert(len(gg_array) == 4)

def test_structure():
    grid_generator = Grid_Generator(10, [3, 3, 4, 4])
    print(grid_generator)

def test_length():
    gg1 = Grid_Generator(10, [3, 3, 4, 4])
    print('\n length of gg1: {}' .format(len(gg1)))
    print(gg1)

    gg2 = gg1.take_step()[0]
    print('length of gg2: {} \n' .format(len(gg2)))
    print(gg2)

def test_create_grid():

    gg = Grid_Generator(10, [3, 3, 4, 4])
    results_list = gg.create_grid()
    print(results_list)

def test_create_largegrid():

    gg = Grid_Generator(10, [10, 10, 10, 10])
    results_list = gg.create_grid()
    print(results_list)