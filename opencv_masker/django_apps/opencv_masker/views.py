import logging
import logging.config
from json import load as jload
from pathlib import Path

from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from opencv_masker.forms import VideoUploadForm

# Configure logger lg with config for appLogger from config.json["logging"]
CONFIG_DIR = Path(__file__).resolve().parent.parent.parent.parent
with open(CONFIG_DIR / "config.json", "r") as f:
    config = jload(f)
    logging.config.dictConfig(config["logging"])
lg = logging.getLogger("appLogger")
# lg.debug("This is a debug message")

# Create your views here.


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
