from scripts.CheckAlgorithm import check
from scripts.Algorithm0 import make as make0
from scripts.Algorithm1 import make as make1
from scripts.Algorithm2 import make as make2
from scripts.Algorithm3 import make as make3

from utils.Models import Product

from database.DatabaseUtils import upsert_new_product

from TestDataframe import dataframe

def main(data: list) -> None:
    for i in range(len(data)):
        product = Product(sid = data[i]['sid'],
                          category = data[i]['category'],
                          name = data[i]['name'],
                          price = data[i]['price'])
        algorithm_id = check(logistics=Product.logistics(),
                             delivery=Product.delivery()) 
        match algorithm_id:
            case 0:
                sale_price = make0()
            case 1:
                sale_price = make1()
            case 2:
                sale_price = make2()
            case 3:
                sale_price = make3()
        upsert_new_product()
    
if __name__ == '__main__':
    main(dataframe)