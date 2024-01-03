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
    

class Game:

    def __init__(self) -> None:
        self.attempts = 0
        objects = self.create_objects()
        self.room = Room(731, objects)
    
    def create_objects(self):
        return [
          GameObject(
            "Sweater",
            "It's a blue sweater that had the number 12 switched on it.",
            "Someone has unstitched the second number, leaving only the 1.",
            "The sweater smells of laundry detergent."),
          GameObject(
            "Chair", 
            "It's a wooden chair with only 3 legs.",
            "Someone had deliberately snapped off one of the legs.",
            "It smells like old wood."),
          GameObject(
            "Journal",
            "The final entry states that time should be hours then minutes then seconds (H-M-S).",
            "The cover is worn and several pages are missing.",
            "It smells like musty leather."),
          GameObject(
            "Bowl of soup", 
            "It appears to be tomato soup.",
            "It has cooled down to room temperature.",
            "You detect 7 different herbs and spices."),
          GameObject(
            "Clock", 
            "The hour hand is pointing towards the soup, the minute hand towards the chair, and the second hand towards the sweater.",
            "The battery compartment is open and empty.",
            "It smells of plastic."),
        ]
    
    def take_turn(self):
        prompt  = self.get_room_prompt()
        selection = input(prompt)
        print(selection) 
    
    def get_room_prompt(self):
        prompt = "Enter the 3 digit lock code or choose an item to interact with: \n"
        count =0
        for name in self.room.get_game_object_names():
            count+=1
            prompt+=f"{count}: {name} \n"
        return prompt

game = Game()

game.take_turn()
