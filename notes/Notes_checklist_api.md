# Create an API that will take the input video, and return an output video url

- Create a view at an url that takes a request
- It extracts the video from the request and stores it
- It calls the class function with the input video
- It returns the video url

## Main tasks

- Create a view that takes a form request
- Get video from the request and store it if necessary
- Pass it to class `Masker` function `apply_mask`
- Get output video path
- Render a page where it can be downloaded
- Refactor homepage

## Create a view that takes a form request

- Create a view function `video`
- Check  if form is valid
- Add to urls
- Refactor and run

## Get video from the request and store it if necessary

- Get video from the request and store it
- Create a function `store_file(name: str, path: str, and file: FileType)`
- Create media root directory
- Store file in media root directory
- Add `media/` to `.gitignore`
- Refactor and run

## Pass it to class `Masker` function `apply_mask`

- Call `Masker.apply_mask` with video path
- Redirect to `show_video`
- Refactor and run

## Get output url

- Get output path and add it to `context`
- Refactor and run

## Refactor homepage

- Rewrite the video file when homepage renders
- Create utility functions.
- Call function `write_file_to_files` whenever `homepage` loads with media files.
