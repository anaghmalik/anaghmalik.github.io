import os
import imageio
import matplotlib.pyplot as plt 
import numpy as np 

basedir = "/Users/anagh/Projects/anaghmalik.github.io/TransientNeRF/static/videos/masks"
imgdir = "/Users/anagh/Projects/anaghmalik.github.io/TransientNeRF/static/videos/images"
outdir = "/Users/anagh/Projects/anaghmalik.github.io/TransientNeRF/static/videos/masked_images"

for file in os.listdir(basedir):
    mask_img = imageio.imread(os.path.join(basedir, file))
    # mask = np.zeros((512, 512))
    # mask[mask_img[..., 0]==253] = 1
    # mask = mask.astype(np.int8)
    mask = mask_img/255

    img = imageio.imread(os.path.join(imgdir, file))/255
    if img.ndim == 2:
        new_img = np.ones((512, 512))
        new_img = new_img*(1-mask) + img*(mask)
    else:
        new_img = np.ones((512, 512, 3))
        new_img = new_img*(1-mask[..., None]) + img*(mask[..., None])

    
    imageio.imsave(os.path.join(outdir, file), (new_img*255).astype(np.uint8))

    