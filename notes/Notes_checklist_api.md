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
