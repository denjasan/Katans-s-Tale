# encoding: utf-8
from functions import *
import Constants


class Camera:
    def __init__(self):
        self.dx = 0
        self.dy = 0
        self.go = True

    def apply(self, obj, target, start_pos=(0, 0), level=None, many_strart_poses=None):

        for k, i in enumerate(obj):
            if many_strart_poses:
                start_pos = many_strart_poses[k]
            if -215 <= (i.rect.x - start_pos[0]) + self.dx <= 0 and obj != laser_group:
                # print(i.rect.x, start_pos[0], self.dx, (i.rect.x - start_pos[0]) + self.dx)
                i.rect.x += self.dx
                self.go = True
            elif self.go and obj == laser_group:
                i.rect.x += self.dx
            else:
                self.go = False

            if obj == laser_group:
                level.lasers[k] = (i.rect.x, i.rect.y)

    def update(self, target):
        # print(target.moving)
        self.dx = 0
        if target.moving[LEFT] != target.moving[RIGHT] and not any(target.moving[2:]):
            if target.moving[LEFT] == 1:
                self.dx = 1 * target.speed
            if target.moving[RIGHT] == 1:
                self.dx = -1 * target.speed


