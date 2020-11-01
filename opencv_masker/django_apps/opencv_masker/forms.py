from django import forms


class VideoUploadForm(forms.Form):
    video = forms.FileField(
        widget=forms.FileInput(
            attrs={
                "type": "upload",
                "placeholder": "Choose a file",
                "name": "video_upload",
                "id": "video_upload",
            }
        )
    )
