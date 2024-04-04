let num = 0
input.onButtonPressed(Button.A, function () {
    basic.clearScreen()
    num = randint(1, 5)
    if (num == 1) {
        basic.showLeds(`
            # . . . #
            . # . # .
            . . # . .
            . # . # .
            # . . . #
            `)
        music.play(music.stringPlayable("F E D C - - - - ", 120), music.PlaybackMode.UntilDone)
    } else if (num == 2) {
        basic.showLeds(`
            . . . . .
            . . . . #
            . . . # .
            # . # . .
            . # . . .
            `)
        music.play(music.stringPlayable("F C5 - - - - - - ", 120), music.PlaybackMode.UntilDone)
    } else if (num == 3) {
        basic.showLeds(`
            . # # # .
            # . . . #
            . . . . #
            . . . # .
            . . # . .
            `)
        music.play(music.stringPlayable("D D D D - - - - ", 120), music.PlaybackMode.UntilDone)
    } else if (num == 4) {
        basic.showString("Ask later")
    } else if (num == 5) {
        basic.showString("Hmm.")
    }
})
// rigged yes
input.onButtonPressed(Button.B, function () {
    basic.clearScreen()
    basic.showLeds(`
        # . . . #
        . # . # .
        . . # . .
        . # . # .
        # . . . #
        `)
    music.play(music.stringPlayable("F E D C - - - - ", 120), music.PlaybackMode.UntilDone)
})
