def check_constraints(grid_file, coordinates_from, coordinates_to, coordinates_destination, nets):
   # Checks if the line doesnt break rules
    size = grid_file.get_size()
    coordinates_gates = grid_file.get_coordinates_gates()
    check = True
    cross = False

    # Checks if line exceeds boundaries
    if coordinates_to[0] > size  or coordinates_to[1] > size or coordinates_to[2] > 7 or coordinates_to[0] < 0 or coordinates_to[1] < 0 or coordinates_to[2] < 0:
        check = False

    list_of_nets = grid_file.get_list_of_nets()

    for i in nets:
        net_from = i.get_coordinates_from()
        net_to = i.get_coordinates_to()

        if coordinates_to == coordinates_destination:
            if coordinates_from == net_from:
                check = False
                return check, cross
        else:
            if coordinates_to == net_from or coordinates_to == net_to:
                cross = True
            if coordinates_from == net_from and coordinates_to == net_to:
                check = False
                return check, cross
            if coordinates_from == net_to and coordinates_to == net_from:
                check = False
                return check, cross
            if coordinates_to in coordinates_gates and coordinates_to != coordinates_destination:
                check = False
                return check, cross

    for i in range(len(list_of_nets)):
        for x in list_of_nets[i]:
            net_from = x.get_coordinates_from()
            net_to = x.get_coordinates_to()

            if coordinates_to == coordinates_destination:
                if coordinates_from == net_from:
                    return check, cross
            else:
                if coordinates_to == net_from or coordinates_to == net_to:
                    cross = True
                if coordinates_from == net_from and coordinates_to == net_to:
                    check = False
                    return check, cross
                elif coordinates_from == net_to and coordinates_to == net_from:
                    check = False
                    return check, cross
                elif coordinates_to in coordinates_gates and coordinates_to != coordinates_destination:
                    check = False
    
    return check, cross