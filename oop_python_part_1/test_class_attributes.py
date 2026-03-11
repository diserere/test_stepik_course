from icecream import ic


class Car:
    number_of_wheels = 4
    cars_produced = 0

    def __init__(self, model: str, color: str, year: int):
        self.model: str = model
        self.color: str = color
        self.year: int = year
        self.is_engine_on: bool = False
        print(f"car {self.model} created")

        Car.cars_produced += 1

    def start_engine(self):
        self.is_engine_on = True
        print(f"{self.model} is started!")


def header(text: str, n: int = 4) -> None:
    symbol = "-"
    print(f"\n{symbol * n}[ {text} ]\n")


def main():

    header("INIT")
    ic(Car.cars_produced)
    car_1 = Car("BMW", "black", 2022)
    ic(Car.cars_produced)
    car_2 = Car("Audi", "white", 2021)
    ic(Car.cars_produced)

    header("DO CAHANGES")
    car_2.start_engine()
    ic(Car.cars_produced)
    car_1.cars_produced = 100500
    ic(car_1.cars_produced)
    ic(Car.cars_produced)
    car_3 = Car("Threecycle", "red", 2020)
    car_3.number_of_wheels = 3
    ic(Car.cars_produced)

    header("LIST")
    for car in (car_1, car_2, car_3):
        print(
            f"{car.model} is {car.color}, has {car.number_of_wheels} wheels and was produced in {car.year}; engine started: {car.is_engine_on}"
        )
        print(f"- On {car.model}: cars_produced: {car.cars_produced}")

    header("TOTAL")
    print(f"Total cars produced: {Car.cars_produced}")


if __name__ == "__main__":
    main()
