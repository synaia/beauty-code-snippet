import asyncio
from carbon import Carbon
import os
from pathlib import Path
from PIL import Image

client = Carbon()

from carbon import Carbon

client = Carbon(
    downloads_dir=os.getcwd(),  # Defaults to current directory
    colour="rgba(132, 102, 191, 100)",  # Hex or rgba color
    shadow=True,  # Turn on/off shadow
    shadow_blur_radius="68px",
    shadow_offset_y="20px",
    export_size="2x",  # resolution of exported image, e.g. 1x, 3x
    font_size="14px",
    font_family= "Hack",  # font family, e.g. JetBrains Mono, Fira Code.
    first_line_number=1,
    language="Python",  # programing language for properly highlighting
    line_numbers=False,  # turn on/off, line number
    horizontal_padding="26px",
    vertical_padding="26px",
    theme="cobalt",  # code theme dracula-pro, seti, cobalt
    watermark=False,  # turn on/off watermark
    width_adjustment=True,  # turn on/off width adjustment
    window_controls= True,  # turn on/off window controls
    window_theme=None
)


image_name = 'test01'


async def main():
    file = Path('./snippet.py').read_text()
    img = await client.create(file, file=image_name)
    print(img)


def watermark_with_transparency(input_image_path,
                                output_image_path):
    watermark_image_path = 'synaia_beta.png'
    base_image = Image.open(input_image_path)
    watermark = Image.open(watermark_image_path)
    watermark = watermark.reduce(factor=25)
    width, height = base_image.size
    transparent = Image.new('RGBA', (width, height), (0,0,0,0))
    transparent.paste(base_image, (0,0))
    transparent.paste(watermark, (width - 80, height - 80), mask=watermark)
    transparent.show()
    transparent.save(output_image_path)


if __name__ == '__main__':
    asyncio.run(main())
    img = f'{image_name}-wm.png'
    watermark_with_transparency(f'{image_name}.png', img)


