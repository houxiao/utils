#!/usr/bin/env python
# -*- coding:utf-8 -*-

import imageio


def create_gif(image_list, gif_name):
	"""
    :param image_list: all img files you want to make into gif
    :param gif_name: output gif file name
    :return: 
    """
    frames = []
    for image_name in image_list:
        frames.append(imageio.imread(image_name))
    imageio.mimsave(gif_name, frames, 'GIF', duration=0.5)
