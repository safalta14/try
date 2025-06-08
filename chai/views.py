from django.shortcuts import render
from.models  import chaivariety
from django.shortcuts import get_list_or_404
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required 

# Create your views here.
@login_required
def all_chai(request):
    chais=chaivariety.objects.all()
    return render(request,'chai/all_chai.html',{'chais':chais})

def linking(request):
    return render(request,'chai/order.html')

# @login_required
# def chai_detail(request,chai_id):
#     chai=get_object_or_404(chaivariety,pk=chai_id)
    # return render(request,'chai/chai_details.html',{'chai':chai})
