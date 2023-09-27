from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

def handle_events():
    global running, dir_x, dir_y
    global x, y

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_x += 1
            elif event.key == SDLK_LEFT:
                dir_x -= 1
            elif event.key == SDLK_UP:
                dir_y += 1
            elif event.key == SDLK_DOWN:
                dir_y -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_x -= 1
            elif event.key == SDLK_LEFT:
                dir_x += 1
            elif event.key == SDLK_UP:
                dir_y -= 1
            elif event.key == SDLK_DOWN:
                dir_y += 1

running = True
x = TUK_WIDTH // 2
y = TUK_HEIGHT // 2
frame = 0
dir_x = 0
dir_y = 0


while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

    if dir_x > 0:
        if x < TUK_WIDTH - 75:
            x += dir_x * 5
        else:
            x = TUK_WIDTH - 75
        if y > 75:
            y += dir_y * 5
        else:
            y = 75
        if y < TUK_HEIGHT - 75:
            y += dir_y * 5
        else:
            y = TUK_HEIGHT - 75
        character.clip_draw(frame * 66, 66, 66, 66, x, y, 150, 150)
    elif dir_x < 0:
        if x > 75:
            x += dir_x * 5
        else:
            x = 75
        if y > 75:
            y += dir_y * 5
        else:
            y = 75
        if y < TUK_HEIGHT - 75:
            y += dir_y * 5
        else:
            y = TUK_HEIGHT - 75
        character.clip_draw(frame * 66, 132, 66, 66, x, y, 150, 150)
    elif dir_y > 0:
        if y < TUK_HEIGHT - 75:
            y += dir_y * 5
        else:
            y = TUK_HEIGHT - 75
        character.clip_draw(frame * 66, 0, 66, 66, x, y, 150, 150)
    elif dir_y < 0:
        if y > 75:
            y += dir_y * 5
        else:
            y = 75
        character.clip_draw(frame * 66, 198, 66, 66, x, y, 150, 150)
    else:
        character.clip_draw(frame * 66, 198, 66, 66, x, y, 150, 150)

    update_canvas()
    handle_events()
    frame = (frame + 1) % 4
    x += dir_x * 10
    y += dir_y * 10
    delay(0.03)

close_canvas()