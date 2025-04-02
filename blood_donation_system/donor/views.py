from django.shortcuts import render, redirect, get_object_or_404
from .models import Donor

def donor_list(request):
    donors = Donor.objects.all()
    return render(request, 'donor_list.html', {'donors': donors})

def add_donor(request):
    if request.method == "POST":
        name = request.POST['name']
        blood_group = request.POST['blood_group']
        contact = request.POST['contact']
        Donor.objects.create(name=name, blood_group=blood_group, contact=contact)
        return redirect('donor_list')
    return render(request, 'add_donor.html')

def delete_donor(request, donor_id):
    donor = get_object_or_404(Donor, id=donor_id)
    donor.delete()
    return redirect('donor_list')
