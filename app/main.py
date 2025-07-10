class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self

    def __repr__(self) -> None:
        return f"Person(name=\'{self.name}\', age={self.age})"


def create_person_list(people: list) -> list:
    Person.people.clear()

    for person in people:
        Person(person["name"], person["age"])

    for person in people:
        current_person = Person.people[person["name"]]

        wife_name = person.get("wife")
        if wife_name and wife_name in Person.people:
            current_person.wife = Person.people[wife_name]

        husband_name = person.get("husband")
        if husband_name and husband_name in Person.people:
            current_person.husband = Person.people[husband_name]

    return [Person.people[person["name"]] for person in people]
