# 第 0000 题： 将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。
__author__ = "Lei gitwing"
from PIL import Image, ImageDraw, ImageFont

def text(input_image_path, output_path, num):
    """ 
    Adding an image from the path, draw a red number text in the image, and then save it in a specific output path.
    """
    with Image.open(input_image_path) as image:
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype("OpenSans-ExtraBold.ttf", size=50)
        draw.text((145, -10), str(num), fill="red", font=font)
        image.save(output_path)


if __name__ == "__main__":
    num = 4
    text("pic.jpg", "new_pic.jpg", num)