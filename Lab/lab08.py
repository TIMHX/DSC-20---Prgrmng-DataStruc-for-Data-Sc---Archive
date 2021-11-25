# Question 1.


class Student:
    """
    Manages student information for any student.
    >>> st1 = Student("Black", "John", 12345, "blackj@ucsd.edu")
    >>> print(st1)
    Black, John -- ID: 12345
    Email Address: blackj@ucsd.edu
    >>> st2 = Student("White", "Ann", 35435, "whitea@rt.edu")
    >>> print(st2)
    White, Ann -- ID: 35435
    Email Address: whitea@rt.edu
    """

    #YOUR CODE IS HERE#
    def __init__(self, lastname, firstname, ID, email):
        self.lastname = lastname
        self.firstname = firstname
        self.ID = ID
        self.email = email
    
    def __str__(self):
        return self.lastname + ', ' + self.firstname + ' -- ID: ' + \
        str(self.ID) + '\n' + 'Email Address: ' + self.email

class DSC_Student(Student):
    """
    DSC_Student inherits from Student. Manages student information
    DSC students specifically. Has the taken_classes method.
    >>> dsc_s1 = DSC_Student("Nabi", "Cool", 98767, "cooln@ucsd.edu")
    >>> print(dsc_s1)
    Nabi, Cool -- ID: 98767
    Email Address: cooln@ucsd.edu
    >>> print(DSC_Student.major)
    DSC
    >>> dsc_s1.taken_classes(["dsc10", "dsc40a", "dsc20"])
    ['dsc10', 'dsc40a', 'dsc20']
    >>> dsc_s1.taken_classes(["dsc10", "dsc40a", "dsc20", "dsc30"])
    ['dsc10', 'dsc40a', 'dsc20', 'dsc30']
    """

    #YOUR CODE IS HERE#
    major = 'DSC'
    
    def __init__(self, lastname, firstname, ID, email):
        Student.__init__(self, lastname, firstname, ID, email)
        self.class_list = []
    
    def taken_classes(self,classes):
        for i in classes:
            if i not in self.class_list:
                self.class_list.append(i)
        return self.class_list


# Question 2.

class DSC_Student_Proud(DSC_Student):
    """
    DSC_Student_Proud inherits from DSC_Student. Manages student information
    for proud DSC students.
    >>> dsc_s2 = DSC_Student_Proud("Nabi", "Cool", 98767, "cooln@ucsd.edu")
    >>> print(dsc_s2)
    Nabi, Cool -- ID: Secret
    Major: DSC
    Email Address: cooln@ucsd.edu
    >>> dsc_s2
    DSC_Student_Proud(Nabi, Cool, DSC, cooln@ucsd.edu), type:class
    """

    #YOUR CODE IS HERE#
    def __str__(self):
        return self.lastname + ', ' + self.firstname + ' -- ID: Secret'+ '\n' \
        + 'Major: ' + self.major + '\n' + 'Email Address: ' + self.email
    def __repr__(self):
        return 'DSC_Student_Proud({0}, {1}, {2}, {3}), type:class'.format(self.lastname \
        , self.firstname, self.major, self.email)

# Question 3.

class DSC_Student_Drop(DSC_Student):
    """
    Inherits from DSC_Student. This class is intended for DSC Students
    that are dropping a course.
    >>> dsc_s1 = DSC_Student_Drop("Nabi", "Cool", 98767, "cooln@ucsd.edu")
    >>> print(dsc_s1)
    Nabi, Cool -- ID: 98767
    Email Address: cooln@ucsd.edu
    >>> print(DSC_Student.major)
    DSC
    >>> dsc_s1.drop("dsc40b")
    'You do not have list of classes'
    >>> dsc_s1.taken_classes(["dsc10", "dsc40a", "dsc20"])
    ['dsc10', 'dsc40a', 'dsc20']
    >>> dsc_s1.taken_classes(["dsc10", "dsc40a", "dsc20", "dsc30"])
    ['dsc10', 'dsc40a', 'dsc20', 'dsc30']
    >>> dsc_s1.drop("dsc30")
    >>> print(dsc_s1.class_list)
    ['dsc10', 'dsc40a', 'dsc20']
    >>> dsc_s1.drop("dsc40b")
    'Class is not in your list'
    """
    #YOUR CODE IS HERE#
    def drop(self, the_class):
        if self.class_list == []:
            return ('You do not have list of classes')
        if the_class not in self.class_list:
            return ('Class is not in your list')
        else:
            self.class_list.remove(the_class)    

# Question 4.


class Address:
    """
    Keeps street name and number in each instance.
    >>> Arda_addr = Address("1 Miramar Street", 3303)
    >>> Arda_addr.street_name
    '1 Miramar Street'
    >>> Arda_addr.number
    3303
    >>> Arda_addr.number = 2222
    >>> print(Arda_addr.get_full_addr())
    Street Name: 1 Miramar Street
    Number: 2222
    """

    #YOUR CODE IS HERE#
    def __init__(self, street, num):
        self.street_name = street
        self.number = num
    def get_full_addr(self):
        return 'Street Name: {0}\nNumber: {1}' \
        .format(self.street_name, self.number)


class WorkAddress(Address):
    """
    Inherits from Address. Used specifically for Work Adresses.
    >>> Marina_addr = WorkAddress("205E")
    >>> Marina_addr.office_number
    '205E'
    >>> Marina_addr.street_name
    'Hopkins Dr'
    >>> Marina_addr.number
    10100
    >>> print(Marina_addr.get_full_addr())
    Street Name: Hopkins Dr
    Number: 10100
    Office No: 205E
    """
    #YOUR CODE IS HERE#
    def __init__(self, office_number, street = 'Hopkins Dr', num = 10100):
        Address.__init__(self, street, num)
        self.office_number = office_number
    def get_full_addr(self):
        return 'Street Name: {0}\nNumber: {1}\nOffice No: {2}' \
        .format(self.street_name, self.number, self.office_number)

class HomeAddress(Address):
    """
    Inherits from Address. Used specifically for Home Adresses.
    >>> Arda_addr = HomeAddress("1 Miramar St.", 3303, "La Jolla")
    >>> print(super(HomeAddress, Arda_addr).get_full_addr())
    Street Name: 1 Miramar St.
    Number: 3303
    >>> print(Arda_addr.get_full_addr())
    Street Name: 1 Miramar St.
    Number: 3303
    City: La Jolla
    """

    #YOUR CODE IS HERE#
    def __init__(self, street, num, city):
        Address.__init__(self, street, num)
        self.city = city
    
    def get_full_addr(self):
        return 'Street Name: {0}\nNumber: {1}\nCity: {2}'\
        .format(self.street_name, self.number, self.city)
