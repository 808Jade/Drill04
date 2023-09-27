from pico2d import *


TUK_WIDTH, TUK_HEIGHT = 1280,1024
open_canvas(TUK_WIDTH, TUK_HEIGHT) # 캔버스가 준비되지 않은 상태에서는 이미지를 로드할 수 없다.
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')


character = load_image('animation_sheet.png')


def handle_events():
    global running
    global x, y

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, TUK_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


running = True
frame = 0
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
hide_cursor()



while running:
    clear_canvas()

    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame*100, 100*1, 100, 100, x, y)

    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    delay(0.05)

close_canvas()



