"""
DSC 20 HW 07 OOP
NAME: XING HONG
PID: A15867895
"""

## Question 2 ##

NO_PENDING_MSG = "No pending assignments to grade!"
INVALID_ASSGN_MSG = "Submission has invalid assignment name!"


def doctests_go_here():
    """
    Since this question involves class interaction, we decided to put all
    doctests together for your benefit.

    The idea of these doctest is to simulate the operation of the whole
    system of classes. If your are successful in this regard you will get
    full points from style. You should add (at least) three doctests for
    each function you defined.

    >>> s1 = Student("fan", "yUXUAN", 2)
    >>> s2 = Student("Bati", "aRdA", 5)
    >>> s3 = Student("Nakahara", "Etsu", 4)
    >>> s4 = Student("Ozberkman", "Nabi", 4)

    >>> print(s2)
    ID: 2; Bati, Arda; Graduate student
    >>> s2.get_name()
    'Bati, Arda'
    >>> s1.get_id()
    1
    >>> s3.get_level()
    'Senior'

    >>> b1 = Submission(s3, "hw1", "Line1\\nLine2")
    >>> b2 = Submission(s3, "hw2", "Line1\\nLine2\\nLine3")
    >>> b3 = Submission(s4, "hw2", "AAAAAAAAAAAAAAAAAAA")
    >>> print(b2)
    Submission #2
    Name: Nakahara, Etsu
    Assignment: HW2
    Score: Pending
    Content:
    Line1
    Line2
    Line3

    >>> c1 = Course("dsc 20")
    >>> c2 = Course("DsC 30")
    >>> _, __ = c1.enroll_student(s1), c2.enroll_student(s4)
    >>> _, __ = c1.enroll_student(s2), c2.enroll_student(s2)
    >>> _, __ = c1.enroll_student(s3), c2.enroll_student(s3)
    >>> print(c2)
    Course name: DSC 30
    Students Enrolled: (3 students in total)
    ID: 4; Ozberkman, Nabi; Senior student
    ID: 2; Bati, Arda; Graduate student
    ID: 3; Nakahara, Etsu; Senior student

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++

    """
    return


class Student:
    """
    Implementation of student.
    """
    STR_LEVEL = ["", "Freshmen", "Sophomore", "Junior", "Senior", "Graduate"]
    count = 1

    ## Question 2.1.2 (A) ##
    def __init__(self, lastname, firstname, level):
        """
        Constructor of Student.

        Requirement:
        Input validation

        Parameters:
        lastname (str): Last name of student. After initialization, the first
                        letter should be in uppercase while other letters are
                        all in lowercase. This string must have at least 2
                        characters.
        firstname (str): First name of student. After initialization, the first
                        letter should be in uppercase while other letters are
                        all in lowercase. This string must have at least 2
                        characters.
        level (int): Class level of student.
                     1 - Freshmen, 2 - Sophomore,
                     3 - Junior, 4 - Senior, 5 - Graduate

        Other attributes you need to initialze:
        (1) A student ID (int), ordered by the order of initialization
        (2) A list to record all courses (as Course instance) this
            student enrolled
        (3) A dictionary to record all graded submissions (as Submission
            instance) of this student, with course name (as string) as key
        """
        # YOUR CODE STARTS HERE #
        assert type(lastname) == str
        assert type(firstname) == str
        assert len(lastname) > 1
        assert len(firstname) > 1
        assert level in [1, 2, 3, 4, 5]
        self.ID = Student.count
        Student.count += 1
        self.lastname = lastname.title()
        self.firstname = firstname.title()
        self.level = level

    ## Question 2.1.2 (E) ##
    def __str__(self):
        """String representation (__str__). Do not modify."""
        return "ID: {}; {}; {} student".format(
            self.get_id(), self.get_name(), self.get_level())

    ## Question 2.1.2 (B) ##
    def get_name(self):
        """Get student's name in Lastname, Firstname format."""
        # YOUR CODE STARTS HERE #
        return self.lastname + ', ' + self.firstname

    ## Question 2.1.2 (C) ##
    def get_id(self):
        """Get student's ID."""
        # YOUR CODE STARTS HERE #
        return self.ID

    ## Question 2.1.2 (D) ##
    def get_level(self):
        """Get student's level in string format."""
        # YOUR CODE STARTS HERE #
        return Student.STR_LEVEL[self.level]

    ## Question 2.5.1 (A) ##
    def submit_assignment(self, course, assignment, content):
        """
        Create a submission and submit it to the course only if the
        student enrolled in this course.

        Requirement:
        Input validation

        Parameters:
        course (Course): The course to submit.
        assignment (str): Assignment name of this submission.
        content (str): Content of this submission.

        Returns:
        None
        """
        # YOUR CODE STARTS HERE #

    ## Question 2.6.1 (A) ##
    def overall_grade(self, course):
        """
        Get this student's overall grade in given course as percentage,
        round to 2 decimal places.

        Parameters:
        course (Course): The course to check overall grade.

        Returns:
        (int or float) This student's overall grade in given course as
        percentage, rounded to 2 decimal places. For example: return 94.65
        if overall grade is 94.65%. Return -1 if course not found, or no
        graded submissions under this course.
        """
        # YOUR CODE STARTS HERE #


class Submission:
    """
    Implementation of submission.
    """
    ID = 1
    ## Question 2.2.2 (A) ##

    def __init__(self, student, assignment, content):
        """
        Constructor of Submission.

        Requirement:
        Input validation

        Parameters:
        student (Student): Student that created this submission.
        assignment (str): Assignment name this submission belongs to. After
                          initialization, this string should be all capitalized.
        content (str): Content of this submission.

        Other attributes you need to initialze:
        (1) The score of this assignment (int or float), initialize it to
            -1, which stands for not graded (pending).
        (2) A submission ID (int), ordered by the order of initialization
        """
        # YOUR CODE STARTS HERE #
        self.student = student
        self.score = -1
        self.ID = Submission.ID
        Submission.ID += 1
        self.assignment = assignment.upper()
        self.content = '\n'.join(content.split('\\n'))

    ## Question 2.2.2 (B) ##
    def __str__(self):
        """String representation (__str__). Do not modify."""
        return "\n".join([
            "Submission #{}".format(self.ID),
            "Name: {}".format(self.student.get_name()),
            "Assignment: {}".format(self.assignment),
            "Score: {}".format(
                (lambda g: "Pending" if g < 0 else g)(self.score)),
            "Content:",
            self.content])


class Course:
    """
    Implementation of course.
    """

    ## Question 2.3.2 (A) ##
    def __init__(self, name):
        """
        Constructor of Course.

        Requirement:
        Input validation

        Parameters:
        name (str): Name of the course. After initialization, this string
                    should be all capitalized. This string must have at least 2
                    characters.

        Other attributes you need to initialze:
        (1) A list to record all students (as Student instances) that enrolled
            in this class
        (2) A list to accept all submissions (as Submission instances) from
            students that are pending a grade
        (3) A dictionary to record all assignments created and their maximum
            score
        (4) A dictionary to record all graded submissions of all assignments
        """
        # YOUR CODE STARTS HERE #
        self.students = []

    ## Question 2.3.2 (B) ##
    def __str__(self):
        """String representation (__str__). Do not modify."""
        join_list = [
            "Course name: {}".format(self.name),
            "Students Enrolled: ({} students in total)".format(
                len(self.students))
        ]
        join_list += list(map(str, self.students))
        return "\n".join(join_list)

    ## Question 2.3.2 (C) ##
    def add_assignment(self, assignment_name, full_score):
        """
        Add assignment to the course.

        Requirement:
        Input validation

        Parameters:
        assignment_name (str): Name of assignment
        full_score (int): Full score of assignment

        Returns:
        None
        """
        # YOUR CODE STARTS HERE #

    ## Question 2.5.2 (A) ##
    def enroll_student(self, student):
        """
        Enroll student to this course.

        Requirement:
        Input validation

        Parameters:
        student (Student): Student to enroll

        Returns:
        None
        """
        # YOUR CODE STARTS HERE #

    ## Question 2.5.2 (B) ##
    def peak_pending(self):
        """
        Print the content of the first pending submission. See write-up
        for details.

        Returns:
        None
        """
        # YOUR CODE STARTS HERE #

    ## Question 2.5.2 (C) ##
    def grade_pending(self, score):
        """
        Grade the first pending submission. See write-up for details.

        Requirement:
        Input validation

        Parameters:
        score (int or float): Score assigned to this assignment. Cannot
                              exceed the full score of this assignment.

        Returns:
        (boolean) True if graded submission is successfully send back to
        student, False otherwise.
        """
        # YOUR CODE STARTS HERE #

    ## Question 2.6.2 (A) ##
    def get_assignment_avg(self, assignment_name):
        """
        Get the average score of graded submissions of given assignment.
        Round to 2 decimal places.

        Requirement:
        Input validation

        Parameters:
        assignment_name (str): Name of assignment

        Returns:
        (int or float)The average score of graded submissions of given
        assignment, rounded to 2 decimal places. Return -1 if assignment not
        found, or no graded submissions under this assignment.
        """
        # YOUR CODE STARTS HERE #
