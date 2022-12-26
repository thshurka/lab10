import logging

logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="a")

col = int(input("Введите число рублей"))
logging.info(f"Users entered: {col}")
i = 0
j = 0
k = 0
g = 0
m = 0
f = 0
d = 0
while col != 0:
    if col - 64 >= 0:
        i += 1
        col -= 64
    elif col - 32 >= 0:
        j += 1
        col -= 32
    elif col - 16 >= 0:
        k += 1
        col -= 16
    elif col - 8 >= 0:
        g += 1
        col -= 8
    elif col - 4 >= 0:
        m += 1
        col -= 4
    elif col - 2 >= 0:
        f += 1
        col -= 2
    else:
        d += 1
        col -= 1
logging.info(f"Result: {i,j,k,g,m,f,d}")
print(" Купюр по 64:",i," Купюр по 32:", j, " Купюр по 16:", k, " Купюр по 8:", g, " Купюр по 4:",m, " Купюр по 2:",f, " Купюр по 1:", d )
logging.info("Program ended")
