import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
# Define GPIO pins for servo motors
pan_pin = 17
tilt_pin = 18
# Define GPIO pins for stepper motor
step_pin = 23
dir_pin = 24
enable_pin = 25
# Setup GPIO pins
GPIO.setup(pan_pin, GPIO.OUT)
GPIO.setup(tilt_pin, GPIO.OUT)
GPIO.setup(step_pin, GPIO.OUT)
GPIO.setup(dir_pin, GPIO.OUT)
GPIO.setup(enable_pin, GPIO.OUT)
pan_pwm = GPIO.PWM(pan_pin, 50)  # 50 Hz frequency
tilt_pwm = GPIO.PWM(tilt_pin, 50)  # 50 Hz frequency
# Initialize variables for stepper motor control
delay = 0.001  # Adjust as per motor speed and requirement
# Function to capture photo based on device position
def capture_photo():
    print("Capturing photo...")
def move_servos(pan_angle, tilt_angle):
    pan_pwm.start(pan_angle)
    tilt_pwm.start(tilt_angle)
def move_stepper(steps, direction):
    GPIO.output(dir_pin, direction)
    for _ in range(steps):
        GPIO.output(step_pin, GPIO.HIGH)
        sleep(delay)
        GPIO.output(step_pin, GPIO.LOW)
        sleep(delay)
# Main function to control the device
def main():
    try:
        while True:
            # User input for photo capture
            user_input = input("Press Enter to capture photo (q to quit): ")
            if user_input.lower() == 'q':
                break
            # Get user input for servo angles and stepper motor steps
            pan_angle = float(input("Enter pan angle (0-180 degrees): "))
            tilt_angle = float(input("Enter tilt angle (0-180 degrees): "))
            steps = int(input("Enter stepper motor steps for height adjustment: "))
            direction = GPIO.HIGH if steps > 0 else GPIO.LOW  
            # Move servo motors and stepper motor
            move_servos(pan_angle, tilt_angle)
            move_stepper(abs(steps), direction)
            # Capture photo
            capture_photo()
    except KeyboardInterrupt:
        print("\nExiting program...")
    finally:
        # Clean up GPIO
        GPIO.cleanup()
        print("GPIO cleanup completed.")
if __name__ == "__main__":
    main()
