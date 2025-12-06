from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import item
from .forms import itemform
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
import logging
from django.shortcuts import get_object_or_404
from django.utils import timezone
logger = logging.getLogger(__name__)

#@login_required
"""class IndexClassView(ListView):
    model=item
    template_name='food/index.html'
    context_object_name='item_list'"""
#@cache_page(60*3)
#@vary_on_headers("User-Agent")
def index(request): 
    logger.info("Index Page Requested")
    logger.info(f"User [{timezone.now().isoformat()}] {request.user} requested item from {request.META.get('REMOTE_ADDR    ')}")
    item_list =item.objects.all()
    logger.debug(f"Found { item_list.count() } items")
    paginator = Paginator(item_list, 5)
    page_no = request.GET.get("page")
    page_obj = paginator.get_page(page_no)
    context = {
        "page_obj": page_obj
    }
    return render (request, "food/index.html", context )

"""class Detail(DetailView):
    model=item
    template_name='food/detail.html'
    context_object_name='item_detail'"""

def detail(request,id):
    logger.info(f"Fetching item with id: {id}")
    try:
        item_detail = get_object_or_404(item, id=id)
        logger.debug("Found the item: {item_detail.item_name}, ${item_detail.item_price}")
    except Exception as e:
        logger.error("Error found with id %s: %s",id,e)
        raise

    context = {
        "item_detail": item_detail
    }
    return render(request, "food/detail.html",context)


"""class ItemCreateView(CreateView):
    model=item
    fields = [ 'item_name', 'item_desc', 'item_price', 'item_image']
    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)
"""

def create_item(request):
    form = itemform(request.POST or None)
    if request.method=="POST" :
        print("POST METHOD TRIGGERED")
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('food:index')
    context = {
        "form":form
    }
    return render(request,"food/item-form.html",context)


class ItemUpdate(UpdateView):
    model=item
    fields = [ 'item_name', 'item_desc', 'item_price', 'item_image']
    template_name_suffix = '_update'

    def get_queryset(self):
        return item.objects.filter(user_name=self.request.user)

"""def update_item(request,id):
    print("THIS IS THE ID FROM URL",id)
    item_detail = item.objects.get(id=id)
    
    form = itemform(request.POST or None, instance=item_detail)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    context={
        "form":form
    }    
    return render(request,'food/item-form.html',context)"""


"""class ItemDelete(DeleteView):
    model=item
    success_url= reverse_lazy('food:index')
    template_name_suffix='-delete' """

def delete_item(request,id):
    item_detail=item.objects.get(id=id)
    if request.method=='POST': 
        item_detail.delete()
        return redirect('food:index')
    
    return render(request, 'food/item-delete.html')