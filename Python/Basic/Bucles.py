def potencia(num_mul):
    num_mul = num_mul * 2
    print(num_mul)
    if num_mul <= 999999 :
        potencia(num_mul)
    else:
        print("Finish!!!")


if __name__ == "__main__":
    potencia(1)