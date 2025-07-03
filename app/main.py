class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self

    def __repr__(self) -> None:
        return f"Person(name={self.name!r}, age={self.age!r})"


def create_person_list(people_list: list) -> list:
    Person.people.clear()

    instances = [
        Person(
            name=person_data["name"],
            age=person_data["age"]
        )
        for person_data in people_list
    ]

    for person_data in people_list:
        person = Person.people[person_data["name"]]

        wife_name = person_data.get("wife")
        if wife_name:
            person.wife = Person.people[wife_name]

        husband_name = person_data.get("husband")
        if husband_name:
            person.husband = Person.people[husband_name]

    return instances
