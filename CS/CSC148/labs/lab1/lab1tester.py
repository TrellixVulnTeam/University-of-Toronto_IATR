if __name__ == '__main__':
    from lab1 import RaceRegistry
    r1 = RaceRegistry()
    r1.add('gerhard@mail.utoronto.ca', 'under 40')
    r1.add('tom@mail.utoronto.ca', 'under 30')
    r1.add('toni@mail.utoronto.ca', 'under 20')
    r1.add('margot@mail.utoronto.ca', 'under 30')
    r1.add('gerhard@mail.utoronto.ca', 'under 30')
    print(r1.under_30)

