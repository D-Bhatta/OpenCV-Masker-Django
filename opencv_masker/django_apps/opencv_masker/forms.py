from django import forms
from opencv_masker.validators import check_validation_file_upload


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
