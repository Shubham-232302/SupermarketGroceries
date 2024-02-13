from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
import json
from django.core.serializers.json import DjangoJSONEncoder
# from .forms import SubcategoryForm, ItemForm

def home(request):
    # return HttpResponse("<h1>hey this is shubham</h1>")
    return render(request, 'index.html')

# def success(request):
#     return HttpResponse("<h1> This is success page </h1>")

# Create your views here.

def addCategory(request):
    if request.method == 'POST':
        data = request.POST
        print(data.get('category'))
        Category.objects.create(name=data.get('category'))
        return redirect('/addCategory')
    return render(request, 'addCategory.html')


def addSubCategory(request):
    data = Category.objects.all()
    arr=[]
    for ele in data:
        arr.append(ele.name)
    if request.method == 'POST':
        data = request.POST
        if data.get('subCategory') and data.get('category'):
            SubCategory.objects.create(name=data.get('subCategory'), category = Category.objects.get(name = data.get('category')))
            # SubCategory.objects.create(name='Beverage', category = 'ThumsUp')
        return redirect('/addSubCategory')
    return render(request, 'addSubCategory.html', context={"data": arr})

def deleteCategory(request):
    data = Category.objects.all()
    arr=[]
    for ele in data:
        arr.append(ele.name)
    if request.method == 'POST':
        item = request.POST.get('delCategory')
        if item:
            Category.objects.get(name=item).delete()
        print(request.POST.get('delCategory'))
        return redirect('/deleteCategory')
    return render(request, 'deleteCategory.html', context={"data":arr})



def addItem(request):
    categories = [ele.name for ele in Category.objects.all()]
    subcategories_temp = [[ele.name,ele.category.name] for ele in SubCategory.objects.all()]
    subcategories = {}
    for ele in subcategories_temp:
        if ele[1] in subcategories:
            subcategories[ele[1]].append(ele[0])
        else:
            subcategories[ele[1]] = [ele[0]]
    if request.method == "POST":
        data = request.POST
        print(data)
        Item.objects.create(
            name = data.get('item'),
            price = data.get('price'),
            subCategory = SubCategory.objects.get(name = data.get('subcategory'))
        )
        return redirect('/addItem')

# SubCategory.objects.create(name=data.get('subCategory'), category = Category.objects.get(name = data.get('category')))

    return render(request, 'addItem.html', context={"subcategories": subcategories,"categories":categories})

def delSubCategory(request):
    categories = [ele.name for ele in Category.objects.all()]
    subcategories_temp = [[ele.name,ele.category.name] for ele in SubCategory.objects.all()]
    subcategories = {}
    for ele in subcategories_temp:
        if ele[1] in subcategories:
            subcategories[ele[1]].append(ele[0])
        else:
            subcategories[ele[1]] = [ele[0]]
    if request.method == "POST":
        data = request.POST
        SubCategory.objects.get(
            name = data.get('subcategory'),
            category = Category.objects.get(name = data.get('category'))
        ).delete()
        return redirect('/delSubCategory')
    return render(request, 'delSubCategory.html', context={"subcategories": subcategories,"categories":categories})

def delItem(request):
    categories = [ele.name for ele in Category.objects.all()]
    subcategories_temp = [[ele.name,ele.category.name] for ele in SubCategory.objects.all()]
    item_temp = [[ele.name,ele.subCategory.name] for ele in Item.objects.all()]
    subcategories = {}
    item={}
    for ele in subcategories_temp:
        if ele[1] in subcategories:
            subcategories[ele[1]].append(ele[0])
        else:
            subcategories[ele[1]] = [ele[0]]

    for ele in item_temp:
        if ele[1] in item:
            item[ele[1]].append(ele[0])
        else:
            item[ele[1]] = [ele[0]]


    if request.method == "POST":
        data = request.POST
        Item.objects.get(
            name = data.get('item'),
            subCategory = SubCategory.objects.get(name = data.get('subcategory'))
        ).delete()
        print(data.get('item'))
        print(data.get('subcategory'))
        return redirect('/delItem')
    return render(request, 'delItem.html', context={"subcategories": subcategories,"categories":categories, "items":item})


def displayData(request):
    categories = [ele.name for ele in Category.objects.all()]
    subcategories_temp = [[ele.name,ele.category.name] for ele in SubCategory.objects.all()]
    item_temp = [[ele.name,ele.subCategory.name, ele.price] for ele in Item.objects.all()]
    subcategories = {}
    item={}
    for ele in subcategories_temp:
        if ele[1] in subcategories:
            subcategories[ele[1]].append(ele[0])
        else:
            subcategories[ele[1]] = [ele[0]]

    for ele in item_temp:
        print(item_temp)
        if ele[1] in item:
            item[ele[1]].append({'name':ele[0], 'price':ele[2]})
        else:
            item[ele[1]] = [{'name':ele[0], 'price':ele[2]}]
    print(item)
    item = json.dumps(item, cls=DjangoJSONEncoder)

    return render(request, 'displayData.html', context={"subcategories": subcategories,"categories":categories, "items":item})


def updateCategory(request):
    data = Category.objects.all()
    arr=[]
    for ele in data:
        arr.append(ele.name)
    if request.method == 'POST':
        item = request.POST.get('updateCategory')
        if item:
            Category.objects.filter(name=item).update(name = request.POST.get('newCategory'))
        print(request.POST.get('updateCategory'))
        return redirect('/updateCategory')
    return render(request, 'updateCategory.html', context={"data":arr})



def UpdateSubCategory(request):
    categories = [ele.name for ele in Category.objects.all()]
    subcategories_temp = [[ele.name,ele.category.name] for ele in SubCategory.objects.all()]
    subcategories = {}
    for ele in subcategories_temp:
        if ele[1] in subcategories:
            subcategories[ele[1]].append(ele[0])
        else:
            subcategories[ele[1]] = [ele[0]]
    if request.method == "POST":
        data = request.POST
        SubCategory.objects.filter(
            name = data.get('subcategory'),
            category = Category.objects.get(name = data.get('category'))
        ).update(name = data.get('newsubcategory'))
        return redirect('/updateSubCategory')
    return render(request, 'updateSubCategory.html', context={"subcategories": subcategories,"categories":categories})


def updateItem(request):
    categories = [ele.name for ele in Category.objects.all()]
    subcategories_temp = [[ele.name,ele.category.name] for ele in SubCategory.objects.all()]
    item_temp = [[ele.name,ele.subCategory.name] for ele in Item.objects.all()]
    subcategories = {}
    item={}
    for ele in subcategories_temp:
        if ele[1] in subcategories:
            subcategories[ele[1]].append(ele[0])
        else:
            subcategories[ele[1]] = [ele[0]]

    for ele in item_temp:
        if ele[1] in item:
            item[ele[1]].append(ele[0])
        else:
            item[ele[1]] = [ele[0]]


    if request.method == "POST":
        data = request.POST

        element = Item.objects.filter(
            name = data.get('item'),
            subCategory = SubCategory.objects.get(name = data.get('subcategory'))
        )
        if data.get('newItem'):
            element.update(name = data.get('newItem'))
        if data.get('newPrice'):
            element.update(price = data.get('newPrice'))
        print(data.get('item'))
        print(data.get('subcategory'))
        return redirect('/updateItem')
    return render(request, 'updateItem.html', context={"subcategories": subcategories,"categories":categories, "items":item})

