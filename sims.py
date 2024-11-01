import random

class Human:
    def __init__(self, name = "Human", job = None, car = None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.car = car
        self.home = home
    def get_home(self):
        self.home = House()
    def get_car(self):
        self.car = Auto(brands_of_car)
    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_rapair()
            return
        self.job = Job(job_list)
    def eat(self):
        if self.home.food <= 0:
            self.shopping("Food")
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 5

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 4

        def shopping(self, manage):
            if self.car.drive():
                pass
            else:
                if self.car.fuel < 20:
                    manage = "fuel"
                else:
                    self.to_repair()
                    return
            if manage == "fuel":
                print("I bought fuel ")
                self.money -= 100
                self.car.fuel += 100
            elif manage == "food":
                print("bought food")
                self.money -= 50
                self.home.food += 50
            elif manage == "delicacies":
                print("Hooray! Delicacious")
                self.gladness += 10
                self.satiety += 2
                self.money -= 15

        def chill(self):
            self.gladness += 10
            self.home.mess += 5
        def clean_home(self):
            self.gladness -= 5
            self.home.mess += 0

        def to_repair(self):
            self.car.strenght += 100
            self.money -= 50

        def day_indexes(self, day):
            day = f"Today the {day} of {self.name}'s life"
            print(f"{day:=^50}", "\n")
            human_indexes = self.name + "'s indexes"
            print(f"{human_indexes:=^50}", "\n")
            print(f"Money - {self.money}")
            print(f"Satiety - {self.satiety}")
            print(f"Gladness - {self.gladness}")
            home_indexes = "home indexes"
            print(f"{home_indexes:=^50}", "\n")
            print(f"food - {self.food}")
            print(f"mess - {self.home.mess}")
            car_indexes = f" {self.car.brand} + car indexes"
            print(f"{car_indexes:=^50}", "\n")
            print(f"Fuel - {self.car.fuel}")
            print(f"Strenght - {self.car.strenght}")
        def is_alive(self):
            if self.gladness < 0:
                print("Depression...")
                return False
            if self.satiety <= 0:
                print("Dead...")
                return False
            if self.money < -500:
                print("Bankrot...")
                return False

        def live(self, day):
            if self.is_alive() == False:
                return False
            if self.home is None:
                print("Settled in the house")
                self.get_home()
            if self.car is None:
                self.get.car
                print(f"I bought a car {self.car.band}")
            if self.job is None:
                self.get.job()
                print(f"I dont have a job, going to get a job {self.job.job} with salary {self.job.job}")
            self.day_indexes(day)
            dice = random.randint(1, 4)

class Pet:
    def __init__(self, name="Pet"):
        self.name = name
        self.gladness = 50
        self.satiety = 50
        self.home = home

    def get_home(self):
        self.home = House()


    def eat(self):
        if self.home.food <= 0:
            self.shopping("Food")
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 5

    def work(self):
        def chill(self):
            self.gladness += 10
            self.home.mess += 5

        def day_indexes(self, day):
            day = f"Today the {day} of {self.name}'s life"
            print(f"{day:=^50}", "\n")
            pet_indexes = self.name + "'s indexes"
            print(f"{pet_indexes:=^50}", "\n")
            print(f"Satiety - {self.satiety}")
            print(f"Gladness - {self.gladness}")
            print(f"food - {self.food}")

        def is_alive(self):
            if self.gladness < 0:
                print("Depression...")
                return False
            if self.satiety <= 0:
                print("Dead...")
                return False
            if self.money < -500:
                print("Bankrot...")
                return False

        def live(self, day):
            if self.is_alive() == False:
                return False
            if self.home is None:
                print("Settled in the house")
                self.get_home()
            if self.human is None:
                self.get.human()
                print(f"I dont have a human, going to get a human {self.human.human} with salary {self.human.human}")
            self.day_indexes(day)