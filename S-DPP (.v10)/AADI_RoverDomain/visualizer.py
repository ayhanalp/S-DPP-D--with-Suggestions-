#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
import numpy as np
import time
import math
from AADI_RoverDomain.parameters import Parameters as p

pygame.font.init()  # you have to call this at the start, if you want to use this module
myfont = pygame.font.SysFont('Comic Sans MS', 30)


def draw(display, obj, x, y):
    display.blit(obj, (x, y))  # Correct for center of mass shift


def generate_color_array(num_colors): #generates num random colors
    color_arr = []
    
    for i in range(num_colors):
        color_arr.append(list(np.random.choice(range(256), size=3)))
    
    return color_arr


def visualize(rd, episode_reward):
    scale_factor = 25  # Scaling factor for images
    width = 32  # robot icon widths
    x_map = p.x_dim + 10  # Slightly larger so POI are not cut off
    y_map = p.y_dim + 10
    image_adjust = 100  # Adjusts the image so that everything is centered
    pygame.init()
    game_display = pygame.display.set_mode((x_map*scale_factor, y_map*scale_factor))
    pygame.display.set_caption('Rover Domain')
    robot_image = pygame.image.load('./AADI_RoverDomain/robot.png')
    background = pygame.image.load('./AADI_RoverDomain/background.png')
    greenflag = pygame.image.load('./AADI_RoverDomain/greenflag.png')
    redflag = pygame.image.load('./AADI_RoverDomain/redflag.png')
    color_array = generate_color_array(p.num_rovers)
    pygame.font.init() 
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    poi_status = [False for _ in range(p.num_pois)]
    
    for tstep in range(p.num_steps):
        draw(game_display, background, image_adjust, image_adjust)
        for poi_id in range(p.num_pois):  # Draw POI and POI values
            poi_x = int(rd.poi_pos[poi_id, 0] * scale_factor-width) + image_adjust
            poi_y = int(rd.poi_pos[poi_id, 1] * scale_factor-width) + image_adjust

            observer_count = 0
            for rover_id in range(p.num_rovers):
                x_dist = rd.poi_pos[poi_id, 0] - rd.rover_path[tstep, rover_id, 0]
                y_dist = rd.poi_pos[poi_id, 1] - rd.rover_path[tstep, rover_id, 1]
                dist = math.sqrt((x_dist**2) + (y_dist**2))

                if dist <= p.min_observation_dist:
                    observer_count += 1


            if observer_count >= p.coupling:
                poi_status[poi_id] = True

            if poi_status[poi_id]:
                draw(game_display, greenflag, poi_x, poi_y)  # POI observed
            else:
                draw(game_display, redflag, poi_x, poi_y)  # POI not observed
            textsurface = myfont.render(str(rd.poi_values[poi_id]), False, (0, 0, 0))
            target_x = int(rd.poi_pos[poi_id, 0]*scale_factor-scale_factor/3) + image_adjust
            target_y = int(rd.poi_pos[poi_id, 1]*scale_factor-width) + image_adjust
            draw(game_display, textsurface, target_x, target_y)

        for rov_id in range(p.num_rovers):  # Draw all rovers and their trajectories
            rover_x = int(rd.rover_path[tstep, rov_id, 0]*scale_factor) + image_adjust
            rover_y = int(rd.rover_path[tstep, rov_id, 1]*scale_factor) + image_adjust
            draw(game_display, robot_image, rover_x, rover_y)

            if tstep != 0:  # start drawing trails from timestep 1.
                for timestep in range(1, tstep):  # draw the trajectory lines
                    line_color = tuple(color_array[rov_id])
                    start_x = int(rd.rover_path[(timestep-1), rov_id, 0]*scale_factor) + width/2 + image_adjust
                    start_y = int(rd.rover_path[(timestep-1), rov_id, 1]*scale_factor) + width/2 + image_adjust
                    end_x = int(rd.rover_path[timestep, rov_id, 0]*scale_factor) + width/2 + image_adjust
                    end_y = int(rd.rover_path[timestep, rov_id, 1]*scale_factor) + width/2 + image_adjust
                    line_width = 3
                    pygame.draw.line(game_display, line_color, (start_x, start_y), (end_x, end_y), line_width)
                    origin_x = int(rd.rover_path[timestep, rov_id, 0]*scale_factor) + int(width/2) + image_adjust
                    origin_y = int(rd.rover_path[timestep, rov_id, 1]*scale_factor) + int(width/2) + image_adjust
                    circle_rad = 3
                    pygame.draw.circle(game_display, line_color, (origin_x, origin_y), circle_rad)
        
        pygame.display.update()
        time.sleep(0.1)
        
    scoresurface = myfont.render('The system reward obtained is ' + str(round(episode_reward, 2)), False, (0, 0, 0))
    draw(game_display, scoresurface, x_map*scale_factor-500, 20)
    pygame.display.update()

    running = True  # Keeps visualizer from closing until you 'X' out of window
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
