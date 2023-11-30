
import random

class Teacher(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = [
            "str is a data type in Python",
            "programming is hard, but it's worth it",
            "JavaScript async web request",
            "Python function call definition",
            "object-oriented teacher instance",
            "programming computers hacking learning terminal",
            "pipenv install pipenv shell",
            "pytest -x flag to fail fast",
        ]

    def teach(self):
        # Return a random element from self.knowledge
        random_index = random.randint(0, len(self.knowledge) - 1)
        return self.knowledge[random_index]


class Student(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = []  # Initialize with an empty list

    def learn(self, new_knowledge):
        # Add the provided string to the student's self.knowledge list
        self.knowledge.append(new_knowledge)
