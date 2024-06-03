#!/usr/bin/env python

from user import User

import random

class Teacher(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = self.generate_knowledge()

    def generate_knowledge(self):
        # Generate some initial knowledge for the teacher
        knowledge = ["Subject A", "Subject B", "Subject C"]
        return knowledge
    
    def teach(self):
        # Randomly select a topic from the teacher's knowledge
        topic = random.choice(self.knowledge)
        return topic