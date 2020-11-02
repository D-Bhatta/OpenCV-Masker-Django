from django import forms


class VideoUploadForm(forms.Form):
    video = forms.FileField(
        widget=forms.ClearableFileInput(
            attrs={
                "label": "Choose a file",
                "name": "video_upload",
                "id": "video_upload",
                "multiple": False,
            }
        )
    )
