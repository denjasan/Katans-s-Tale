class Camera:
    def __init__(self):
        self.dx = 0
        self.dy = 0

    def apply(self, obj):
        obj.rect[1] += self.dx

    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - 800 // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - 600 // 2)