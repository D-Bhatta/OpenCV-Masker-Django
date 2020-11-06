from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django_apps.utils import get_logger
from opencv_masker.forms import VideoUploadForm

lg = get_logger()


def homepage(request):
    # Create form object
    form = VideoUploadForm()

    # On data sent via form
    if request.method == "POST":
        lg.debug("Request is post")
        # set form data in form object
        form = VideoUploadForm(request.POST, request.FILES)
        # check form validity
        if form.is_valid():
            lg.debug("Form is valid")
            return render(request, "dummy.html", {})
        else:
            error_message = "Invalid Form:\n" + str(form.errors)
            lg.error(error_message)
            raise Http404(error_message)

    context = {"form": form}
    lg.debug("Rendering homepage")
    return render(request, "homepage.html", context)
