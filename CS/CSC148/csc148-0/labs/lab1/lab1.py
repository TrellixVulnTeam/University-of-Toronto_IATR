class RaceRegistry:
    """Race Registry includes runners' information

    Attributes:
        @type under_20: list
        emails of under_20 category
        @type under_30: list
        emails of under_30 category
        @type under_40: list
        emails of under_40 category
        @type over_40: list
        emails of over_40 category
    """

    def __init__(self):
        """Creat a RaceRegistry for runners

        @type self: Race_Registry
        @rtype: None
        """

        self.under_20 = []
        self.under_30 = []
        self.under_40 = []
        self.over_40 = []

    def __eq__(self, other):
        """Return True iff this Race_Registry is same as other.

        @type self: Race_Registry
        @type other: Race_Registry
        @rtype: bool

        >>> r1 = RaceRegistry()
        >>> r2 = RaceRegistry()
        >>> r1 == r2
        True
        >>> r1.add('eris@email.utoronto.ca', 'under 20')
        >>> r1 == r2
        False
        """
        self.under_20.sort()
        self.under_30.sort()
        self.under_40.sort()
        self.over_40.sort()
        other.under_20.sort()
        other.under_30.sort()
        other.under_40.sort()
        other.over_40.sort()
        return type(self) == type(other) and \
               self.under_20.sort() == other.under_20.sort() \
               and self.under_30.sort() == other.under_30.sort() \
               and self.under_40.sort() == other.under_40.sort() \
               and self.over_40.sort() == other.over_40.sort()



    def __str__(self):
        """Return readable string representation of this Race_Registry.

        @type self: Race_Registry
        @rtype: None

        >>> r1 = RaceRegistry()
        >>> r1.add('eris@email.utoronto.ca', 'under 20')
        >>> print(r1)
        under 20: [eris@email.utoronto.ca]
        under 30: []
        under 40: []
        over 40: []
        """

        return """under 20: {0}
        under 30: {1}
        under 40: {2}
        over 40:{3}
        """.format(self.under_20, self.under_30, self.under_40, self.over_40)

    def add(self, email, speed_category):
        """add one runner information of email and speed_category \
        to this Race_Registry.

        @type self: Race_Registry
        @type email: str
        @tpye speed_category: str
        @rtype: None

        >>> r = RaceRegistry()
        >>> r.add('gerhard@mail.utoronto.ca', 'under 40')
        >>> r.under_40
        ['gerhard@mail.utoronto.ca']
        """

        if speed_category == 'under 20':
            self.under_20.append(email)
        elif speed_category == 'under 30':
            self.under_30.append(email)
        elif speed_category == 'under 40':
            self.under_40.append(email)
        else:
            self.over_40.append(email)

    def get_runner_cate(self, email):
        """Return runner's category basing on his email.

        @type self: Race_Registry
        @type email: str
        @rtype: str

        >>> r = RaceRegistry()
        >>> r.add('gerhard@mail.utoronto.ca', 'under 40')
        >>> r.get_runner_cate('gerhard@mail.utoronto.ca')
        'under 40'
        """
        if email in self.under_20:
            return 'under 20'

        elif email in self.under_30:
            return 'under 30'
        elif email in self.under_40:
            return 'under 40'
        elif email in self.over_40:
            return 'over 40'


if __name__ == '__main__':
    r = RaceRegistry()
    r.add('gerhard@mail.utoronto.ca', 'under 40')
    r.add('tom@mail.utoronto.ca', 'under 30')
    r.add('jerry@mail.utoronto.ca', 'under 20')
    r.add('haha@mail.utoronto.ca', 'over 40')
    print(r)
    r.get_runner_cate('jerry@mail.utoronto.ca')
