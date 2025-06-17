class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_list: str) -> list:
    instance = []
    Person.people.clear()

    for person_data in people_list:
        person = Person(name=person_data["name"], age=person_data["age"])
        instance.append(person)

    for person_data in people_list:
        person = Person.people[person_data["name"]]

        if "wife" in person_data and person_data["wife"] is not None:
            wife_person = Person.people[person_data["wife"]]
            person.wife = wife_person
            wife_person.husband = person

        if "husband" in person_data and person_data["husband"] is not None:
            husband_person = Person.people[person_data["husband"]]
            person.husband = husband_person
            husband_person.wife = person

    return instance
