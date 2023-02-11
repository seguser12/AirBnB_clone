#!/usr/bin/python3
'''models __init__'''

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
