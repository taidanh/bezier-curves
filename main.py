#! /usr/bin/env python3

import pygame as pg
from pygame.locals import *

# PYGAME SETTINGS
pg.init()
window = (1280, 720)
screen = pg.display.set_mode(window)
last_event = 0

clock = pg.time.Clock()

def quad_bezier(t, p0, p1, p2):
    x = (1 - t)**2 * p0[0] + 2 * (1 - t) * t * p1[0] + t**2 * p2[0]
    y = (1 - t)**2 * p0[1] + 2 * (1 - t) * t * p1[1] + t**2 * p2[1]
    return (x, y)

print(quad_bezier(.7676, (0,0), (-1, 1,5), (4,0)))

curves = []
c = []
p0 = (0,0)
p1 = (0,0)
p2 = (0,0)

running = True

while running:

    screen.fill((0,0,0))

    pg.draw.circle(screen, (115,115,115), (window[0], window[1]), 15)

    dt = clock.tick()
    last_event += dt


    if pg.mouse.get_pressed()[0] and last_event > 250:
        print("mouse pressed")
        last_event = 0
        if p0 == (0,0):
            print("setting p0")
            p0 = pg.mouse.get_pos()

        elif p2 == (0,0):
            print("setting p2")
            p2 = pg.mouse.get_pos()
        else:
            curves.append(c)
            p0 = (0,0)
            p2 = (0,0)

    p1 = pg.mouse.get_pos()

    # draw lines from points to mouse
    pg.draw.line(screen, (0,80,0), p1, p0)
    pg.draw.line(screen, (0,80,0), p1, p2)

    # draw start and end points
    pg.draw.circle(screen, (255,0,0), p0, 2)
    pg.draw.circle(screen, (0,255,0), p2, 2)

    if p0 != (0,0) and p2 != (0,0):
        pg.draw.circle(screen, (0,115,0), (window[0] - 20, 20), 10)
        t = 0.0
        c = []
        while t < 1:
            c.append(quad_bezier(t, p0, p1, p2))
            t += 0.02

    if len(c) > 2:
            pg.draw.lines(screen, (255,255,255), 0, c)

    for curve in curves:
        if len(curve) > 2:
            pg.draw.lines(screen, (255,255,255), 0, curve)

    pg.display.flip()

    # check if user closed game
    for event in pg.event.get():
        if event.type == QUIT:
            print("quitting game...")
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            if event.key == K_SPACE:
                pause ^= 1
