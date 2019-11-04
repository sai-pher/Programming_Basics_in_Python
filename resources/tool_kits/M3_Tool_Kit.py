# TODO: Write Milestone 3 tool kit
from typing import List, Tuple


class Person:
    # Instance variable type annotations.
    # These do not define the variable, only provide a suggestion for what the type should be
    #   to allow the developer to know how to work with the variable.
    #
    # This also allows us to "predefine" our instance variables
    #   and gives our code clearer structure
    __contact: List[Tuple[str, int]]
    __name: str
    __age: int
    __gender: str

    # Constructor definition with type annotation for clarity
    def __init__(self, name: str, age: int, gender_num: int):
        """
        The constructor method for the person class to instantiate a new person object.

        :param name: The name of a given person
        :param age: The age of a given person
        :param gender_num: An int indicating the gender of a new person.
                            0 is female, 1 is male, and all else is other.
        """
        self.__name = name
        self.__age = age

        if gender_num == 0:
            self.__gender = "female"
        elif gender_num == 1:
            self.__gender = "male"
        else:
            self.__gender = "other"

        self.__contacts = list()

    def get_age(self):
        return self.__age

    def get_gender(self):
        return self.__gender

    def add_contact(self, name: str, number: int):
        self.__contacts.append((name, number))

    def show_contacts(self) -> str:
        """
        Method to show contacts of each person object.
        :return: A list of the contacts as a string.
        """
        if self.__contacts.__len__() == 0:
            return "Sorry. i have no contacts."
        else:
            contacts = ""
            for contact in self.__contacts:
                contacts += "{} : {}\n".format(contact[0], contact[1])

            return "My contacts are:\n{}".format(contacts)


# ==================================================================

group = list()


def add_person(group_list, name, age, gender):
    new_person = Person(name=name, age=age, gender_num=gender)
    group_list.append(new_person)


def avg_age(group_list):
    sums = 0

    for i in group_list:
        sums += i.get_age()

    avg = sums / len(group_list)
    return avg


add_person(group, "red", 10, 0)
add_person(group, "rde", 12, 0)
add_person(group, "ree", 14, 1)
add_person(group, "rdd", 17, 1)

print(avg_age(group))
