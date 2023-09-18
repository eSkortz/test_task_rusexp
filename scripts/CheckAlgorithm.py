from database.DatabaseUtils import get_min_max_logistics, get_min_max_delivery


def check(logistics: float, delivery: float) -> tuple:
    min_logistics, max_logistics = get_min_max_logistics()
    min_delivery, max_delivery = get_min_max_delivery()
    if min_logistics < logistics < max_logistics and \
        min_delivery < delivery < max_delivery:
            return 0, logistics, delivery
    elif min_logistics < logistics < max_logistics:
        if delivery > max_delivery:
            return 3, logistics, max_delivery
        return 3, logistics, min_delivery
    elif min_delivery < delivery < max_delivery:
        if logistics > max_logistics:
            return 2, max_logistics, delivery
        return 2, min_logistics, delivery
    else:
        if logistics > max_logistics and delivery > max_delivery:
            return 1, max_logistics, max_delivery
        elif logistics < min_logistics and delivery < min_delivery:
            return 1, min_logistics, min_delivery
        elif delivery > max_delivery:
            return 1, min_logistics, max_delivery
        return 1, max_logistics, min_delivery