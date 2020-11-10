import time

import cv2
import numpy as np
from django_apps.settings import MEDIA_ROOT
from django_apps.utils import get_logger

lg = get_logger()

# pylint: disable=no-member


class Masker:
    r"""Class for performing masking functions on an input video.

    This class abstracts away the logic of creating a mask from a color and
    using it to replace the masked region with a mask of the background
    instead.

    The class uses OpenCV functions and logs information as it operates.

    Supported colors:
    ----------
    BLUE

    Attributes
    ----------
    colors : dict
        Dict of color values supported by the class. Contains sub dictionaries
        that hold information needed to create masks of that color.
    output_path : str
        Path to the output video file.

    Parameters
    ----------
    video_path : str
        Path to the input video.

    Methods
    ----------
    apply_mask(video_path: str, colors: list)
        Call this method to apply masks to an input video from a list of
        colors. Colors should be in CAPITAL letters.

    Examples
    --------
    Create a Masker object and call the `apply_mask` method.

    >>> from masker import Masker
    >>> maskr = Masker()
    >>> maskr.apply_mask(MEDIA_ROOT + "video_path.mp4", "BLUE")
    """

    def __init__(self, video_path=""):
        self.colors = {
            "BLUE": {
                "multiple": True,
                "num": 2,
                "ranges": [
                    (np.array([75, 125, 20]), np.array([95, 255, 255])),
                    (np.array([95, 125, 20]), np.array([130, 255, 255])),
                ],
            },
        }
        self.video_path = video_path
        self.output_path = MEDIA_ROOT + "output_video.mp4"
        self.input_colors = []

    def apply_mask(self, video_path: str, colors: list):
        self.video_path = video_path
        for color in colors:
            try:
                self.colors[color]
            except KeyError:
                lg.error(
                    "Couldn't recognise color. Please try with a different color or check the color name entered."
                )
                raise ValueError("Unknown Color")
        self.input_colors = self.input_colors + colors
        return self.get_video()

    def get_video(self):
        self.gen_video()
        return self.output_path

    def get_colors(self):
        ranges = []
        for color_name in self.input_colors:
            color = self.colors[color_name]
            if color["multiple"]:
                for i in range(color["num"]):
                    ranges.append(color["ranges"][i])
            else:
                ranges.append(color["ranges"])

        return ranges

    def get_mask(self, color_range: tuple, hsv):
        # lg.debug(color_range)
        lower, upper = color_range
        mask = cv2.inRange(hsv, lower, upper)  # pylint: disable=no-member
        return mask

    def get_masks(self, ranges: list, hsv) -> list:
        masks = []
        for color_range in ranges:
            mask = self.get_mask(color_range, hsv)
            masks.append(mask)
        return masks

    def refine_mask(self, mask):

        mask = cv2.morphologyEx(  # pylint: disable=no-member
            mask, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations=1
        )
        mask = cv2.dilate(  # pylint: disable=no-member
            mask, np.ones((3, 3), np.uint8), iterations=1
        )

        return mask

    def gen_video(self):
        ranges = self.get_colors()
        lg.debug(ranges)

        captured_video = cv2.VideoCapture(self.video_path)
        lg.debug(captured_video)
        time.sleep(2)
        shape = int(captured_video.get(cv2.CAP_PROP_FRAME_WIDTH)), int(
            captured_video.get(cv2.CAP_PROP_FRAME_HEIGHT)
        )
        lg.info(f"Dimensions of the video: {shape}")
        # For the first 50 frames, get the video background pixels

        background = 0
        for i in range(50):
            return_value, background = captured_video.read()
            if return_value == False:
                continue

        # Flip the frame array so that we get the pixels mirrored
        background = np.flip(background, axis=1)

        count = 0
        fourcc = cv2.VideoWriter_fourcc(*"MP4V")
        output_writer = cv2.VideoWriter(self.output_path, fourcc, 20.0, shape)

        while captured_video.isOpened():
            return_val, img = captured_video.read()
            if not return_val:
                break
            count += 1
            img = np.flip(img, axis=1)

            # Convert to hsv color range
            hsv = cv2.cvtColor(
                img, cv2.COLOR_BGR2HSV
            )  # pylint: disable=no-member
            masks = self.get_masks(ranges, hsv)

            mask1 = masks[0]
            # lg.debug(mask1)
            if len(masks) > 1:
                for i in range(1, len(masks)):
                    mask1 = mask1 + masks[i]
            # lg.debug(mask1)

            mask1 = self.refine_mask(mask1)
            # lg.debug(mask1)
            inv_mask = cv2.bitwise_not(mask1)
            # lg.debug(inv_mask)

            res1 = cv2.bitwise_and(background, background, mask=mask1)
            res2 = cv2.bitwise_and(img, img, mask=inv_mask)
            final_output = cv2.addWeighted(res1, 1, res2, 1, 0)

            output_writer.write(final_output)

        lg.info(f"Wrote frames: {count}")
