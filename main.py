num = 0

def on_button_pressed_a():
    global num
    basic.clear_screen()
    num = randint(1, 5)
    if num == 1:
        basic.show_string("Ask later")
        music.play(music.string_playable("F E D C - - - - ", 120),
            music.PlaybackMode.UNTIL_DONE)
    elif num == 2:
        basic.show_string("Hmm.")
        music.play(music.string_playable("D D D D - - - - ", 120),
            music.PlaybackMode.UNTIL_DONE)
    elif num == 3:
        basic.show_string("Yes!")
        music.play(music.string_playable("F C5 - - - - - - ", 120),
            music.PlaybackMode.UNTIL_DONE)
    elif num == 4:
        basic.show_string("No!")
        music.play(music.string_playable("F E D C - - - - ", 120),
            music.PlaybackMode.UNTIL_DONE)
    elif num == 5:
        basic.show_string("Maybe?")
        music.play(music.string_playable("D D D D - - - - ", 120),
            music.PlaybackMode.UNTIL_DONE)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.clear_screen()
    if num == 1:
        basic.show_leds("""
            . . . . .
            . . . . .
            . . # . .
            # # . # #
            . . . . .
            """)
        basic.show_string("Ask later")
        music.play(music.string_playable("F E D C - - - - ", 120),
            music.PlaybackMode.UNTIL_DONE)
    elif num == 2:
        basic.show_leds("""
            . . . . .
            . . . # #
            # # . . .
            . . . . .
            . . . . .
            """)
        music.play(music.string_playable("D D D D - - - - ", 120),
            music.PlaybackMode.UNTIL_DONE)
    elif num == 3:
        basic.show_leds("""
            . . . . .
            . . . . #
            . . . # .
            # . # . .
            . # . . .
            """)
        music.play(music.string_playable("F C5 - - - - - - ", 120),
            music.PlaybackMode.UNTIL_DONE)
    elif num == 4:
        basic.show_leds("""
            # . . . #
            . # . # .
            . . # . .
            . # . # .
            # . . . #
            """)
        music.play(music.string_playable("F E D C - - - - ", 120),
            music.PlaybackMode.UNTIL_DONE)
    elif num == 5:
        basic.show_leds("""
            . # # # #
            # . # # #
            . . # . .
            . . . . .
            . . # . .
            """)
        music.play(music.string_playable("D D D D - - - - ", 120),
            music.PlaybackMode.UNTIL_DONE)
input.on_button_pressed(Button.B, on_button_pressed_b)
