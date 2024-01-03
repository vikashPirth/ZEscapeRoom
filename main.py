from typing import List

class GameObject:
  
    # Initializing the fields of the class
    def __init__(self, name, appearance, feel, smell):
        self.name = name
        self.appearance = appearance
        self.feel = feel
        self.smell = smell

    # Implementing the methods of our class
    def look(self):
        return f"You look at the {self.name}. {self.appearance}\n"

    def touch(self):
        return f"You touch the {self.name}. {self.feel}\n"

    def sniff(self):
        return f"You sniff the {self.name}. {self.smell}\n"


class Room:

    def __init__(self, escape_code: int, game_objects: List[GameObject]) -> None:
        self.escape_code = escape_code
        self.game_objects= game_objects
    
    def check_code(self, code):
        return self.escape_code == code
    
    def get_game_object_names(self):
        return [game_object.name for game_object in self.game_objects]
     