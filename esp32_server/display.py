import time
from machine import Pin, I2C, Timer
import ssd1306


class OledDisplay:
    def __init__(self, width=128, height=64, scl_pin=22, sda_pin=21):
        # Initialize I2C and OLED display
        self.i2c = I2C(scl=Pin(scl_pin), sda=Pin(sda_pin))
        self.oled = ssd1306.SSD1306_I2C(width, height, self.i2c)
        self.timer = Timer(0)
        self.continue_display = False  # Control flag for the continuous message

    def update_wifi_status(self, status):
        """ Update the Wi-Fi connection status to be displayed. """
        self.wifi_status = status

    def display_status(self, timer):
        """ Function to be called periodically to update the OLED display. """
        self.oled.fill(0)  # Clear the display

        # Add other status information here, e.g., core usage
        self.oled.text("Other info:", 0, 10)
        self.oled.text("Core Usage: Busy", 0, 20)

        # Update the display with new content
        self.oled.show()

    def start_display_timer(self, period=1000):
        """ Start the timer that periodically refreshes the OLED display. """
        self.timer.init(period=period, mode=Timer.PERIODIC, callback=self.display_status)

    def stop_display_timer(self):
        """ Stop the display update timer. """
        self.timer.deinit()

    def custom_message(self, message, x=0, y=0, max_chars_per_line=16, line_height=10):
        """ Display a custom message that wraps across multiple lines. """
        self.oled.fill(0)  # Clear the display

        # Split message into words to handle line wrapping
        words = message.split()
        current_line = ""
        current_y = y

        for word in words:
            # Check if adding the word exceeds max line length
            if len(current_line) + len(word) + 1 <= max_chars_per_line:
                if current_line:
                    current_line += " "
                current_line += word
            else:
                # Display the current line and start a new line
                self.oled.text(current_line, x, current_y)
                current_y += line_height
                current_line = word  # Start the new line with the current word

            # If the next line exceeds the display height, break
            if current_y >= self.oled.height:
                break

        # Display the last line
        if current_line:
            self.oled.text(current_line, x, current_y)

        self.oled.show()
        #time.sleep(0.5)


    def start_continuous_message(self, message, x=0, y=0):
        """ Continuously display a message at a specific location until commanded to stop. """
        self.continue_display = True
        if self.continue_display:
            # Clear the specific area for continuous message
            self.oled.fill_rect(x, y, self.oled.width, 10, 0)

            # Display the continuous message at the specified coordinates
            self.oled.text(message, x, y)
            self.oled.show()

            #time.sleep(0.5)



    def stop_continuous_message(self):
        """ Stop the continuous message display. """
        self.continue_display = False

