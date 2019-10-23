from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
# pip install watchdog

import os
import json
import time
from datetime import datetime

class MyHandler(FileSystemEventHandler):
    i = 1
    
    #filename = "test.txt"

    def on_modified(self, event):
        actual_date = datetime.now().strftime("%d.%m.%y_%Hh%Mm%Ss")
        print(actual_date)

        new_name = filename + str(self.i) + "_" + actual_date + ".txt"
        #filename = "test.txt"
        for filename in os.listdir(source_folder):
            file_exists = os.path.isfile(destination_folder + "/" + new_name)
            while file_exists:
                self.i += 1
                new_name = filename + str(self.i) + "_" + actual_date + ".txt"
                file_exists = os.path.isfile(destination_folder + "/" + new_name)

            src = source_folder + "/" + filename
            dest = destination_folder + "/" + new_name
            os.rename(src, dest)

source_folder = "c:/Users/JF/Desktop/Source"
destination_folder = "c:/Users/JF/Desktop/Destination"
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, source_folder, recursive=True)
observer.start()

y = 0
try:
    while True:
        print(y)
        y+=1
        time.sleep(3) 
except KeyboardInterrupt:
    observer.stop()
observer.join()
