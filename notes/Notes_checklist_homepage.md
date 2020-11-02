# A homepage where people upload their videos through an upload form

- Create a homepage with a heading and instructions and example videos
- Add a form with upload button and a check list with `blue` and `red` on it
- Link the form destination to it

## Main tasks

- Create a view
- Create a homepage
- Add a form element with a dummy link
- Add the videos
- Link the form
- Research how to upload files and use checklists

## Create a view

- Create a `homepage` view function
- Add an url to `home/`
- Serve `dummy.html`
- Run and refactor

## Create a homepage

- Create a `homepage.html`
- Add a heading
- Add a dummy instruction paragraph
- Add a form element
- Run and refactor

## Add a form element with a dummy link

- Create a `Form` in `forms.py` as `VideoUploadForm`
- Add a `TextField` with a `TextInput` `Widget`
- Add it to the `context` variable of the `homepage` view function
- Place it in `homepage.html`
- Run and refactor

## Add the videos

- Upload to YouTube and embed
- Run and refactor

## Link the form

- Link the form to render `dummy.html`
- Link the form to the actual api view

## Research how to upload files and use checklists

- Research how to upload files and use checklists
- Create plan for it

## Modify form to upload files

- Change `TextField` to `FileField`
- Add a `ClearableFileInput` widget
- Set attrs
- Run and refactor
- Create validation function `check_validation_file_upload` and pass
- Add to `validators` parameter
- Run and refactor
- Check validation for file size, type, and extension
