from django.shortcuts import render
from app.models import Wheel, Nav, Mustbuy, Shop, Mainshow, Foodtype


# Create your views here.
def home(request):
    # 轮播图数据
    wheels = Wheel.objects.all()

    # 导航
    navs = Nav.objects.all()

    # 每日必购
    mustbuys = Mustbuy.objects.all()

    # 商品部分
    shops = Shop.objects.all()
    shophead = shops[0]
    shoptabs = shops[1:3]
    shopclass_list = shops[3:7]
    shopcommends = shops[7:11]

    # 商品列表
    mainshows = Mainshow.objects.all()

    response_dir = {
        'wheels':wheels,
        'navs': navs,
        'mustbuys': mustbuys,
        'shophead': shophead,
        'shoptabs': shoptabs,
        'shopclass_list': shopclass_list,
        'shopcommends': shopcommends,
        'mainshows': mainshows
    }

    return render(request, 'home/home.html', context=response_dir)


def market(request):
    # 分类信息
    foodtypes = Foodtype.objects.all()

    response_dir = {
        'foodtypes': foodtypes
    }

    return render(request, 'market/market.html', context=response_dir)


def cart(request):
    return render(request, 'cart/cart.html')


def mine(request):
    return render(request, 'mine/mine.html')