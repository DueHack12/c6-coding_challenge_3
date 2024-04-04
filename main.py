num = 0

def on_button_pressed_a():
    global num
    basic.clear_screen()
    num = randint(1, 5)
    if num == 1:
        basic.show_leds("""
            # . . . #
            . # . # .
            . . # . .
            . # . # .
            # . . . #
            """)
    elif num == 2:
        basic.show_leds("""
            . . . . .
            . . . . #
            . . . # .
            # . # . .
            . # . . .
            """)
    elif num == 3:
        basic.show_leds("""
            . # # # .
            # . . . #
            . . . . #
            . . . # .
            . . # . .
            """)
    elif num == 4:
        basic.show_string("Ask later")
    elif num == 5:
        basic.show_string("Hmm.")
input.on_button_pressed(Button.A, on_button_pressed_a)

# rigged yes
def on_button_pressed_b():
    basic.clear_screen()
    basic.show_leds("""
        . . . . .
        . . . . #
        . . . # .
        # . # . .
        . # . . .
        """)
input.on_button_pressed(Button.B, on_button_pressed_b)
