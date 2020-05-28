import time


def progressbar(lst):
    try:
        start = start - 0
    except NameError:
        start = time.time()
    i = 0
    size = len(lst)
    for elem in lst:
        end = time.time()
        elapsed_time = end - start
        i += 1
        time_left = (0.01 * size) - (0.01 * i)
        percentage = 100 * i / size
        bars_number = int(percentage / 5)
        space_number = 20 - bars_number
        format_str = ''.join(["ETA: {time_left:.2f}s [{percentage:06.2f}%]",
                              "[{nul:=<{bars_number}s}>",
                              "{nul: >{space_number}s}]",
                              "{i: 5d}/{size:d} | elapsed time",
                              " {elapsed_time:.2f}s\r"])
        t = (time_left, percentage, i, size, elapsed_time)
        print(format_str.format(
            time_left=time_left,
            percentage=percentage,
            nul='',
            bars_number=bars_number,
            space_number=space_number,
            i=i,
            size=size,
            elapsed_time=elapsed_time
            ), end='')
        yield elem
