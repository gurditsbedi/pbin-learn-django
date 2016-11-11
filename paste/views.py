from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt

from .forms import pasteForm
from .models import pasteModel
from .utils import create_shortcode


def index(request):
    form = pasteForm()
    shortcodeDuplicate = None
    try:
        if request.session['shortcodeDuplicate']:
            shortcodeDuplicate = 'This shortcode is already taken. You can go Back and choose another shortcode.'
            request.session['shortcodeDuplicate'] = None
    except:
        pass

    return render(request, 'paste/index.html', {'form': form,
                                                'shortcodeDuplicate': shortcodeDuplicate})


def formSubmit(request):
    if request.method == 'POST':
        form = pasteForm(request.POST)
        if form.is_valid():
            cdata = form.cleaned_data

            # case for repeatation of shortcode/slug
            getslug = None
            try:
                getslug = pasteModel.objects.get(slug=cdata["slug"])
            except ObjectDoesNotExist:
                pass
            if getslug:
                request.session['shortcodeDuplicate'] = True
                return redirect('index')

            # if slug or name is empty
            if not cdata["slug"]: cdata["slug"] = create_shortcode()
            if not cdata["name"]: cdata["name"] = "Untitled"

            # adding to the database
            q = pasteModel(slug=cdata['slug'], name=cdata['name'],
                           text=cdata['text'])
            q.save()
            #redirecting to the paste page
            return redirect('paste', slug=str(cdata['slug']))
        else:
            return redirect('verr')
    else:
        return redirect('index')

def paste(request, slug=None):
    getslug = None
    try:
        getslug = pasteModel.objects.get(slug=slug)
    except ObjectDoesNotExist:
        pass

    if getslug:
        return render(request, 'paste/paste.html', {'paste': getslug})
    else:
        return render(request, 'paste/404.html')


def verr(request):
    return render(request, 'paste/verr.html')

