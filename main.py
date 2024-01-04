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
        selection = int(input(prompt))
        if selection >=1 and selection <= 5:
            self.select_object(selection-1)
            self.take_turn()
        else:
            if self.guess_code(selection):
                print("Succesful attempt")
            elif self.attempts <3 :
                print(f'your attempt was wrong and left attempts are:{self.attempts}/3')
                self.take_turn()
            else:
                print("Game over you went of the the Guess. Better Luck next time.")

    def get_room_prompt(self):
        prompt = "Enter the 3 digit lock code or choose an item to interact with: \n"
        count =0
        for name in self.room.get_game_object_names():
            count+=1
            prompt+=f"{count}: {name} \n"
        return prompt
    
    def select_object(self, index:int):
        selected_object = self.room.game_objects[index]
        prompt = self.get_object_interation_string(selected_object.name)
        interaction = input(prompt)
        clue = self.interact_with_object(selected_object, interaction)
        print(clue)
    
    def get_object_interation_string(self, name):
        return f"How do you want to interact with the {name}? \n 1. Look\n 2. Touch\n 3. Smell"

    def interact_with_object(self, object:GameObject, interaction):
        if interaction == "1":
            return object.look()
        elif interaction == "2":
            return object.feel()
        elif interaction == "3":
            return object.sniff()

    def guess_code(self, code: int):
        if self.room.check_code(code):
            return True
        else:
            self.attempts+=1
            return False

game = Game()

game.take_turn()
