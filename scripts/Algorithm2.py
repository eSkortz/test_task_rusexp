def make(cost_price: float,
        comission_for_returns: int,
        comission_percent: float,
        equiring: int,
        flogistics: float,
        delivery_percent: float,
        loyalty_program: float,
        markup: int) -> float:
    sum1 = cost_price / ((100 - comission_for_returns - comission_percent*100 - equiring*100 \
        - delivery_percent*100 - loyalty_program*100)/100)
    sum2 = flogistics / ((100 - comission_for_returns - comission_percent*100 - equiring*100 \
        - delivery_percent*100 - loyalty_program*100)/100)
    sum3 = (100 - (markup / ((100 - comission_for_returns - comission_percent*100 - equiring*100 \
        - delivery_percent*100 - loyalty_program*100) / 100)))/100
    return round((sum1 + sum2) / sum3, 2)