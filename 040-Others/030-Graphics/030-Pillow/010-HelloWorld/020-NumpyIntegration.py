from PIL import Image;
import numpy;

img = Image.open("test.jpg");
img.load();
data = numpy.asarray(img, dtype="int32");
print(data);