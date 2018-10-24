import numpy as np
import pandas as pd
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

def test_create_largergrid():

    #Note that this takes ~3s to run. Think twice before increasing the size of the grid
    gg = Grid_Generator(10, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10])
    results_list = gg.create_grid()
    print(results_list)

def test_Investment_allocation_use():
    # The purpose is to generate the grid of all permutations of the parameters.
    # The parameters in total must equal 100%
    # For example, this can be considered an approach to review the asset allocation of an investment fund
    # E.g. it is not possible to allocation 70% to bonds and 70% to equity. Both numbers must add up to 100%.

    # Lets assume 5 asset classes
    minimum_allocation = [0.2, 0.0, 0.0, 0.1, 0.1]
    maximum_allocation = [0.5, 0.2, 0.2, 0.5, 0.2]
    # grid size is the distance between markers for each asset allocation:
    grid_size = 0.02

    # this is equivalent to the question of assigning balls between 0 and the follwoing,
    # with the following numbers of balls
    maximum_balls = ((np.array(maximum_allocation) - np.array(minimum_allocation))/grid_size).astype(int).tolist()
    total_balls = int((1 - sum(minimum_allocation))/grid_size)

    #Generate the equaivalent grid
    gg = Grid_Generator(total_balls, maximum_balls)
    results = gg.create_grid()

    #tidy up the numbers to turn back into percentages
    results = minimum_allocation + grid_size*results
    print(results)







