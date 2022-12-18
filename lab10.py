import logging

logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="a")

col = int(input())
logging.info(f"Users entered: {col}")
i = 0
while col != 0:
    if col - 64 >= 0:
        i += 1
        col -= 64
    elif col - 32 >= 0:
        i += 1
        col -= 32
    elif col - 16 >= 0:
        i += 1
        col -= 16
    elif col - 8 >= 0:
        i += 1
        col -= 8
    elif col - 4 >= 0:
        i += 1
        col -= 4
    elif col - 2 >= 0:
        i += 1
        col -= 2
    else:
        i += 1
        col -= 1
logging.info(f"Result: {i}")
print(i)
logging.info("Program ended")
