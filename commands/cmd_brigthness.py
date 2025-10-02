from utils.io import load_image, save_image, get_in_out
import numpy as np

def cmd_brightness(kv: dict) -> int:
    input_path, output_path = get_in_out(kv)
    try:
        delta = int(float(kv.get("delta")))
        if not (-255 <= delta <= 255):
            print("Delta must be between -255 and 255.")
            return 2
    except (TypeError, ValueError):
        print("Invalid or missing --delta argument.")
        return 2

    arr = load_image(input_path)  # array rodzaju uint8 (0-255). Problem z overflowem
    arr_int = arr.astype(np.int16)  # konwersja na int16 aby uniknac overflowa
    arr_int += delta
    out = np.clip(arr_int, 0, 255).astype(np.uint8)  # przyciecie do zakresu (256 na 0 i -1 na 0) i konwersja z powrotem na uint8
    save_image(output_path, out)
    return 1
