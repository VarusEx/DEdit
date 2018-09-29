from os import path


def get_tab_object( tab):
    current = tab.currentWidget()
    return current


def get_tab_index(self, tab):
    index = tab.indexOf(self.get_tab_object())
    return index


def get_tab_name(self, tab):
    name = tab.tabText(self.get_tab_index())
    return name


def check_exist_filename(self, name):
    if self.fullname.count(name) == 1:
        return True
    else:
        return False


def find_way_to_file(self, file):
    base = path.abspath(path.join(self.basepath, file))
    return base
