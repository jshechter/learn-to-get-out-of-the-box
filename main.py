def on_button_pressed_a():
    global sonar_switch
    if sonar_switch == 0:
        basic.pause(2000)
        sonar_switch = 1
        basic.show_icon(IconNames.YES)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global Sonar_Test
    Sonar_Test = 1
    basic.show_icon(IconNames.SMALL_DIAMOND)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global Sonar_Test, sonar_switch
    kitronik_simple_servo.servo_stop(kitronik_simple_servo.ServoChoice.SERVO1)
    kitronik_simple_servo.servo_stop(kitronik_simple_servo.ServoChoice.SERVO2)
    Sonar_Test = 0
    sonar_switch = 0
    basic.show_icon(IconNames.NO)
input.on_button_pressed(Button.B, on_button_pressed_b)

sonar_current = 0
Sonar_Test = 0
sonar_switch = 0
sonar_switch = 0
Sonar_Test = 0
basic.show_icon(IconNames.HAPPY)

def on_forever():
    global sonar_current
    if sonar_switch == 1:
        while True:
            sonar_current = sonar.ping(DigitalPin.P1, DigitalPin.P2, PingUnit.CENTIMETERS)
            if sonar_current > 10:
                break
            basic.show_icon(IconNames.SWORD)
            kitronik_simple_servo.servo_run_percentage(kitronik_simple_servo.ServoChoice.SERVO1,
                kitronik_simple_servo.ServoDirection.CCW,
                10)
            kitronik_simple_servo.servo_run_percentage(kitronik_simple_servo.ServoChoice.SERVO2,
                kitronik_simple_servo.ServoDirection.CW,
                10)
            kitronik_simple_servo.servo_run_percentage(kitronik_simple_servo.ServoChoice.SERVO1,
                kitronik_simple_servo.ServoDirection.CW,
                5)
            kitronik_simple_servo.servo_run_percentage(kitronik_simple_servo.ServoChoice.SERVO2,
                kitronik_simple_servo.ServoDirection.CW,
                5)
        basic.show_icon(IconNames.GHOST)
        # One clockwise, one counter to go straight in current HW setup
        kitronik_simple_servo.servo_run_percentage(kitronik_simple_servo.ServoChoice.SERVO1,
            kitronik_simple_servo.ServoDirection.CW,
            20)
        kitronik_simple_servo.servo_run_percentage(kitronik_simple_servo.ServoChoice.SERVO2,
            kitronik_simple_servo.ServoDirection.CCW,
            20)
    if Sonar_Test == 1:
        sonar_current = sonar.ping(DigitalPin.P1, DigitalPin.P2, PingUnit.CENTIMETERS)
        basic.show_number(sonar_current)
basic.forever(on_forever)
