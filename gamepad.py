import sdl2

last_pos1 = 0
last_pos2 = 0

sdl2.SDL_Init(sdl2.SDL_INIT_JOYSTICK)
joystick = sdl2.SDL_JoystickOpen(0)

print(joystick)

while True:
    sdl2.SDL_PumpEvents()
    pos1 = sdl2.SDL_JoystickGetAxis(joystick,1)
    pos2 = sdl2.SDL_JoystickGetAxis(joystick,3)
    if (pos1 != last_pos1 or pos2 != last_pos2):
        print(str(pos1) + ',' + str(pos2))
        last_pos1,last_pos2 = pos1, pos2
