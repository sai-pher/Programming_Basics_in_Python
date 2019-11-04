from typing import *


class Student:
    __name: str
    __gender: str
    __age: int
    __record: Dict[str:int]

    def __init__(self, name: str, age: int, gender_num: int) -> None:
        self.__name = name
        self.__age = age
        if gender_num == 0:
            self.__gender = "Female"
        elif gender_num == 1:
            self.__gender = "Male"
        else:
            self.__gender = "Other"

    def get_age(self) -> int:
        return self.__age

    def get_name(self) -> str:
        return self.__name

    def get_gender(self) -> str:
        return self.__gender

    def get_test_score(self, test_name):
        if test_name in self.__record:
            return self.__record[test_name]
        else:
            return 0

    def generate_reportcard(self) -> str:
        if len(self.__record) < 1:
            return "Nothing to report"

        reportcard = "Test       ||      score       ||\n"

        for k, v in self.__record:
            reportcard += "{}       ||      {}      ||\n".format(k, v)

        return reportcard

    def add_score(self, test_name: str, test_score: int):
        self.__record[test_name] = test_score

    def avg_score(self):
        avg: float = 0
        for k, v in self.__record:
            avg += v

        avg = avg / len(self.__record)

        return avg
