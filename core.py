
import requests
import time
import os

def adaptive_download(url, filename, delay=0.5, chunk_size=1024):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    r = requests.get(url, stream=True)
    with open(filename, "wb") as f:
        for chunk in r.iter_content(chunk_size=chunk_size):
            if chunk:
                f.write(chunk)
                time.sleep(delay)
    return "Download completed"
