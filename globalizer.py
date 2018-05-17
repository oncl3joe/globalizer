class Globalizer:

    def __setattr__(self, item, value):
        self.__dict__[item] = value

    def __setitem__(self, item, value):
        self.__setattr__(item, value)

    def __getattr__(self, item):
        if not self.__contains__(item):
            self.__dict__[item] = Globalizer()
        return self.__dict__.get(item)

    def __getitem__(self, item):
        return self.__getattr__(item)

    def __delattr__(self, item):
        self.__dict__[item] = None

    def __delitem__(self, item):
        self.__delattr__(item)

    def __contains__(self, item):
        return item in self.__dict__


globalizer = Globalizer()
