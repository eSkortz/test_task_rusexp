from database.DatabaseUtils import get_min_max_logistics, get_min_max_delivery


def check(logistics: float, delivery: float) -> int:
    min_logistics, max_logistics = get_min_max_logistics()
    min_delivery, max_delivery = get_min_max_delivery()
    if min_logistics < logistics < max_logistics and \
        min_delivery < delivery < max_delivery:
            return 0
    elif min_logistics < logistics < max_logistics:
        return 3
    elif min_delivery < delivery < max_delivery:
        return 2
    else:
        return 1