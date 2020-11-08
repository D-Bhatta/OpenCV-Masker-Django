# App checklist

This app is meant to take a video from the internet and make a color in it invisible.
The input video is required to have a few seconds of background in the first few frames.

## Main tasks

- Create project and deploy
- A homepage where people upload their videos through an upload form.
- Create an API that will take the input video, and return an output video url.
- Create a class that will mask colors in a video.
- Create a view that returns the video in a page.

## Create project and deploy

- Create a django project
- Deploy to python anywhere

## A homepage where people upload their videos through an upload form

- Create a homepage with a heading and instructions and example videos
- Add a form with upload button and a check list with `blue` and `red` on it
- Link the form destination to it

## Create an API that will take the input video, and return an output video url

- Create a view at an url that takes a request
- It extracts the video from the request and stores it
- It calls the class function with the input video
- It returns the video url

## Create a class that will mask colors in a video

- Turn the existing code into a class
- Create input, output functions
- Create a mask and replace with background

## Create a view that returns the video in a page

- Create a video page that displays the video

## Future Enhancements

### Overwrite on download

- Trigger the overwriting of the videos whenever the output video is downloaded, instead of when homepage loads.
