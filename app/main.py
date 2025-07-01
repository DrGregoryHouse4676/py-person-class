class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_list: dict) -> Person:
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
            wife_person = Person.people[wife_name]
            person.wife = wife_person
            wife_person.husband = person

        husband_name = person_data.get("husband")
        if husband_name:
            husband_person = Person.people[husband_name]
            person.husband = husband_person
            husband_person.wife = person

    return instances
