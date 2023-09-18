import pandas as pd

from scripts.CheckAlgorithm import check
from scripts.Algorithm0 import make as make0
from scripts.Algorithm1 import make as make1
from scripts.Algorithm2 import make as make2
from scripts.Algorithm3 import make as make3

from utils.Models import Product

from database.DatabaseUtils import upsert_new_product
from database.DatabaseUtils import get_percent_logistics, get_percent_delivery

def main(data):
    for index, row in data.iterrows():
        sid = row['sid']
        category = row['category']
        name = row['name']
        price = row['price']

        if any(val in [0, None, ''] for val in [sid, category, name, price]):
            continue

        product = Product(sid=sid, category=category, name=name, price=price)

        algorithm_id, flogistics, fdelivery = check(
            logistics=product.logistics(),
            delivery=product.delivery())

        if algorithm_id == 0:
            sale_price = make0(
                cost_price=product.cost_price,
                comission_for_returns=product.COMISSION_FOR_RETURNS,
                comission_percent=product.COMISSION_PERCENT,
                equiring=product.EQUIRING,
                logistics_percent=get_percent_logistics(),
                delivery_percent=get_percent_delivery(),
                loyalty_program=product.loyalty_program,
                markup=product.markup
            )
        elif algorithm_id == 1:
            sale_price = make1(
                cost_price=product.cost_price,
                comission_for_returns=product.COMISSION_FOR_RETURNS,
                comission_percent=product.COMISSION_PERCENT,
                equiring=product.EQUIRING,
                flogistics=flogistics,
                fdelivery=fdelivery,
                loyalty_program=product.loyalty_program,
                markup=product.markup
            )
        elif algorithm_id == 2:
            sale_price = make2(
                cost_price=product.cost_price,
                comission_for_returns=product.COMISSION_FOR_RETURNS,
                comission_percent=product.COMISSION_PERCENT,
                equiring=product.EQUIRING,
                flogistics=flogistics,
                delivery_percent=get_percent_delivery(),
                loyalty_program=product.loyalty_program,
                markup=product.markup
            )
        elif algorithm_id == 3:
            sale_price = make3(
                cost_price=product.cost_price,
                comission_for_returns=product.COMISSION_FOR_RETURNS,
                comission_percent=product.COMISSION_PERCENT,
                equiring=product.EQUIRING,
                logistics_percent=get_percent_logistics(),
                fdelivery=fdelivery,
                loyalty_program=product.loyalty_program,
                markup=product.markup
            )

        new_product = {
            'sid': sid,
            'category': category,
            'name': name,
            'price': price,
            'cost_price': product.cost_price,
            'logistics': flogistics,
            'delivery': fdelivery,
            'markup': product.markup,
            'sale_price': sale_price,
            'calculate': algorithm_id
        }
        upsert_new_product(new_product)

if __name__ == '__main__':
    filename = input('Введите название файла в формате "название_файла.csv": ')
    try:
        data = pd.read_csv(f'{filename}')
    except FileNotFoundError:
        print('! Проверьте корректность ввода имени файла')
    else:
        data = data.dropna()
        main(data)