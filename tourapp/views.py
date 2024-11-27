from django.shortcuts import render,redirect
from tourapp.models import Category_DB,Package_DB
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage

# Create your views here.
def admin(req):
    return render(req,"admin.html")
def add_category(request):
    return render(request,"Add_category.html")
def Save_category(request):
    if request.method=="POST":
        na=request.POST.get('name')
        ds=request.POST.get('description')
        img=request.FILES['image']
        obj=Category_DB(Category_Name=na, Description=ds,Category_Image=img)
        obj.save()
        return redirect(add_category)
def view_category(request):
    data=Category_DB.objects.all()
    return render(request,"view_category.html",{'data':data})
def edit_category(request,cat_id):
    data=Category_DB.objects.get(id=cat_id)
    return  render(request,"edit_category.html",{'data':data})
def update_category(request,cat_id):
    if request.method=="POST":
        na = request.POST.get('name')
        ds = request.POST.get('description')
        try:
            img=request.FILES['image']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=Category_DB.objects.get(id=cat_id).Category_Image
        Category_DB.objects.filter(id=cat_id).update(Category_Name=na, Description=ds,Category_Image=file)
        return redirect(view_category)
def delete_category(request,cat_id):
    x=Category_DB.objects.filter(id=cat_id)
    x.delete()
    return redirect(view_category)
def add_package(request):
    category=Category_DB.objects.all()
    return render(request,"Add_package.html",{'category':category})
def save_package(request):
    if request.method=="POST":
      cn= request.POST.get('cname')
      pn= request.POST.get('name')
      pd= request.POST.get('description')
      pc= request.POST.get('price')
      dy= request.POST.get('day')
      dss1=request.POST.get('ds1')
      dss2=request.POST.get('ds2')
      dss3=request.POST.get('ds3')
      img1 = request.FILES['image1']
      img2 = request.FILES['image2']
      img3 = request.FILES['image3']
      obj1 = Package_DB(CategoryName=cn, Package_Name=pn, Package_Description=pd, Price=pc, Days=dy, Description1=dss1, Description2=dss2, Description3=dss3, Image1=img1, Image2=img2, Image3=img3)
      obj1.save()
      return redirect(add_package)
def view_package(request):
    data = Package_DB.objects.all()
    return render(request,"view_package.html",{'data':data})
def edit_package(request,pack_id):
    data = Package_DB.objects.get(id=pack_id)
    category = Category_DB.objects.all()
    return render(request,"edit_package.html",{'category':category,'data':data})

# def save_package(request, cat_id):
#         if request.method == "POST":
#             cn = request.POST.get('cname')
#             pn = request.POST.get('name')
#             pd = request.POST.get('description')
#             pc = request.POST.get('price')
#             dy = request.POST.get('day')
#             dss1 = request.POST.get('ds1')
#             dss2 = request.POST.get('ds2')
#             dss3 = request.POST.get('ds3')
#             try:
#                 img = request.FILES['img1']
#                 fs = FileSystemStorage()
#                 file1 = fs.save(img.name, img)
#             except MultiValueDictKeyError:
#                 file1 = Package_DB.objects.get(id=cat_id).Image1
#             try:
#                 img = request.FILES['img2']
#                 fs = FileSystemStorage()
#                 file2 = fs.save(img.name, img)
#             except MultiValueDictKeyError:
#                 file2 = Package_DB.objects.get(id=cat_id).Image2
#             try:
#                 img = request.FILES['img3']
#                 fs = FileSystemStorage()
#                 file3 = fs.save(img.name, img)
#             except MultiValueDictKeyError:
#                 file3 = Package_DB.objects.get(id=cat_id).Image3
#             Package_DB.objects.filter(id=cat_id).update(CategoryName=cn, Package_Name=pn, Package_Description=pd,
#                                                         Price=pc, Day=dy, Description1=dss1, Description2=dss2,
#                                                         Description3=dss3, Image1=file1, Image2=file2, Image3=file3)
#             return redirect(add_package)















