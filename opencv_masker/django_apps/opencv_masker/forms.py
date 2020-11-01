from django import forms


class VideoUploadForm(forms.Form):
    video = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "upload",
                "placeholder": "Choose a file",
                "name": "video_upload",
                "id": "video_upload",
            }
        )
    )
