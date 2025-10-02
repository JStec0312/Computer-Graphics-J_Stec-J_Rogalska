from utils.io import load_image, save_image, get_in_out
import numpy as np

#cel: Odwrócenie obrazu w pionie (odwrócenie wierszy)
# | [1 2 3 4] | -> |[5 6 7 8] |
# | [5 6 7 8] | -> |[1 2 3 4] |

def cmd_vertical_flip(kv: dict) -> int:
    input_path, output_path = get_in_out(kv)    
    arr = load_image(input_path)  # array rodzaju uint8 (0-255). Problem z overflowem nas nie dotyczy, poniewaz nie robimy zadnych operacji arytmetycznych
    out =  np.flip(arr, axis = 0) #odwraca tablice, axis to oś 0 to wiersze, 1 to kolumny 3 to kanały (RGB), my chcemy odwrócić wiersze czyli oś 0.
    save_image(output_path, out)
    return 1

#poniżej ta sama funckjonalnośc bez użycia numpy flip (ale wolniejsza)

# def cmd_vertical_flip(kv: dict) -> int:
#     input_path, output_path = get_in_out(kv)
#     arr = load_image(input_path)  # array rodzaju uint8 (0-255). Problem z overflowem
#     out = np.empty_like(arr) # tworzymy pusta tablice o takim samym ksztalcie i typie jak arr
#     # metoda shape zwraca krotke z wymiarami tablicy. Jak mamy tablice 2 wierze i 3 kolumny to shape zwroci (2,3)
#     rows = arr.shape[0] 
#     cols = arr.shape[1]
#     #skrypt na odwracanie w pionie
#     for c in range (rows):
#         first = 0
#         last = rows - 1
#         while first < last:
#             top = arr[last, c].copy()
#             bottom = arr[first, c].copy()
#             out[first, c] = top
#             out[last, c]  = bottom
#             first += 1
#             last -= 1
#         if first == last:
#             out[first, c] = arr[first, c].copy()
#     save_image(output_path, out)
#     return 1
