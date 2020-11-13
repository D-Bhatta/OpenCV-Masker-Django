# Create a view that returns the video in a page

- Create a video page that displays the video

## Main tasks

- Create a view and url to display the video with context
- Create a template to display the video
- Show warning to download or video will disappear

## Create a view and url to display the video with context

- Create a view `show_video` to display the video
- Create a `context` dict with url of the output video
- Add url as `show_video/`

## Create a template to display the video

- Create a template `show_video.html`
- Add a heading
- Add elements to display output video
- Research downloading of the video
- Create a `download` view
- Add url as `"download/<str:filename>/"`
- Return `filename` in context
- Create a `filepath` with `MEDIA_ROOT` + `filename`
- Create a `FileResponse` object and return it
- If there is an exception, return `404`
- Show a button that will start download of the video and put the URL inside
- Refactor and run

## Show warning to download or video will disappear

- Add text that says `Save video or it will be deleted`
