import Constants


class Camera:
    def __init__(self):
        self.dx = 0
        self.dy = 0

    def apply(self, obj):
        obj.rect[0] += self.dx

    def update(self, target):
        print(target.moving)
        self.dx = 0
        if target.moving[0] == 1:
            self.dx = 1 * Constants.PLAYER_SPEED
        if target.moving[1] == 1:
            self.dx = -1 * Constants.PLAYER_SPEED
        # self.dx = -(target.rect.x + target.rect.w // 2 - 800 // 2)
        # self.dy = -(target.rect.y + target.rect.h // 2 - 600 // 2)