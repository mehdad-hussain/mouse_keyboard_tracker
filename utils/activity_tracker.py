import keyboard
import mouse
from utils.db_utils import log_event, log_application
import threading
import psutil
import time
from psutil import NoSuchProcess


def track_mouse_clicks():
    mouse.on_click(lambda: log_event("mouse_click"))

def track_key_presses():
    keyboard.on_press(lambda _: log_event("key_press"))

def track_active_window():
    previous_application = None
    while True:
        try:
            active_app = psutil.Process(psutil.Process().ppid()).name()
            if active_app != previous_application:
                log_application(active_app)
                previous_application = active_app
        except NoSuchProcess:
            pass
        time.sleep(1)

def start_tracking():
    threading.Thread(target=track_mouse_clicks, daemon=True).start()
    threading.Thread(target=track_key_presses, daemon=True).start()
    threading.Thread(target=track_active_window, daemon=True).start()
