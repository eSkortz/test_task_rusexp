from scripts.CheckAlgorithm import check
from scripts.Algorithm0 import make as make0
from scripts.Algorithm1 import make as make1
from scripts.Algorithm2 import make as make2
from scripts.Algorithm3 import make as make3

from utils.Models import Product

from database.DatabaseUtils import upsert_new_product
from database.DatabaseUtils import get_percent_logistics, get_percent_delivery

from TestDataframe import dataframe

def main(data: list) -> None:
    for i in range(len(data)):
        sid = data[i]['sid'],
        category = data[i]['category']
        name = data[i]['name']
        price = data[i]['price']
        
        # * Проверяем входные данные на нулевые и пустые значения
        blacklist = [0, None]
        if sid in blacklist or category in blacklist \
            or name in blacklist or price in blacklist:
                continue
        
        product = Product(sid=sid, category=category, name=name, price=price)
         
        # * вычисляем id алгоритма и корректируем сумму логистики и доставки   
        algorithm_id, flogistics, fdelivery = check(logistics=product.logistics(),
                                                delivery=product.delivery()) 
        match algorithm_id:
            case 0:
                sale_price = make0(
                    cost_price = product.cost_price,
                    comission_for_returns = product.COMISSION_FOR_RETURNS,
                    comission_percent = product.COMISSION_PERCENT,
                    equiring = product.EQUIRING,
                    logistics_percent=get_percent_logistics(),
                    delivery_percent=get_percent_delivery(),
                    loyalty_program = product.loyalty_program,
                    markup = product.markup
                )
            case 1:
                sale_price = make1(
                    cost_price = product.cost_price,
                    comission_for_returns = product.COMISSION_FOR_RETURNS,
                    comission_percent = product.COMISSION_PERCENT,
                    equiring = product.EQUIRING,
                    flogistics=flogistics,
                    fdelivery=fdelivery,
                    loyalty_program = product.loyalty_program,
                    markup = product.markup)
            case 2:
                sale_price = make2(
                    cost_price = product.cost_price,
                    comission_for_returns = product.COMISSION_FOR_RETURNS,
                    comission_percent = product.COMISSION_PERCENT,
                    equiring = product.EQUIRING,
                    flogistics=flogistics,
                    delivery_percent=get_percent_delivery(),
                    loyalty_program = product.loyalty_program,
                    markup = product.markup
                )
            case 3:
                sale_price = make3(
                    cost_price = product.cost_price,
                    comission_for_returns = product.COMISSION_FOR_RETURNS,
                    comission_percent = product.COMISSION_PERCENT,
                    equiring = product.EQUIRING,
                    logistics_percent=get_percent_logistics(),
                    fdelivery=fdelivery,
                    loyalty_program = product.loyalty_program,
                    markup = product.markup
                )
                
        # * создаем новую или редактируем существующую запись о продукте
        new_product = {
            'sid' : product.sid,
            'category' : product.category,
            'name' : product.name,
            'price' : product.price,
            'cost_price' : product.cost_price,
            'logistics' : flogistics,
            'delivery' : fdelivery,
            'markup' : product.markup,
            'sale_price' : sale_price,
            'calculate' : algorithm_id
        }
        upsert_new_product(new_product)
    
    
if __name__ == '__main__':
    main(dataframe)