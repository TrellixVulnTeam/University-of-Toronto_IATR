class Registry:
    """A registry of runners in a 5K race.
    """
    
    CATEGORIES = ["<20", "<30", "<40", ">=40"]
    #    The names of the speed categories
    
    # groups: dict{str: list[string]}
    #    Maps a speed category to a list of the email addresses of runners
    #    in that category

    def __init__(self):
        """ (Registry) -> NoneType
        Initialize a new race registry with no runners entered.
        """
        groups = {}
        for c in CATEGORIES:
            groups[c] = {}

    def registered_in(self, e):
        """ (Registry, str) -> str
        Return the category that the runner with email address e is registered
        in, or the empty string if no one with that email address is registered.
        """
        for c in CATEGORIES:
            if e in groups[c]:
                return c
        return ""
        
    def register(self, e, c):
        """ (Registry, str, str) -> NoneType
        Register a runner with email address e and category c.  If they had
        previously registered, remove them from their old category and register
        them in category c.
        Preconditions:
           c occurs in CATEGORIES
        """
        old_category = self.registered_in(e)
        if old_category:
            groups[old_category].remove(e)
        groups[c] = e

    def category_roster(self, c):
        """ (Registry, str) -> [str]
        Return a list of the email addresses of all the runners registered in
        category c.
        Preconditions:
           c occurs in CATEGORIES
        """
        return groups[c]
    
if __name__ == "__main__":
    harry_rosen = Registry()
    harry_rosen.register("diane", "<40")
    harry_rosen.register("margot", "<30")
    harry_rosen.register("tom", "<30")
    harry_rosen.register("toni", "<20")
    harry_rosen.register("diane", "<30")
    print(harry_rosen.category_roster("<30"))
