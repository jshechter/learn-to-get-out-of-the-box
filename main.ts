input.onButtonPressed(Button.A, function () {
    if (sonar_switch == 0) {
        basic.pause(2000)
        sonar_switch = 1
        basic.showIcon(IconNames.Yes)
    }
})
input.onButtonPressed(Button.AB, function () {
    Sonar_Test = 1
    basic.showIcon(IconNames.SmallDiamond)
})
input.onButtonPressed(Button.B, function () {
    kitronik_simple_servo.servoStop(kitronik_simple_servo.ServoChoice.servo1)
    kitronik_simple_servo.servoStop(kitronik_simple_servo.ServoChoice.servo2)
    Sonar_Test = 0
    sonar_switch = 0
    basic.showIcon(IconNames.No)
})
let sonar_current = 0
let Sonar_Test = 0
let sonar_switch = 0
sonar_switch = 0
Sonar_Test = 0
basic.showIcon(IconNames.Happy)
basic.forever(function () {
    if (sonar_switch == 1) {
        while (true) {
            sonar_current = sonar.ping(
            DigitalPin.P1,
            DigitalPin.P2,
            PingUnit.Centimeters
            )
            if (sonar_current > 10) {
                break;
            }
            basic.showIcon(IconNames.Sword)
            kitronik_simple_servo.servoRunPercentage(kitronik_simple_servo.ServoChoice.servo1, kitronik_simple_servo.ServoDirection.CCW, 10)
            kitronik_simple_servo.servoRunPercentage(kitronik_simple_servo.ServoChoice.servo2, kitronik_simple_servo.ServoDirection.CW, 10)
            kitronik_simple_servo.servoRunPercentage(kitronik_simple_servo.ServoChoice.servo1, kitronik_simple_servo.ServoDirection.CW, 5)
            kitronik_simple_servo.servoRunPercentage(kitronik_simple_servo.ServoChoice.servo2, kitronik_simple_servo.ServoDirection.CW, 5)
        }
        basic.showIcon(IconNames.Ghost)
        // One clockwise, one counter to go straight in current HW setup
        kitronik_simple_servo.servoRunPercentage(kitronik_simple_servo.ServoChoice.servo1, kitronik_simple_servo.ServoDirection.CW, 20)
        kitronik_simple_servo.servoRunPercentage(kitronik_simple_servo.ServoChoice.servo2, kitronik_simple_servo.ServoDirection.CCW, 20)
    }
    if (Sonar_Test == 1) {
        sonar_current = sonar.ping(
        DigitalPin.P1,
        DigitalPin.P2,
        PingUnit.Centimeters
        )
        basic.showNumber(sonar_current)
    }
})
