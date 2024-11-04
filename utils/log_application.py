import psutil
import time
from utils.db_utils import log_application
from psutil import NoSuchProcess

def track_active_window():
    previous_title = None
    while True:
        try:
            active_window = psutil.Process(psutil.Process().ppid())
            active_title = active_window.name()
            
            # Check if the application is a browser (Chrome, Firefox)
            if 'chrome' in active_title.lower() or 'firefox' in active_title.lower():
                # Retrieve browser title (contains the URL or website title)
                browser_url = active_window.cmdline()[-1] if active_window.cmdline() else None
                if browser_url and browser_url != previous_title:
                    log_application("Browser", browser_url)
                    previous_title = browser_url
            else:
                # Log other applications
                if active_title != previous_title:
                    log_application(active_title)
                    previous_title = active_title
        except NoSuchProcess:
            pass
        time.sleep(1)
