from utils.io import load_image, save_image, get_in_out
import numpy as np

def cmd_horizontal_flip(kv: dict) -> int:
    input_path, output_path = get_in_out(kv)
    
    arr = load_image(input_path)  # array rodzaju uint8 (0-255). Problem z overflowem
    out = np.empty_like(arr)
    # metoda shape zwraca krotke z wymiarami tablicy. Jak mamy tablice 2 wierze i 3 kolumny to shape zwroci (2,3)
    rows = arr.shape[0] 
    cols = arr.shape[1]

    #skrypt na odwracanie w poziomie
    for r in range(rows):
        first = 0
        last = cols - 1
        while first < last:
            left  = arr[r, last].copy()
            right = arr[r, first].copy()
            out[r, first] = left
            out[r, last]  = right
            first += 1
            last -= 1
        if first == last:
            out[r, first] = arr[r, first].copy()
    
    save_image(output_path, out)
    return 1