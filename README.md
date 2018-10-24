# AllocationGridGenerator

This tool makes it simple to generate a list of parameter settings to complete a grid search of parameters when the sum of all parameters is fixed.

An examples of this is for an "Asset Liability Study" where the investment strategy is limited to be an allocation to asset classes that sums to 100%

## Implementing the tool in your project

There are two possibles ways to use this tool:
* As a script to generate a csv. The test.py document sets out a script that be used to generate a csv of the possible purmations of the parameter
* Directly in a python program. Please feel free to make use of the file with any adjustments you think neccessary

### Using the tool 

The format of the inputs for the tool are as follows:
*balls: int
*maximum_balls_list:[int]

#### Basic use:

    gg = Grid_Generator([10, [3, 3, 4, 4]) #Initialise the Grid Generator
    gg.create_grid() # returns a pandas dataframe of the results

#### More practical use example:
    
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
    results = (minimum_allocation + grid_size*results).round(4) #Note rounding is to deal with floating point issues
    print(results.round(4))
    results.to_csv('./asset_class_allocations.csv', sep='\t', encoding='utf-8')

Note in this second example some consideration of floating arithmetic needs to be considered to ensure that rounding does not lead to small discrepancies

## Authors

**John Thurman** - *Initial work* 

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
