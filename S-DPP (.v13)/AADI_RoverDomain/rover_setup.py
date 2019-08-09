from AADI_RoverDomain.parameters import Parameters as p
import numpy as np
import random
import math

### ROVER SETUP FUNCTIONS ######################################################

def init_rover_positions_fixed():  # Set rovers to fixed starting position
    """
    Rovers all start out in the middle of the map at an orientation of 0 degrees.
    :return: rover_positions: np array of size (nrovers, 3)
    """
    nrovers = p.num_rovers
    rover_positions = np.zeros((nrovers, 3))

    for rov_id in range(p.num_rovers):
        rover_positions[rov_id, 0] = 0.5*p.x_dim  # Rover X-Coordinate
        rover_positions[rov_id, 1] = 0.5*p.y_dim  # Rover Y-Coordinate
        rover_positions[rov_id, 2] = random.uniform(0, 360)  # Rover orientation

    return rover_positions

def init_rover_positions_random():  # Randomly set rovers on map
    """
    Rovers given random starting positions and orientations
    :return: rover_positions: np array of size (nrovers, 3)
    """
    nrovers = p.num_rovers
    rover_positions = np.zeros((nrovers, 3))

    for rov_id in range(p.num_rovers):
        rover_positions[rov_id, 0] = random.uniform(0, p.x_dim-1)  # Rover X-Coordinate
        rover_positions[rov_id, 1] = random.uniform(0, p.y_dim-1)  # Rover Y-Coordinate
        rover_positions[rov_id, 2] = random.uniform(0, 360)  # Rover orientation

    return rover_positions

def init_rover_positions_random_concentrated():
    """
        Rovers given random starting positions and orientations
        :return: rover_positions: np array of size (nrovers, 3)
        """
    nrovers = p.num_rovers
    rover_positions = np.zeros((nrovers, 3))

    for rov_id in range(p.num_rovers):
        rover_positions[rov_id, 0] = random.uniform(p.x_dim/4, 3*p.x_dim/4)  # Rover X-Coordinate
        rover_positions[rov_id, 1] = random.uniform(p.y_dim/4, 3*p.y_dim/4)  # Rover Y-Coordinate
        rover_positions[rov_id, 2] = random.uniform(0, 360)  # Rover orientation

    return rover_positions

### POI SETUP FUNCTIONS ###########################################################

def init_poi_positions_random():  # Randomly set POI on the map
    """
    POI positions set randomly across the map
    :return: poi_positions: np array of size (npoi, 2)
    """
    poi_positions = np.zeros((p.num_pois, 2))

    for poi_id in range(p.num_pois):
        poi_positions[poi_id, 0] = random.uniform(0, p.x_dim-1)
        poi_positions[poi_id, 1] = random.uniform(0, p.y_dim-1)

    return poi_positions

def init_poi_positions_circle():
    radius = 12.0
    interval = 360/p.num_pois

    poi_positions = np.zeros((p.num_pois, 2))

    x = p.x_dim/2
    y = p.y_dim/2
    theta = 0.0

    for poi_id in range(p.num_pois):
        poi_positions[poi_id, 0] = x + radius*math.cos(theta*math.pi/180)
        poi_positions[poi_id, 1] = y + radius*math.sin(theta*math.pi/180)
        theta += interval

    return poi_positions


def init_poi_positions_two_poi():
    """
    Sets two POI on the map, one on the left, one on the right at Y-Dimension/2
    :return: poi_positions: np array of size (npoi, 2)
    """
    assert(p.num_pois == 2)

    poi_positions = np.zeros((p.num_pois, 2))

    poi_positions[0, 0] = 0.0; poi_positions[0, 1] = p.y_dim/2
    poi_positions[1, 0] = (p.x_dim-1); poi_positions[1, 1] = p.y_dim/2

    return poi_positions


def init_poi_positions_four_corners():  # Statically set 4 POI (one in each corner)
    """
    Sets 4 POI on the map, one in each corner
    :return: poi_positions: np array of size (npoi, 2)
    """
    assert(p.num_pois == 4)  # There must only be 4 POI for this initialization

    poi_positions = np.zeros((p.num_pois, 2))

    poi_positions[0, 0] = 5.0; poi_positions[0, 1] = 5.0  # Bottom left
    poi_positions[1, 0] = 5.0; poi_positions[1, 1] = (p.y_dim - 5.0)  # Top left
    poi_positions[2, 0] = (p.x_dim - 5.0); poi_positions[2, 1] = 5.0  # Bottom right
    poi_positions[3, 0] = (p.x_dim - 5.0); poi_positions[3, 1] = (p.y_dim - 5.0)  # Top right

    return poi_positions

def init_poi_positions_txt_file():
    """
    POI positions read in from existing txt file (TXT FILE NEEDED FOR THIS FUNCTION)
    :return: poi_positions: np array of size (npoi, 2)
    """
    poi_positions = np.zeros((p.num_pois, 2))

    with open('Output_Data/POI_Positions.txt') as f:
        for i, l in enumerate(f):
            pass

    line_count = i + 1

    posFile = open('Output_Data/POI_Positions.txt', 'r')

    count = 1
    coordMat = []

    for line in posFile:
        for coord in line.split('\t'):
            if (coord != '\n') and (count == line_count):
                coordMat.append(float(coord))
        count += 1

    prev_pos = np.reshape(coordMat, (p.num_pois, 2))

    for ii in range(p.num_pois):
        poi_positions[ii, 0] = prev_pos[ii, 0]
        poi_positions[ii, 1] = prev_pos[ii, 1]

    return poi_positions



def init_poi_values_random():
    """
    POI values randomly assigned 1-10
    :return: poi_vals: array of size(npoi)
    """
    poi_vals = [0.0 for _ in range(p.num_pois)]

    for poi_id in range(p.num_pois):
        poi_vals[poi_id] = random.randint(1, 10)

    return poi_vals


def init_poi_values_fixed():
    """
    POI values set to fixed value
    :return: poi_vals: array of size(npoi)
    """
    poi_vals = np.zeros(p.num_pois)

    for poi_id in range(p.num_pois):
        poi_vals[poi_id] = poi_id + 1

    return poi_vals

def init_poi_values_half_and_half():
    """
    POI values set to fixed value
    :return: poi_vals: array of size(npoi)
    """

    poi_vals = [1.0 for _ in range(p.num_pois)]

    for poi_id in range(p.num_pois):
        if poi_id%2 == 0:
            poi_vals[poi_id] *= 10.0
        else:
            poi_vals[poi_id] *= 5.0

    return poi_vals

def init_case01_conf(isRandom):
    num_pois = p.num_pois
    num_rovers = p.num_rovers
    num_outer_pois = 4
    num_inner_pois = num_pois - num_outer_pois

    poi_positions = np.zeros((p.num_pois, 2))

    poi_positions[0, 0] = 0.0; poi_positions[0, 1] = 0.0  # Bottom left
    poi_positions[1, 0] = 0.0; poi_positions[1, 1] = (p.y_dim - 1.0)  # Top left
    poi_positions[2, 0] = (p.x_dim - 1.0); poi_positions[2, 1] = 0.0  # Bottom right
    poi_positions[3, 0] = (p.x_dim - 1.0); poi_positions[3, 1] = (p.y_dim - 1.0)  # Top right

    for i in range(4, num_pois):
        poi_positions[i, 0] = random.uniform(p.x_dim / 4, 3 * p.x_dim / 4)
        poi_positions[i, 1] = random.uniform(p.y_dim / 4, 3 * p.y_dim / 4)

    rover_positions = np.zeros((num_rovers, 3))

    for rov_id in range(p.num_rovers):
        rover_positions[rov_id, 0] = 0.5*p.x_dim  # Rover X-Coordinate
        rover_positions[rov_id, 1] = 0.5*p.y_dim  # Rover Y-Coordinate
        rover_positions[rov_id, 2] = 0.0  # Rover orientation

    poi_vals = [0.0 for _ in range(p.num_pois)]

    poi_vals[0] = 20
    poi_vals[1] = 20
    poi_vals[2] = 20
    poi_vals[3] = 20

    if isRandom:
        for poi_id in range(4, p.num_pois):
            poi_vals[poi_id] = random.randint(1, 10)

    else:
        for poi_id in range(4, p.num_pois):
            poi_vals[poi_id] = 4

    return poi_vals, poi_positions, rover_positions

def init_case02_conf(isRandom):
    num_pois = 12
    num_rovers = p.num_rovers

    poi_positions = np.zeros((num_pois, 2))
    poi_id = 0

    for i in range(4):
        for j in range(3):
            poi_positions[poi_id, 0] = j * ((p.x_dim - 10) / 2)
            poi_positions[poi_id, 1] = i * (p.y_dim / 3)
            print("X---> " + str(poi_positions[poi_id, 0]) + " Y---> " + str(poi_positions[poi_id, 1]))

            poi_id += 1

    rover_positions = np.zeros((num_rovers, 3))

    for rover_id in range(num_rovers):
        rover_positions[rover_id, 0] = p.x_dim - 1
        rover_positions[rover_id, 1] = random.uniform((p.y_dim / 2) - 5, (p.y_dim / 2) + 5)

    poi_vals = [0.0 for _ in range(p.num_pois)]

    if isRandom:
        for poi_id in range(p.num_pois):
            poi_vals[poi_id] = random.randint(1, 10)

    else:
        for poi_id in range(p.num_pois):
            poi_vals[poi_id] = 5

    return poi_vals, poi_positions, rover_positions


def init_case03_conf(isFixed):
    num_rovers = p.num_rovers

    poi_positions = np.zeros((8, 2))
    poi_id = 0

    poi_positions[0, 0] = (p.x_dim / 2) - 5
    poi_positions[0, 1] = (p.y_dim / 2) - 5

    poi_positions[1, 0] = (p.x_dim / 2) + 5
    poi_positions[1, 1] = (p.y_dim / 2) - 5

    poi_positions[2, 0] = (p.x_dim / 2) - 5
    poi_positions[2, 1] = (p.y_dim / 2) + 5

    poi_positions[3, 0] = (p.x_dim / 2) + 5
    poi_positions[3, 1] = (p.y_dim / 2) + 5

    poi_positions[4, 0] = (p.x_dim / 2) - 10
    poi_positions[4, 1] = (p.y_dim / 2) - 10

    poi_positions[5, 0] = (p.x_dim / 2) + 10
    poi_positions[5, 1] = (p.y_dim / 2) - 10

    poi_positions[6, 0] = (p.x_dim / 2) - 10
    poi_positions[6, 1] = (p.y_dim / 2) + 10

    poi_positions[7, 0] = (p.x_dim / 2) + 10
    poi_positions[7, 1] = (p.y_dim / 2) + 10

    rover_positions = np.zeros((num_rovers, 3))

    for rover_id in range(num_rovers):
        rover_positions[rover_id, 0] = p.x_dim / 2
        rover_positions[rover_id, 1] = p.y_dim / 2

    poi_vals = [0.0 for _ in range(p.num_pois)]

    poi_vals[0] = 4
    poi_vals[1] = 4
    poi_vals[2] = 4
    poi_vals[3] = 4

    poi_vals[4] = 20
    poi_vals[5] = 20
    poi_vals[6] = 20
    poi_vals[7] = 20

    return poi_vals, poi_positions, rover_positions


def init_case04_conf(isFixed):
    num_pois = 16
    num_rovers = p.num_rovers

    poi_positions = np.zeros((num_pois, 2))
    poi_id = 0
    adapt_dist = 0
    inorout = 0

    for i in range(2):
        for ii in range(3):
            for jj in range(3):
                x_val = adapt_dist / 2 + jj * ((p.x_dim - inorout) / 2)
                y_val = adapt_dist / 2 + ii * ((p.y_dim - inorout) / 2)

                if not ((x_val == (p.x_dim / 2)) and (y_val == (p.y_dim / 2))):
                    poi_positions[poi_id, 0] = x_val
                    poi_positions[poi_id, 1] = y_val

                    poi_id += 1

        adapt_dist += 10
        inorout += 10

    rover_positions = np.zeros((num_rovers, 3))

    for rover_id in range(num_rovers):
        rover_positions[rover_id, 0] = p.x_dim / 2
        rover_positions[rover_id, 1] = p.y_dim / 2

    poi_vals = [0.0 for _ in range(p.num_pois)]

    for poi_id in range(p.num_pois):
        if 0 <= poi_id < 8:
            poi_vals[poi_id] = 20

        else:
            poi_vals[poi_id] = 4

    return poi_vals, poi_positions, rover_positions
