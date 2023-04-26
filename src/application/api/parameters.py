class Parameters:

    def __init__(self, q="", sort=None, order=None, per_page=None, page=None) -> None:
        self._sort = sort
        self._order = order
        self._page = page
        self._q = q
        self._per_page = per_page

    # Sorting params are (stats, forks, help-wanted-issues, updates)
    def set_sort(self, sort: str) -> 'Parameters':
        """
        Args: sort (str): Enter sorting params. Select on of: "stats", "forks", "help-wanted-issues", "updates".
        """
        self._sort = sort
        return self

    # Order params are (desc, asc)
    def set_order(self, order: str) -> 'Parameters':
        """
        Args: order (str): Type "desc" or "asc" for ordering.
        """
        self._order = order
        return self

    def set_per_page(self, per_page: int) -> 'Parameters':
        """
        Args: page (int): Enter number of repos on page. Max value is "100".
        """
        self._per_page = per_page
        return self

    # Page param is number of page
    def set_page(self, page: int) -> 'Parameters':
        """
        Args: page (int): Enter page number to show
        """
        self._page = page
        return self

    # "q" param query contains one ore more search keywords and qualifiers
    def set_q(self, q: str) -> 'Parameters':
        """
        Args: q (str): Required parameter. Example: q=tetris+language:assembly
        """
        self._q = q
        return self

    def build(self) -> dict:
        """
        Returns: (dict): Building object of parameters
        """
        params_dict = {}
        if self._q != "":
            params_dict["q"] = self._q
        if self._sort != None:
            params_dict["sort"] = self._sort
        if self._order != None:
            params_dict["order"] = self._order
        if self._page != None:
            params_dict["page"] = self._page
        if self._per_page != None:
            params_dict["per_page"] = self._per_page
        return params_dict
