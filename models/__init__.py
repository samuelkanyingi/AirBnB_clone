#!/usr/bin/python3
"""This module defines instance of FileStorage class"""
from models.engine.file_storage import FileStorage
storage = FileStorage('file.json')
storage.reload()
