import numpy as np
from AADI_RoverDomain.parameters import Parameters as p


def low_high_split(nobservers, rover_dist, rover_id, poi_id, poi_values):
    npartners = p.coupling - nobservers
    if npartners > 0:
        partners = np.zeros(npartners)

        if rover_id < p.num_rovers/2:
            if poi_values[poi_id] > 5.0:
                for partner_id in range(npartners):
                    partners[partner_id] = rover_dist
            else:
                for partner_id in range(npartners):
                    partners[partner_id] = 100.0
        else:
            if poi_values[poi_id] <= 5.0:
                for partner_id in range(npartners):
                    partners[partner_id] = rover_dist
            else:
                for partner_id in range(npartners):
                    partners[partner_id] = 100.0
    else:
        partners = 0
        npartners = 0

    return partners, npartners


def satisfy_coupling_high_value_incentive(rover_dist, poi_id, poi_values):
    npartners = p.coupling - 1

    partners = np.zeros(npartners)
    if poi_values[poi_id] > 5.0:
        for partner_id in range(npartners):
            partners[partner_id] = p.min_distance
    else:
        for partner_id in range(npartners):
            partners[partner_id] = rover_dist

    return partners, npartners


def high_value_only(rover_dist, poi_id, poi_values):
    npartners = p.coupling - 1

    partners = np.zeros(npartners)
    if poi_values[poi_id] > 5.0:
        for partner_id in range(npartners):
            partners[partner_id] = rover_dist
    else:
        for partner_id in range(npartners):
            partners[partner_id] = 100.0

    return partners, npartners


def high_value_only_with_steps(rover_dist, poi_id, poi_values, step_index):
    npartners = p.coupling - 1

    partners = np.zeros(npartners)
    if step_index <= p.num_steps * (3/4):
        if poi_values[poi_id] > 5.0:
            for partner_id in range(npartners):
                partners[partner_id] = rover_dist
        else:
            for partner_id in range(npartners):
                partners[partner_id] = 100.0

    else:
        for partner_id in range(npartners):
            partners[partner_id] = rover_dist

    return partners, npartners


def low_value_pois(nobservers, rover_dist, poi_id, poi_values):
    npartners = p.coupling - nobservers

    if npartners > 0:
        partners = np.zeros(npartners)
        if poi_values[poi_id] <= 5.0:
            for partner_id in range(npartners):
                partners[partner_id] = rover_dist
        else:
            for partner_id in range(npartners):
                partners[partner_id] = 100.0
    else:
        partners = 0
        npartners = 0

    return partners, npartners


def position_based(nobservers, rover_dist, rx, ry, poi_id, poi_values):
    npartners = p.coupling - nobservers

    if npartners > 0:
        partners = np.zeros(npartners)

        if ry > 15 and poi_values[poi_id] <= 5.0:
            for partner_id in range(npartners):
                partners[partner_id] = p.min_distance
        else:
            for partner_id in range(npartners):
                partners[partner_id] = rover_dist
    else:
        partners = 0
        npartners = 0

    return partners, npartners


def negative_distances(rover_dist, poi_id, poi_values):
    npartners = p.coupling - 1

    partners = np.zeros(npartners)

    if poi_values[poi_id] > 5:
        for partner_id in range(npartners):
            partners[partner_id] = rover_dist
    elif rover_dist < p.min_observation_dist:
        for partner_id in range(npartners):
            partners[partner_id] = -10.0
    else:
        for partner_id in range(npartners):
            partners[partner_id] = 100.00

    return partners, npartners


def aaa_sugg(rover_dist, poi_id, poi_values):
    npartners = p.coupling - 1

    partners = np.zeros(npartners)

    if poi_values[poi_id] > 5:
        for partner_id in range(npartners):
            partners[partner_id] = rover_dist

    elif poi_values[poi_id] <= 5:
        for partner_id in range(npartners):
            partners[partner_id] = rover_dist + partner_id + 1

    return partners, npartners


def adaptive_partners_with_steps(rover_dist, poi_id, poi_values, observer_count):
    npartners = observer_count

    partners = np.zeros(npartners)

    if poi_values[poi_id] > 5:
        for partner_id in range(npartners):
            partners[partner_id] = rover_dist
    elif rover_dist < p.min_observation_dist:
        for partner_id in range(npartners):
            partners[partner_id] = -10.0
    else:
        for partner_id in range(npartners):
            partners[partner_id] = 100.00

    return partners, npartners


def adaptive_partners_with_steps(rover_dist, poi_id, poi_values, observer_count, step_number):
    npartners = p.coupling - observer_count

    if npartners <= 0:
        npartners = p.coupling - 1

    partners = np.zeros(npartners)

    if step_number < (p.num_steps * 3) / 4:
        if poi_values[poi_id] > 5:
            for partner_id in range(npartners):
                partners[partner_id] = rover_dist
        elif rover_dist < p.min_observation_dist:
            for partner_id in range(npartners):
                partners[partner_id] = -10.0
        else:
            for partner_id in range(npartners):
                partners[partner_id] = 100.00

    else:
        for partner_id in range(npartners):
            partners[partner_id] = rover_dist

    return partners, npartners
