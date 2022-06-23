import random


class Die:

    def __init__(self, face_up=3):
        self.value = face_up

    def get_face(self):
        return self.value

    def set_face(self, new_face_up):
        self.value = new_face_up

    def __str__(self):
        return str(self.value)

    def roll(self):
        self.value = random.randint(1, 6)


def main():
    die1 = Die(1)  # instatiation - make an instance of a class
    die2 = Die()
    num_snakes = 0
    num_boxcars = 0

    for num in range(0, 1000):
        die1.roll()
        die2.roll()

        if die1.get_face() == 1 and die2.get_face() == 1:
            num_snakes += 1
        elif die1.get_face() == 6 and die2.get_face() == 6:
            num_boxcars += 1

    print(num_snakes, num_boxcars)





if __name__ == "__main__":
    main()
