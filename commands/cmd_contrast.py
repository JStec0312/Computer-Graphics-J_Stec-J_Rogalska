from utils.io import load_image, save_image, get_in_out
import numpy as np

def cmd_contrast(kv:dict) -> int:
    input_path, output_path = get_in_out(kv)
    try:
        alpha = float(kv.get("alpha"))
    except (TypeError, ValueError):
        print("Invalid or missing --alpha argument.")
        return 2
    
    pivot = 128
    arr = load_image(input_path)  # array rodzaju uint8 (0-255). Problem z overflowem
    arr_int = arr.astype(np.int16)  # konwersja na int16 aby uniknac overflowa
    out = (arr - pivot) * alpha + pivot # formuła na kontrast. Sprawdzamy, czy piskel jest ponizej czy powyzej piwotu, a potem go skalujemy.
    out = np.clip(out, 0, 255).astype(np.uint8)  # przyciecie do zakresu (256 na 0 i -1 na 0) i konwersja z powrotem na uint8
    save_image(output_path, out)
    return 0