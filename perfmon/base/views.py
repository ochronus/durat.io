""" Views for the base application """

from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from .models import Site, SiteForm

def home(request):
    if request.user.is_authenticated():
        sites = request.user.site_set.all()
        return render(request, 'base/home_signedin.html', {'sites': sites})
    else:
        return render(request, 'base/home.html',)

def get_code_for_site(site_id):
    try:
        site = Site.objects.get(pk=site_id)
        return render_to_string("script_loader.js.template", {'site_hash': site.uuid})
    except Exception as e:
        print e

@login_required
def new_site(request):
    if request.method == 'POST':
        form = SiteForm(request.POST)
        new_site = form.save(commit=False)
        new_site.owner_id = request.user.id
        new_site.save()
        return redirect('/')
    else:
        form = SiteForm()
        return render(request, 'base/new_site.html', {'new_site_form': form})