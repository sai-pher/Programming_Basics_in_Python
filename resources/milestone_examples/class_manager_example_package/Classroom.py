from typing import *

from resources.milestone_examples.class_manager_example_package import Student


class Classroom:
    """Instance variable"""
    #   Using type annotation with access level `__` modifier for clarity
    __class_list: Dict[str:Student]
    __class_names_list: List[str]
    __class_test_list: List[str]
    __class_size: int
    __class_name: str

    """Constructor"""

    def __init__(self, class_name):
        # actual definition of instance variables made using `self` key word
        self.__class_name = class_name
        self.__class_list = dict()
        self.__class_names_list = list()
        self.__class_test_list = list()
        self.__class_size = 0

    """Accessor Methods"""

    def get_class_list(self):
        return self.__class_list

    def get_class_name_list(self):
        return self.__class_names_list

    def get_class_test_list(self):
        return self.__class_test_list

    def get_class_size(self):
        return self.__class_size

    def get_class_name(self):
        return self.__class_name

    """Unique methods"""

    def add_student(self, student: Student):
        self.__class_list[student.get_name()] = student
        self.__class_names_list.append(student.get_name())
        self.__class_size += 1

    def remove_student(self, student_name: str):
        if student_name in self.__class_list:
            del self.__class_list[student_name]
            self.__class_names_list.remove(student_name)
            self.__class_size -= 1

    def add_student_test_score(self, student_name: str, test_name: str, test_score: int):
        if student_name in self.__class_list:
            self.__class_list[student_name].add_score(test_name, test_score)

    def add_all_test_scores(self, test_name: str, test_scores: Dict[str:int]):
        self.__class_test_list.append(test_name)
        for name, score in test_scores:
            self.add_student_test_score(name, test_name, score)

    def generate_all_reportcards(self):
        reportcard_dict: Dict[str:str] = dict()

        for name, student in self.__class_list:
            reportcard_dict[name] = student.generate_reportcard()

        return reportcard_dict

    def test_avg(self, test_name):
        avg = 0

        for name, student in self.__class_list:
            avg += student.get_test_score(test_name)

        avg = avg / self.__class_size
        return avg

    def all_test_avgs(self):

        test_avgs = list()

        for test in self.__class_test_list:
            test_avgs.append(self.test_avg(test))

        return test_avgs

    def class_avg(self):
        avg = 0

        for name, student in self.__class_list:
            avg += student.avg_score()

        avg = avg / self.__class_size
        return avg

    """Utility methods"""

    def __str__(self):
        class_info = "Class Name: {}\n" \
                     "Class Size: {}\n" \
                     "tests Written: {}\n".format(self.__class_name,
                                                  self.__class_size,
                                                  len(self.__class_test_list))
        return class_info
