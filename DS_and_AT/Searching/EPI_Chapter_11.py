import collections
from typing import Tuple, List , Callable
import bisect

Student = collections.namedtuple("Student",('gpa','name'))

def comp_gpa(student : Student ) -> Tuple[float, str]:
    return (-student.gpa, student.name)

def search_student(students : List[Student], target : Student,
                    comp_gpa : Callable[[Student], Tuple[float, str]]):
    
    i = bisect.bisect_left([comp_gpa(s) for s in students], comp_gpa(target))

    return 0 <= i < len(students) and students[i] == target

students = [Student(gpa,name) for gpa, name in zip([1,2,3,4],"abcd")]
print(search_student(students,Student(1, 'a'),comp_gpa))

