# Create an API that will take the input video, and return an output video url

- Create a view at an url that takes a request
- It extracts the video from the request and stores it
- It calls the class function with the input video
- It returns the video url

## Main tasks

- Create a view that takes a form request URL, and a `source` variable
- Get video from the request and store it if necessary
- Pass it to class `Masker` function `apply_mask`
- Get output url
- Return according to `source`

## Create a view that takes a form request URL, and a `source` variable

- Create a view function `video` that takes a `source` variable
- Check  if form is valid
- Check if `source` is `homepage`
- Add to urls
- Refactor and run

## Get video from the request and store it if necessary

- Get video from the request and store it
- Refactor and run

## Pass it to class `Masker` function `apply_mask`

- Call `Masker.apply_mask` with video path
- Refactor and run

## Get output url

- Get output path and add it to `context`
- Refactor and run

## Return according to `source`

- If it is from `homepage` render a template `view_video.html`
- Else, return output url in response
- Refactor and run
