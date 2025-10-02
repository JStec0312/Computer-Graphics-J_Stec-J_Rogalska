import numpy
from PIL import Image


def load_image(path: str) -> Image.Image:
    try:
        img = Image.open(path)

    except ValueError as e:
        print(f"Error loading image. Check the file path and format. {e}")
        raise SystemExit(2)

    # ENSURE AN IMAGE IN INRGB OR L MODE
    if img.mode == "P":
        img = img.convert("RGB") # paletted image
    elif img.mode == "LA": #grayscale with alpha
        img = img.convert("L")
    elif img.mode == "RGBA": #rgb with alpha
        img = img.convert("RGB") #drop alpha channel
    elif img.mode not in ("L", "RGB"):
        img = img.convert("RGB") #convert to RGB if in unknown mode

    return numpy.array(img) #convert to numpy array

def save_image(path: str, arr: numpy.ndarray) -> None:
    try:
        Image.fromarray(arr).save(path)
    except Exception as e:
        print(f"Error saving image. Check the file path and format. {e}")
        raise SystemExit(2)

def get_in_out(kv:dict) -> tuple[str, str]:
    input_path = kv.get("input")
    output_path = kv.get("output")
    if not input_path or not output_path:
        print("Both --input and --output arguments are required.")
        raise SystemExit(2)
    return input_path, output_path