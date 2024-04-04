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
    } else if (num == 2) {
        basic.showLeds(`
            . . . . .
            . . . . #
            . . . # .
            # . # . .
            . # . . .
            `)
    } else if (num == 3) {
        basic.showLeds(`
            . # # # .
            # . . . #
            . . . . #
            . . . # .
            . . # . .
            `)
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
        . . . . .
        . . . . #
        . . . # .
        # . # . .
        . # . . .
        `)
})
