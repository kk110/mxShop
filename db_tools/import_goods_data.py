import sys
import os

# 当前路径
pwd = os.path.dirname(os.path.realpath(__file__))
# 指定环境寻找settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE','mxShop.settings')

import django
django.setup()

from goods.models import Goods,GoodsCategory,GoodImage

from db_tools.data.product_data import row_data

for goods_detail in row_data:
    goods = Goods()
    goods.name = goods_detail['name']
    goods.market_price = float(goods_detail['market_price'].replace('￥','').replace('元',''))
    goods.shop_price = float(goods_detail['sale_price'].replace('￥','').replace('元',''))
    goods.goods_brief = goods_detail['desc'] if goods_detail['desc'] is not None else ""
    goods.goods_desc = goods_detail['goods_desc'] if goods_detail['goods_desc'] is not None else ""
    # 取第一张作为封面
    goods.goods_front_image = goods_detail['images'][0] if goods_detail['images'] is not None else ''
    # 取最后一个
    category_name = goods_detail['categorys'][-1]
    # 取出当前子类对应的商品分类对象，filter没有匹配的会返回空数组，不报异常
    category = GoodsCategory.objects.filter(name=category_name)
    if category:
        goods.category = category[0]
    goods.save()

    for goods_image in goods_detail['images']:
        goods_image_instance = GoodImage()
        goods_image_instance.image = goods_image
        goods_image_instance.goods = goods
        goods_image_instance.save()