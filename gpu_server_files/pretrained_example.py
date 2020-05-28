# Copyright (c) 2019, NVIDIA CORPORATION. All rights reserved.
#
# This work is licensed under the Creative Commons Attribution-NonCommercial
# 4.0 International License. To view a copy of this license, visit
# http://creativecommons.org/licenses/by-nc/4.0/ or send a letter to
# Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

"""Minimal script for generating an image using pre-trained StyleGAN generator."""

import os
import pickle
import numpy as np
import PIL.Image
import dnnlib
import dnnlib.tflib as tflib
import config
import sys
import subprocess


def main():
    # Initialize TensorFlow.
    tflib.init_tf()

    # Load pre-trained network.
    url = os.path.abspath("/home/ubuntu/stylegan/image.pkl")
    with open(url, 'rb') as f:
        _G, _D, Gs = pickle.load(f)
        # _G = Instantaneous snapshot of the generator. Mainly useful for resuming a previous training run.
        # _D = Instantaneous snapshot of the discriminator. Mainly useful for resuming a previous training run.
        # Gs = Long-term average of the generator. Yields higher-quality results than the instantaneous snapshot.

    # Print network details.
    Gs.print_layers()

    # Pick latent vector.
    rnd = np.random.RandomState(5)
    latents = rnd.randn(1, Gs.input_shape[1])

    #iterations & starting image number
    iterations = int(sys.argv[1])
    image_start = int(sys.argv[2])
    
    for i in range(0, iterations):
        # Generate image.
        fmt = dict(func=tflib.convert_images_to_uint8, nchw_to_nhwc=True)
        images = Gs.run(latents, None, truncation_psi=0.7, randomize_noise=True, output_transform=fmt)
        
        # Save image.
        #os.makedirs(config.result_dir, exist_ok=True)
        png_filename = '/home/ubuntu/stylegan/results/a' + str(image_start+i) + '.png' 
        PIL.Image.fromarray(images[0], 'RGB').save(png_filename)


    # copy resulting images back to Autama Image folder
    tmp = subprocess.Popen('scp -o StrictHostKeyChecking=no -i /home/ubuntu/stylegan/autama.pem /home/ubuntu/stylegan/results/* ubuntu@ec2-52-38-158-185.us-west-2.compute.amazonaws.com:/home/ubuntu/Autama-Backend/Images/', shell=True, stdout=subprocess.PIPE).communicate()  

    # delete images to keep results folder tidy
    tmp = subprocess.Popen('rm /home/ubuntu/stylegan/results/*', shell=True, stdout=subprocess.PIPE).communicate()

    # shut down this instance.
    tmp = subprocess.Popen('aws ec2 stop-instances --instance-ids i-01d6de0c8312b250c --region us-west-2', shell=True, stdout=subprocess.PIPE).communicate()  



if __name__ == "__main__":
    main()
