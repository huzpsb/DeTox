import numpy as np
from PIL import Image, ImageFilter

img = Image.open('pr.png').convert('RGB')

h = img.height
w = img.width

# You basically can't predict how the output will shape,
# and thus nearly impossible to combat against the following filters.
img = img.resize((int(h * (np.random.random() + 1)), int(w * (np.random.random() + 1))), Image.Resampling.NEAREST)

# Smooth here, so every pixel isn't the same as the original
img = img.filter(ImageFilter.SMOOTH)
# Median filter breaks the high frequency noise.
img = img.filter(ImageFilter.MedianFilter(3))
# Sharpen to bring back the details
img = img.filter(ImageFilter.SHARPEN)
# Resize to the original shape
img = img.resize((h, w), Image.Resampling.BILINEAR)

img.save('done.png')
