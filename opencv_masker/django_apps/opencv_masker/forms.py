from django import forms
from opencv_masker.masker import Masker
from opencv_masker.validators import check_validation_file_upload

masker = Masker()
colors = masker.colors.keys()
colors = tuple([(color, color) for color in colors])


class VideoUploadForm(forms.Form):
    video = forms.FileField(
        widget=forms.ClearableFileInput(
            attrs={
                "label": "Choose a file",
                "name": "video_upload",
                "id": "video_upload",
                "multiple": False,
            }
        ),
        validators=[
            check_validation_file_upload,
        ],
    )
    color = forms.ChoiceField(choices=colors)
