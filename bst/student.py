class Student:
    def __init__ (self, last, first, ssn, email, age):
        self.mLast = last
        self.mFirst = first
        self.mSSN = ssn
        self.mEmail = email
        self.mAge = age
    
    def __eq__(self, rhs):
        return self.getSSN() == rhs.getSSN()