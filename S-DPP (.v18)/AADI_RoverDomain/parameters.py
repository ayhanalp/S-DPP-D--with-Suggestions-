"""
This file contains all constant test parameters which may be altered from this single
location for convenience.
"""


class Parameters:

    """
    TODO: Heterogeneous rover domain code currently not implemented
    """

    # Run Parameters
    stat_runs = 1
    generations = 500  # Number of generations for CCEA in each stat run
    visualizer_on = True  # Turn visualizer on or off (TURN OFF FOR MULTIPLE STAT RUNS)
    new_world_config = False  # False -> Reuse existing world config, True -> Use new world config

    # Domain parameters
    team_types = 'homogeneous'  # Switch between 'homogeneous' and 'heterogeneous' rover domains
    num_rovers = 10  # Number of rovers on map (GETS MULTIPLIED BY NUMBER OF TYPES)
    coupling = 3  # Number of rovers required to view a POI for credit
    num_pois = 16  # Number of POIs on map
    num_steps = 20  # Number of steps rovers take each episode
    min_distance = 1.0  # Minimum distance which may appear in the denominator of credit eval functions
    x_dim = 30  # X-Dimension of the rover map
    y_dim = 30  # Y-Dimension of the rover map
    min_observation_dist = 3.0  # Minimum distance rovers must be to observe POIs
    angle_resolution = 90  # Resolution of sensors (determines number of sectors)
    sensor_model = "summed"  # Should either be "density" or "closest"

    # Neural network parameters
    num_inputs = 8
    num_nodes = 9
    num_outputs = 2

    # CCEA parameters
    mutation_rate = 0.1  # Probability that a member of the offspring population will be mutated
    percentage_mut = 0.01  # Percentage of bits which get flipped in an individual
    epsilon = 0.1  # For e-greedy selection in CCEA
    parent_pop_size = 15
    offspring_pop_size = 5
    n_bits = 11  # Number of bits used to express a single weight in binary ccea

    # User specific parameters
    reward_type = "SDPP"  # Switch between reward functions "Global" "Difference" "DPP" "SDPP"
