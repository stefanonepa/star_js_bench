#!/usr/bin/env python3

# Prepare some data to be rendered


import os
import sys
import json
import random

all_entries = []

def all_files(path="/usr/lib"):
    images = os.listdir(os.path.join(os.path.dirname(__file__), "../data/images/"))
    for root, dirs, files in os.walk(path):
        for f in files:
            full_path = os.path.join(root, f)
            try:
                stat = os.stat(full_path)
            except:
                next
            yield {
                "filename":full_path,
                "size":stat.st_size,
                "uid":stat.st_uid,
                "gid":stat.st_gid,
                "date":stat.st_ctime,
                "color":random.choice(["red", "green", "blue",
                    "orange", "black", "puce", "yellow"]),
                "img":random.choice(images),
                }

print(json.dumps(list(all_files()), indent=1))
