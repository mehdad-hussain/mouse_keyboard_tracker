from PyQt5.QtWidgets import QApplication
from ui.dashboard import Dashboard
from utils.db_utils import init_db
from utils.activity_tracker import start_tracking
import sys
import threading

if __name__ == "__main__":
    # Initialize the database and tables before starting the application
    init_db()
    print("Database initialized successfully.")

    # Start tracking mouse clicks, key presses, and active applications
    tracking_thread = threading.Thread(target=start_tracking, daemon=True)
    tracking_thread.start()

    # Start the PyQt application
    app = QApplication(sys.argv)
    window = Dashboard()
    window.show()
    sys.exit(app.exec_())
