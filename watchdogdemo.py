from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

WATCHED_DIRECTORY = "/home/naveena/Businessfiles"

class MonitorHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory:
            return
        print(f"File modified: {event.src_path}")

        # Detect if suspicious file changes are happening
        if event.src_path.endswith(".encrypted"):  # adjust this condition as needed
            print(f"Suspicious encryption activity detected on: {event.src_path}")

observer = Observer()
handler = MonitorHandler()
observer.schedule(handler, path=WATCHED_DIRECTORY, recursive=True)

print(f"Monitoring changes in directory: {WATCHED_DIRECTORY}")
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()

