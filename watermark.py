from PIL import Image
import os
import imdirect


def watermark_all(fname="watermark"):
    if not os.path.exists(fname):
        os.makedirs(fname)
    directory = os.getcwd()
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):
            if filename == "logo.jpg":
                continue
            bname = os.path.basename(filename)
            newname = fname + "/" + bname
            watermark_with_transparency(bname, newname, "logo.png")
            # watermark_photo(bname, newname, "logo.png")
            print(os.path.basename(filename))
            continue
        else:
            continue


def watermark_photo(input_image_path, output_image_path, watermark_image_path):
    base_image = Image.open(input_image_path).convert('RGB')
    base_image = imdirect.autorotate(base_image)
    watermark = Image.open(watermark_image_path)
    w, h = base_image.size

    wm, wh = watermark.size
    base_image.paste(watermark, (w - wm, h - wh))
    base_image.save(output_image_path)


def watermark_with_transparency(input_image_path,
                                output_image_path,
                                watermark_image_path):
    base_image = Image.open(input_image_path)
    #  base_image = imdirect.autorotate(base_image)
    watermark = Image.open(watermark_image_path)
    width, height = base_image.size

    w, h = base_image.size

    watermark.thumbnail((w / 6, h / 6))
    transparent = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    wm, wh = watermark.size
    transparent.paste(base_image, (0, 0))
    transparent.paste(watermark, (w/2 - wm*0.5, h - wh), mask=watermark)
    transparent = transparent.convert('RGB')
    transparent.save(output_image_path)


if __name__ == '__main__':
    watermark_all()
