import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 5780444792 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    a=0.083
    alpha = 1 - p
    loc = x.max()
    n = len(x)
    divisor=np.power(alpha,(1/n))
    return loc, \
           round(((loc - a) / divisor + a),4)
