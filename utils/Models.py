from database.DatabaseUtils import get_markup, \
    get_percent_logistics, get_percent_delivery

class Product:
    
    OWN_EXPENSES = 54
    SORTING = 10
    COMISSION_FOR_RETURNS = 15
    EQUIRING = 0.02
    COMISSION_PERCENT = 0.12
    
    sid: int
    category: int
    name: str
    price: float
    loyalty_program: float
    cost_price: float
    markup: int
    
    
    def __init__(self, sid, category, name, price, loaylty_program = 0.01) -> None:
        self.sid = sid
        self.category = category
        self.name = name
        self.price = price
        self.loyalty_program = loaylty_program
        self.cost_price = price + self.OWN_EXPENSES + self.SORTING + self.COMISSION_FOR_RETURNS
        self.markup = get_markup(cost_price=self.cost_price, category=self.category)

    
    def logistics(self) -> float:
        return round(self.cost_price * get_percent_logistics(), 2)
    
    
    def delivery(self) -> float:
        return round(self.cost_price * get_percent_delivery(), 2)