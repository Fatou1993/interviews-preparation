class Name :
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __eq__(self, other):
        return self.first_name == other.first_name and self.last_name == other.last_name

    def __lt__(self, other):
        return self.first_name < other.first_name \
                if self.first_name != other.first_name \
                else self.last_name < other.last_name


def eliminate_duplicates(names):
    names.sort()
    writing_idx = 1
    for name in names[1:] : #be careful here
        if name != names[writing_idx-1]:
            names[writing_idx] = name
            writing_idx+=1
    del names[writing_idx:]