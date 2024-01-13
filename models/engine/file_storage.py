import json
from models.base_model import BaseModel

class FileStorage:
    def __init__(self, file_path):
        self.__file_path = file_path
        self.__objects = {}

    def all(self):
        return self.__objects
    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj
        #print(f"Added instance to instances: {key}")

    def save(self):
        serialized_objects = {}
        for key, value in self.__objects.items():
            serialized_objects[key] = value.to_dict()
            with open(self.__file_path, 'w') as file:
                json.dump(serialized_objects, file)
    def reload(self):
        try:
            with open(self.__file_path,'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    #class_instance = globals()[class_name](**value)
                    class_instance = globals().get(class_name)
                    if class_instance:
                        instance = class_instance(**value)
                        self.__objects[key] = instance
                        #print("Loaded instance from file:", key)
                       # self.__objects[key] = class_instance
        except FileNotFoundError:
            pass
