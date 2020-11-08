from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django_apps.settings import MEDIA_ROOT
from django_apps.utils import get_logger
from opencv_masker.forms import VideoUploadForm
from opencv_masker.utils import store_file, write_file_to_files

lg = get_logger()


def homepage(request):
    # Create form object
    form = VideoUploadForm()

    # On data sent via form
    if request.method == "POST":
        lg.debug("Request is post")
        return video(request)

    context = {"form": form}
    lg.debug("Rendering homepage")
    write_file_to_files(
        "sample.mp4",
        MEDIA_ROOT,
        ["input_video.mp4", "output_video.mp4"],
        [MEDIA_ROOT, MEDIA_ROOT],
    )
    return render(request, "homepage.html", context)


def video(request):
    lg.debug(request)
    # On data sent via form
    if request.method == "POST":
        lg.debug("Request is post")
        # set form data in form object
        form = VideoUploadForm(request.POST, request.FILES)
        # check form validity
        if form.is_valid():
            lg.debug("Form is valid")
            store_file("input_video.mp4", MEDIA_ROOT, request.FILES["video"])
            context = {
                "video_path": "opencv_masker/django_apps/media/output_video.mp4"
            }
            return render(request, "dummy.html", context)
        else:
            error_message = "Invalid Form:\n" + str(form.errors)
            lg.error(error_message)
            raise Http404(error_message)
    else:
        raise Http404("Only POST requests are accepted")
