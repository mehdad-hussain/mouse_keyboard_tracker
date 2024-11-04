from PyQt5.QtWidgets import QVBoxLayout, QLabel, QListWidget, QListWidgetItem, QWidget
from PyQt5.QtCore import QTimer
import sqlite3
import os

# Path to the SQLite database
DB_PATH = "db/activity_log.db"

class Dashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Activity Tracker Dashboard")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        
        # Labels for displaying the count of mouse clicks and key presses
        self.click_count_label = QLabel("Mouse Clicks: 0")
        self.keypress_count_label = QLabel("Key Presses: 0")
        self.layout.addWidget(self.click_count_label)
        self.layout.addWidget(self.keypress_count_label)
        
        # List widget for displaying the activity log (applications and websites)
        self.activity_log_list = QListWidget()
        self.layout.addWidget(self.activity_log_list)

        # Initial updates for counts and activity log
        self.update_counts()
        self.update_activity_log()

        # Timer to update counts and activity log every second
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_counts)
        self.timer.timeout.connect(self.update_activity_log)
        self.timer.start(1000)

    def update_counts(self):
        """Updates the counts of mouse clicks and key presses."""
        try:
            with sqlite3.connect(DB_PATH) as conn:
                cursor = conn.cursor()
                
                # Retrieve mouse click count
                cursor.execute("SELECT COUNT(*) FROM mouse_keyboard WHERE event_type = 'mouse_click'")
                mouse_clicks = cursor.fetchone()[0]
                self.click_count_label.setText(f"Mouse Clicks: {mouse_clicks}")
                
                # Retrieve key press count
                cursor.execute("SELECT COUNT(*) FROM mouse_keyboard WHERE event_type = 'key_press'")
                key_presses = cursor.fetchone()[0]
                self.keypress_count_label.setText(f"Key Presses: {key_presses}")
        except sqlite3.OperationalError:
            # If the table doesn't exist, display a warning message
            self.click_count_label.setText("Mouse Clicks: N/A (DB Error)")
            self.keypress_count_label.setText("Key Presses: N/A (DB Error)")

    def update_activity_log(self):
        """Updates the activity log with the most recent applications and websites."""
        self.activity_log_list.clear()
        try:
            with sqlite3.connect(DB_PATH) as conn:
                cursor = conn.cursor()
                
                # Retrieve recent application and website logs, limited to the 10 most recent entries
                cursor.execute("SELECT application, url, timestamp FROM activity_log ORDER BY timestamp DESC LIMIT 10")
                logs = cursor.fetchall()
                
                # Populate the activity log list with the retrieved entries
                for app, url, timestamp in logs:
                    url_display = url if url else "N/A"
                    item_text = f"{timestamp} - {app} ({url_display})"
                    self.activity_log_list.addItem(QListWidgetItem(item_text))
        except sqlite3.OperationalError:
            # If the table doesn't exist, display an error message in the list
            self.activity_log_list.addItem("Error: Unable to fetch activity log. Database may be uninitialized.")
