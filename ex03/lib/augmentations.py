import torch
from PIL import Image
import numpy as np


class horizontal_flip(torch.nn.Module):
    """
    Flip the image along the second dimension with a probability of p
    """

    def __init__(self, p):
        super().__init__()
        self.p = p

    def forward(self, img):
        # START TODO #################
        # convert the image to numpy
        # draw a random number
        # flip the image in the second dimension 
        # if this number is smaller than self.p
        # raise NotImplementedError
        img_np = np.array(img)
        if np.random.rand(1)[0] < self.p:
            img_np = np.flip(img_np, axis=1)
        return Image.fromarray(img_np)
        # END TODO #################


class random_resize_crop(torch.nn.Module):
    """
    simplified version of resize crop, which keeps the aspect ratio of the image.
    """

    def __init__(self, size, scale):
        """ initialize this transform
        Args:
            size (int): size of the image
            scale (tuple(int)): upper and lower bound for resizing image"""
        super().__init__()
        self.size = size
        self.scale = scale

    def _uniform_rand(self, low, high):
        return np.random.rand(1)[0] * (low - high) + high

    def forward(self, img):
        # START TODO #################
        # raise NotImplementedError
        # Crop a part of the image and resize it to the expected input size.
        img_np = np.array(img)
        # img = Image.fromarray(img)
        # resize the image with a random scale
        scale_factor = self._uniform_rand(self.scale[0], self.scale[1])
        # img = img.resize((int(img.width * scale_factor), int(img.height * scale_factor)))
        new_height = int(self.size * scale_factor)
        new_width = int(img_np.shape[1] * new_height / img_np.shape[0])
        # crop the image to self.size x self.size
        img = Image.fromarray(img_np).resize((new_width, new_height), Image.BICUBIC)
        img = img.crop((0, 0, self.size, self.size))
        return img
        # END TODO #################
