import sublime
import sublime_plugin
from datetime import datetime, timezone, timedelta

class InsertTimestampCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # Define your desired timezone offset (e.g., GMT+6)
        tz_offset = timedelta(hours=6)

        # Get the current UTC time
        current_time = datetime.now(timezone.utc)

        # Apply the timezone offset
        current_time += tz_offset

        # Format the timestamp as "10th September, 2023 13:08:36"
        formatted_time = current_time.strftime("%dth %B, %Y %H:%M:%S GMT+6")

        # Insert the formatted timestamp at the cursor position
        for region in self.view.sel():
            self.view.insert(edit, region.begin(), formatted_time)
