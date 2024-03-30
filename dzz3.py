import random

class Dialog:
    @staticmethod
    def ask_for_input(message):
        return input(message)

    @staticmethod
    def display_message(message):
        print(message)

class Human:
    def __init__(self, name="Human", job=None, home=None, car=None):
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
            self.to_repair()
            return
        self.job = Job(job_list)

    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
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
                return
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
            Dialog.display_message("I bought fuel")
            self.money -= 100
            self.car.fuel += 100
        elif manage == "food":
            Dialog.display_message("Bought food")
            self.money -= 50
            self.home.food += 50
        elif manage == "delicacies":
            Dialog.display_message("Hooray! Delicious!")
            self.gladness += 10
            self.satiety += 2
            self.money -= 15

    def chill(self):
        self.gladness += 10
        self.home.mess += 5

    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0

    def to_repair(self):
        self.car.strength += 100
        self.money -= 50

    def days_indexes(self, day):
        day = f" Today the {day} of {self.name}'s life "
        Dialog.display_message(f"{day:=^50}" + "\n")
        human_indexes = self.name + "'s indexes"
        Dialog.display_message(f"{human_indexes:^50}" + "\n")
        Dialog.display_message(f"Money – {self.money}")
        Dialog.display_message(f"Satiety – {self.satiety}")
        Dialog.display_message(f"Gladness – {self.gladness}")
        home_indexes = "Home indexes"
        Dialog.display_message(f"{home_indexes:^50}" + "\n")
        Dialog.display_message(f"Food – {self.home.food}")
        Dialog.display_message(f"Mess – {self.home.mess}")
        car_indexes = f"{self.car.brand} car indexes"
        Dialog.display_message(f"{car_indexes:^50}" + "\n")
        Dialog.display_message(f"Fuel – {self.car.fuel}")
        Dialog.display_message(f"Strength – {self.car.strength}")

    def is_alive(self):
        if self.gladness < 0:
            Dialog.display_message("Depression…")
            return False
        if self.satiety < 0:
            Dialog.display_message("Dead…")
            return False
        if self.money < -500:
            Dialog.display_message("Bankrupt…")
            return False

    def live(self, day):
        if self.is_alive() == False:
            return False
        if self.home is None:
            Dialog.display_message("Settled in the house")
            self.get_home()
        if self.car is None:
            self.get_car()
            Dialog.display_message(f"I bought a car {self.car.brand}")
        if self.job is None:
            self.get_job()
            Dialog.display_message(f"I don't have a job, I'm going to get a job {self.job.job} with salary {self.job.salary}")
        self.days_indexes(day)
        action = Dialog.ask_for_input("What do you want to do? (eat, work, chill, clean, shop): ").lower()
        if action == "eat":
            self.eat()
        elif action == "work":
            self.work()
        elif action == "chill":
            self.chill()
        elif action == "clean":
            self.clean_home()
        elif action == "shop":
            self.shopping(manage="delicacies")
        else:
            Dialog.display_message("Invalid action!")

class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption = brand_list[self.brand]["consumption"]
    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            Dialog.display_message("The car cannot move")
            return False

class House:
    def __init__(self):
        self.mess = 0
        self.food = 0

job_list = {
 "Java developer":
 {"salary":50, "gladness_less": 10 },
 "Python developer":
 {"salary":40, "gladness_less": 3 },
 "C++ developer":
 {"salary":45, "gladness_less": 25 },
 "Rust developer":
 {"salary":70, "gladness_less": 1 },
 }
brands_of_car = {
 "BMW":{"fuel":100, "strength":100, "consumption": 6},
 "Lada":{"fuel":50, "strength":40, "consumption": 10},
 "Volvo":{"fuel":70, "strength":150, "consumption": 8},
 "Ferrari":{"fuel":80, "strength":120, "consumption": 14},
 }

class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]

def main():
    nick = Human(name="Nick")
    dialog = Dialog()
    for day in range(1, 800):
        if nick.live(day) == False:
            break

if __name__ == "__main__":
    main()
