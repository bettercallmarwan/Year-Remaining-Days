import pendulum
import ctypes
import os
import schedule
import time
from PIL import Image, ImageDraw, ImageFont

width, height = 1920, 1080
try:
    font = ImageFont.truetype("arial.ttf", 100)
except:
    font = ImageFont.load_default()

def last_day_current_year():
    return pendulum.now().last_of('year')

def current_day():
    return pendulum.now()

def remaining_days():
    return (last_day_current_year() - current_day()).in_days() + 1

def days_to_png(filename):
    global i
    image = Image.new("RGB", (width, height), color="black")
    draw = ImageDraw.Draw(image)

    days_remaining = remaining_days()
    text = str(days_remaining)

    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    position = ((width - text_width) // 2, (height - text_height) // 2)

    draw.text(position, text, fill="white", font=font)
    image.save(filename)

def set_wallpaper():
    script_dir = r"D:\python projects\Year's Remaining Days"
    new_filename = f"wallpaper_{int(time.time())}.png"
    abs_path = os.path.join(script_dir, new_filename)
    days_to_png(abs_path)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, abs_path, 0x01 | 0x02)
    print(f"Wallpaper set to: {abs_path}")

set_wallpaper()

schedule.every().day.at("00:00").do(set_wallpaper)

while True:
    schedule.run_pending()
    time.sleep(1)