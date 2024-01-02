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

