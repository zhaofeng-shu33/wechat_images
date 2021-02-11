# convert png to jpg
import os
from PIL import Image
def convert(filename):
    img = Image.open(filename)
    img.save(filename.replace('.png', '.jpg'))
def convert_dir():
    for i in os.listdir('./'):
        if i.find('.png') > 0:
            convert(i)
            os.remove(i)
for i in range(4, 13):
    pad_i = '%02d' % i
    os.chdir('2020-%s' % pad_i)
    convert_dir()
    os.chdir('../')

os.chdir('2021-01')
convert_dir()
