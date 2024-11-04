Here's a `README.md` file for your project. This documentation includes an overview of the project, instructions for setting up the environment, and running the application.

````markdown
# Activity Tracker Dashboard

This project is a cross-platform activity tracker that monitors and logs mouse clicks, keyboard key presses, and tracks active applications and websites. The project is built with Python and PyQt5, and stores data in a local SQLite database.

## Features

-   **Mouse & Keyboard Monitoring**: Tracks total mouse clicks and key presses.
-   **Activity Logging**: Logs recently active applications and visited websites.
-   **UI Dashboard**: Displays real-time data of mouse clicks, key presses, and a log of recent activity with timestamps.

## Requirements

-   **Python 3.7+**
-   **PyQt5** for UI
-   **pynput** for mouse and keyboard tracking
-   **psutil** for application tracking
-   **SQLite** for local data storage

## Project Structure

```plaintext
mouse_keyboard_tracker/
├── db/                         # Database folder
│   └── activity_log.db         # SQLite database file
├── ui/
│   └── dashboard.py            # PyQt5 dashboard code
├── utils/
│   ├── db_utils.py             # Database setup and utility functions
│   └── activity_utils.py       # Utilities for tracking applications and URLs
├── main.py                     # Main application entry point
├── requirements.txt            # Required dependencies
└── README.md                   # Project documentation
```
````

## Installation Guide

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/your-username/repository-name.git
    cd repository-name
    ```

2. **Create a Virtual Environment** (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate          # On Linux/Mac
    venv\Scripts\activate             # On Windows
    ```

3. **Install Dependencies**:

    Install all necessary dependencies from `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

4. **Initialize the Database**:

    Run the following command to initialize the database:

    ```bash
    python -c "from utils.db_utils import init_db; init_db()"
    ```

    This will create the necessary tables for storing mouse/keyboard events and activity logs.

## Usage

To start the activity tracker, simply run:

```bash
python main.py
```

This will open the PyQt5 dashboard, displaying:

-   Total number of mouse clicks and keyboard key presses.
-   A log of recently visited applications and websites.

The dashboard updates every second to show real-time data.

## How It Works

1. **Tracking Mouse and Keyboard Events**:

    - The application uses `pynput` to monitor mouse clicks and key presses. Each event is recorded in the SQLite database.

2. **Application and URL Logging**:

    - `psutil` is used to fetch the currently active window title (application name).
    - URLs are recorded when browsers like Chrome and Firefox are active (as available).

3. **Database Storage**:
    - All activity data is saved in an SQLite database (`activity_log.db`) located in the `db/` folder.
    - The database includes tables for `mouse_keyboard` (events) and `activity_log` (application and URL tracking).

## Files to Note

-   **`main.py`**: The main entry point that initializes the database (if not already initialized) and launches the dashboard.
-   **`ui/dashboard.py`**: Contains the code for the PyQt5 dashboard UI.
-   **`utils/db_utils.py`**: Sets up and manages the SQLite database.
-   **`utils/activity_utils.py`**: Contains functions for application and URL tracking.

## Troubleshooting

1. **Database Errors**: If you see an error related to missing tables, ensure you have run the `init_db()` function as described above to initialize the database.

2. **Platform-Specific Issues**: Some features like URL tracking may behave differently depending on the OS and the browser being used.
