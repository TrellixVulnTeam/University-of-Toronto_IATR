a = SuperDuperManager()
    a.add_vehicle('Car', 'bmw', 20)
    a.add_vehicle('Helicopter', 'heiying', 20)
    a.add_vehicle('UnreliableMagicCarpet', 'alading', 20)

    print('original positions')
    print(a.get_vehicle_position('bmw'))
    print(a.get_vehicle_position('heiying'))
    print(a.get_vehicle_position('alading'))

    print('original fuels')
    print(a.get_vehicle_fuel('bmw'))
    print(a.get_vehicle_fuel('heiying'))
    print(a.get_vehicle_fuel('alading'))

    # first move
    a.move_vehicle('bmw', 6, 6)
    a.move_vehicle('heiying', 6, 6)
    a.move_vehicle('alading', 6, 6)

    # get positions and fuels
    print('after #1 positions')
    print(a.get_vehicle_position('bmw'))
    print(a.get_vehicle_position('heiying'))
    print(a.get_vehicle_position('alading'))

    print('after #1 fuels')
    print(a.get_vehicle_fuel('bmw'))
    print(a.get_vehicle_fuel('heiying'))
    print(a.get_vehicle_fuel('alading'))

    # second move
    a.move_vehicle('bmw', 20, 20)
    a.move_vehicle('heiying', 20, 20)
    a.move_vehicle('alading', 20, 20)

    # get positions and fuels
    print('after #2 positions')
    print(a.get_vehicle_position('bmw'))
    print(a.get_vehicle_position('heiying'))
    print(a.get_vehicle_position('alading'))

    print('after #2 fuels')
    print(a.get_vehicle_fuel('bmw'))
    print(a.get_vehicle_fuel('heiying'))
    print(a.get_vehicle_fuel('alading'))
