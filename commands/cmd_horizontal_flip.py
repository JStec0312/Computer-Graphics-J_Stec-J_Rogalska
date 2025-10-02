from utils.io import load_image, save_image, get_in_out
import numpy as np


#cel:
# | [1 2 3 4] | -> | [4 3 2 1] |
# | [5 6 7 8] | -> | [8 7 6 5] |

def cmd_horizontal_flip(kv: dict) -> int:
    input_path, output_path = get_in_out(kv)
    
    arr = load_image(input_path)  # array rodzaju uint8 (0-255). Problem z overflowem nas nie dotyczy, poniewaz nie robimy zadnych operacji arytmetycznych


    #szybsza metoda na odwracanie w poziomie z wykorzystaniem numpy, ktore jest napisane w C i jest znacznie szybsze niz pythonowe petle
    out =  np.flip(arr, axis = 1) #odwraca tablice, axis to oś 0 to wiersze, 1 to kolumny 3 to kanały (RGB), my chcemy odwrócić kolumny czyli oś 1. 
    save_image(output_path, out)
    return 1




    #poniżej ta sama funckjonalnośc bez użycia numpy flip (ale wolniejsza)

    # def cmd_horizontal_flip(kv: dict) -> int:
    # input_path, output_path = get_in_out(kv)
    #)  # array rodzaju uint8 (0-255). Problem z overflowem
    #out = np.empty_like(arr) # tworzymy pusta tablice o takim samym ksztalcie i typie jak arr
    # metoda shape zwraca krotke z wymiarami tablicy. Jak mamy tablice 2 wierze i 3 kolumny to shape zwroci (2,3)
    # rows = arr.shape[0] 
    # cols = arr.shape[1]    
    #skrypt na odwracanie w poziomie
    # for r in range(rows):
    #     first = 0
    #     last = cols - 1
    #     while first < last:
    #         left  = arr[r, last].copy()
    #         right = arr[r, first].copy()
    #         out[r, first] = left
    #         out[r, last]  = right
    #         first += 1
    #         last -= 1
    #     if first == last:
    #         out[r, first] = arr[r, first].copy()
    # save_image(output_path, out)
    # return 1


   

