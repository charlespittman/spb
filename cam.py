# Takes several pictures.
# Requires picamera (python-picamera)

import time
import picamera


def main():
    with picamera.PiCamera() as camera:
        camera.resolution = (1024, 768)

        # Wait for the automatic gain control to settle
        time.sleep(1)

        # Set values so that set of pictures have the same brightness, color,
        # and contrast.
        camera.shutter_speed = camera.exposure_speed
        camera.exposure_mode = 'off'
        g = camera.awb_gains
        camera.awb_mode = 'off'
        camera.awb_gains = g

        # Take 5 shots, saving file in current directory with timestamp.
        camera.capture_sequence(
            ['{}_{:02d}.jpg'.format(time.strftime('%Y.%m.%d-%H:%M:%S'), i)
             for i in range(5)])

if __name__ == '__main__':
    main()
