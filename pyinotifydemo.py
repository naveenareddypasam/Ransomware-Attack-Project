import pyinotify
import os

WATCHED_DIRECTORY = "/home/naveena/Businessfiles"

class EventHandler(pyinotify.ProcessEvent):
    def process_IN_MODIFY(self, event):
        print(f"File modified: {event.pathname}")

        # Detect if encryption file is changing files
        if event.pathname.endswith(".encrypted"):  # adjust this condition as needed
            print(f"Suspicious encryption activity detected on: {event.pathname}")
            # Take action, such as alerting or stopping the process

# Set up watcher
wm = pyinotify.WatchManager()
notifier = pyinotify.Notifier(wm, EventHandler())
wm.add_watch(WATCHED_DIRECTORY, pyinotify.IN_MODIFY)

print(f"Monitoring changes in directory: {WATCHED_DIRECTORY}")
notifier.loop()

