def get_tab_object(tab):
    return tab.currentWidget()


def get_tab_index(tab):
    return tab.indexOf(get_tab_object(tab))


def get_tab_name(tab):
    return tab.tabText(get_tab_index(tab))


def check_exist_filename(self, name):
    if self.fullname.count(name) == 1:
        return True
    else:
        return False
