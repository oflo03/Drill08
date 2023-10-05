from pico2d import *
import random


# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

    def update(self):
        pass


class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)

    def draw(self):
        boy_image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5


class Ball:
    def __init__(self):
        self.x, self.y = random.randint(100, 750), 580
        self.size = random.randint(1, 2)
        self.speed = random.randint(5, 20)

    def draw(self):
        if self.size == 1:
            ball_image_s.draw(self.x, self.y)
        else:
            ball_image_b.draw(self.x, self.y)

    def update(self):
        self.y -= self.speed
        if self.size == 1 and self.y <= 65:
            self.speed = 0
            self.y = 65
        elif self.size == 2 and self.y <= 75:
            self.speed = 0
            self.y = 75


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def reset_world():
    global running
    global grass
    global team
    global boy_image
    global world
    global balls
    global ball_image_s
    global ball_image_b

    running = True
    world = []

    boy_image = load_image('run_animation.png')
    ball_image_s = load_image('ball21x21.png')
    ball_image_b = load_image('ball41x41.png')

    grass = Grass()
    world.append(grass)

    team = [Boy() for i in range(10)]
    world += team

    balls = [Ball() for i in range(20)]
    world += balls


def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()


def update_world():
    for o in world:
        o.update()
    pass


open_canvas()

# initialization code
reset_world()

# game main loop code
while running:
    handle_events()
    update_world()  # 객체들의 상호작용 결과 업데이트
    render_world()
    delay(0.05)

# finalization code
close_canvas()
