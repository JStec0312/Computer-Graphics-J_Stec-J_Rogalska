from utils.io import load_image, save_image, get_in_out
import numpy as np

def cmd_negative(kv: dict) -> int:
    input_path, output_path = get_in_out(kv)
    
    arr = load_image(input_path)  # array rodzaju uint8 (0-255). Problem z overflowem
    arr_int = arr.astype(np.int16)  # konwersja na int16 aby uniknac overflowa
    out = 255 - arr_int # formuła na negatyw obrazu (jak bylo 220 to bedzie 35, czyli odwrotnie )
    out = np.clip(out, 0, 255).astype(np.uint8)  # przyciecie do zakresu (256 na 0 i -1 na 0) i konwersja z powrotem na uint8
    save_image(output_path, out)
    return 0