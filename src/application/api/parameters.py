class Parameters:

    def __init__(self, sort=None, order=None, page=None, q="") -> None:
        self.__sort = sort
        self.__order = order
        self.__page = page
        self.__q = q

    #Sorting params are (stats, forks, help-wanted-issues, updates)
    def set_sort(self, sort):
        self.__sort = sort
        return self
    
    #Order params are (desc, asc)
    def set_order(self, order):
        self.__order = order
        return self
    
    #Page param is number of page
    def set_page(self, page):
        self.__page = page
        return self
    
    #"q" param query contains one ore more search keywords and qualifiers
    def set_q(self, q):
        self.__q = q
        return self
    
    #Building object of parameters
    def param_build(self):
        params_dict = {}
        if self.__sort != None:
            params_dict["sort"] = self.__sort
        if self.__order != None:
            params_dict["order"] = self.__order
        if self.__page != None:
            params_dict["page"] = self.__page
        if self.__q != "":
            params_dict["q"] = self.__q
        return params_dict


