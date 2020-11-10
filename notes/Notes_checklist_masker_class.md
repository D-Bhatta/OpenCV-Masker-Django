# Create a class that will mask colors in a video

- Turn the existing code into a class
- Create input, output functions
- Create a mask and replace with background

## Main Tasks

- Create a class `Masker`
- Add an input function that gets the video
- Add an output function that returns a video path
- Add mask related functions
- Add a function to apply mask
- Add video writing functions
- Add docstrings
- Refactor and run on pythonAnywhere

## Create a class `Masker`

- Create a module `masker.py`
- Create a class `Masker`
- Initialize it with `video_path` for input video
- Initialize it with `colors` for `dict` of colors
- Refactor and run

## Add an input function that gets the video

- Create a funtion `apply_mask` that gets the input video, and Colors list and sets it to `video_path` and `colors`
- Refactor and run

## Add an output function that returns a video url

- Create an output function that returns the output path

- Create function `get_video` that returns the path to the video
- Return a path to one of the media videos for now
- Return the return of this function in funtion `apply_mask`
- Refactor and run

## Add mask related functions

- Function `get_colors` to get dict of colors and their ranges
- Function `get_mask` to create and return a mask of a color
- Function `get_masks` to create a list of masks from an input list of colors
- Function `add_masks` to add list of masks
- Function `and_masks` to `and` list of masks
- Function `gen_mask` to generate mask from a video
- Function `refine_mask` to refine masks
- Refactor and run

## Add a function to apply mask

- Function `get_res` to generate final resources
- Refactor and run

## Add video writing functions

- Function `gen_output_video` to iterate over the video and write it
- Refactor and run

## Add more colors

- Add `RED` color to `colors` dict

## Refactor the class

- The class doesn't seem to work.
- Rather than find the bug, refactor it into fewer methods.
