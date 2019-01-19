
class ConsList(object):

    element = None
    next_cons = None

    def __init__(self, element=None, next_cons=None):
        self.element = element
        self.next_cons = next_cons

    def __str__(self):
        
        if self.is_empty():
            return "()"

        s = ""
        constmp = self
        while type(constmp) != NoneConsList:
            s += " " + str(constmp.car())
            constmp = constmp.cdr()

        s = "(" + s[1:] + ")"
        return s

    def is_empty(self):
        return False

    def prepend(self, element):
        return ConsList(element=element, next_cons=self)

    def append(self, element):
        if self.is_empty():
            return ConsList(element=element, next_cons=ConsFactory.nil())
            
        return ConsList(element=self.element, next_cons=self.next_cons.append(element))

    def size(self):
        if self.next_cons is None:
            return 1

        return 1 + self.next_cons.size()

    def car(self):
        return self.element

    def cdr(self):
        return self.next_cons

    def map(self, function):
        return ConsList(element=function(self.element), next_cons=self.next_cons.map(function))

    def filter(self, function):
        
        if function(self.element):
            return ConsList(element=self.element, next_cons=self.next_cons.filter(function))
        else:
            return self.next_cons.filter(function)

    def contains(self, function):
        return True if function(self.element) else self.next_cons.contains(function)


class NoneConsList(ConsList, object):

    def __init__(self):
        super(NoneConsList, self).__init__(self)

    def __str__(self):
        return "()"

    def is_empty(self):
        return True
    
    def size(self):
        return 0

    def prepend(self, element):
        return ConsList(element=element, next_cons=self)

    def append(self, element):
        return ConsList(element=element, next_cons=self)

    def car(self):
        return None

    def cdr(self):
        return None

    def map(self, fucntion):
        return self

    def filter(self, function):
        return self

    def contains(self, function):
        return False


class ConsFactory(object):

    @staticmethod
    def nil():
        return NoneConsList()

    @staticmethod
    def singleton(element):
        return ConsList(element=element, next_cons=NoneConsList())

    @staticmethod
    def as_list(array):
        cons = ConsFactory.nil()
        for item in array:
            cons = cons.append(item)

        return cons
