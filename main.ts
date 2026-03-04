/* Copyright (c) 2020 MTHS All rights reserved
 *
 * Created by: Jet Lu
 * Created on: Mar 2026
 * This program is Cookie Clicker.
*/

// create variable + reset
let cookies = 0
basic.showNumber(0)
basic.showIcon(IconNames.Happy)

// adds cookies on A pressed
input.onButtonPressed(Button.A, function() {
    basic.clearScreen()
    cookies = (cookies +1)
    basic.showNumber(cookies)
})

// resets cookies on B pressed
input.onButtonPressed(Button.B, function () {
    basic.clearScreen()
    cookies = 0
    basic.showNumber(cookies)
})
