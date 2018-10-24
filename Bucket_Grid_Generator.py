import numpy as np
import pandas as pd

class Grid_Generator(object):

    #<------------------Dunders------------------------------------------------>

    def __init__(self, balls: int, ball_maximum_list: [int], prior_allocation=None):
        self.balls_remaining = balls
        self.ball_maximum_list = ball_maximum_list
        if prior_allocation is None:
            self.prior_allocation = []
        else:
            self.prior_allocation = prior_allocation

    def __repr__(self):
        returnstring = 'Balls_maximum_list: {} \n'.format(self.ball_maximum_list)
        returnstring += 'Balls_remaining: {} \n'.format(self.balls_remaining)
        returnstring += 'Prior_allocation: {}'.format(self.prior_allocation)
        return returnstring

    def __len__(self):
        return len(self.ball_maximum_list)

    # <---------------- methods to complete the grid------------------------->
    def take_step(self):

        # Find the minimum and maximum balls to be added to this bucket
        # Note that a minimum comes about as you need to use all balls. E.g. If 10 balls remain but only space
        # for 3 more exists this would not work

        gg_array = [] # used to return all generated ggs
        min_balls = max(0,self.balls_remaining - sum(self.ball_maximum_list[1:]))
        max_balls = min(self.balls_remaining, self.ball_maximum_list[0])

        for i in range(min_balls, max_balls+1):
            allocation = self.prior_allocation[:]
            allocation.append(i)
            new_gg = Grid_Generator(self.balls_remaining - i, self.ball_maximum_list[1:], allocation )
            gg_array.append(new_gg)

        return gg_array

    def create_grid(self) -> pd.DataFrame():
        #TODO reorder the asset classes by largest to smallest allocations

        gg_stack = []
        results_list = []
        gg_stack.append(self)

        while len(gg_stack) > 0:
            gg = gg_stack.pop()
            if (len(gg)) == 0:
                results_list.append(gg.prior_allocation)
            else:
                gg_stack.extend(gg.take_step())

        return pd.DataFrame(results_list)

