import mysignals as sig

_mean=0.0
_variance=0.0
_std = 0.0

def calc_standard_deviation(sig_src_arr):
    global _mean
    global _variance
    global _std

    for x in range(len(sig_src_arr)):
        _mean += sig_src_arr[x]
    _mean = _mean/len(sig_src_arr)

    for x in range(len(sig_src_arr)):
        _variance += (sig_src_arr[x]-_mean)**2
        # _variance += same as _variance = _variance + something
    _variance = _variance/(len(sig_src_arr))
    _std = _variance**(0.5)
    #to calculate square root raise power to half
    return _std
print(calc_standard_deviation(sig.InputSignal_1kHz_15kHz))
