import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import win32print
import win32api

FOLDER_TO_WATCH = r"C:\Users\User\Documents\REI\pasta"

class ImageHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory and event.src_path.lower().endswith(('.png', '.jpg', '.jpeg')):
            print(f"Imagem detectada: {event.src_path}")
            print_file(event.src_path)

def print_file(filepath):
    printer_name = win32print.GetDefaultPrinter()  # ou o nome exato da Fujifilm ASK-300
    print(f"Imprimindo na impressora: {printer_name}")
    
    win32api.ShellExecute(
        0,
        "print",
        filepath,
        None,
        ".",
        0
    )

if __name__ == "__main__":
    observer = Observer()
    event_handler = ImageHandler()
    observer.schedule(event_handler, path=FOLDER_TO_WATCH, recursive=False)
    observer.start()

    print(f"Monitorando pasta: {FOLDER_TO_WATCH}")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
