def divide(x,y):
    power = 32
    y_power = (y << power)
    result = 0
    while x >= y :
        while x < y_power :
            y_power >>= 1
            power -= 1
        result += (1<<power)
        x-=y_power
    return result

if __name__ == "__main__":
    x,y = 25, 5
    print divide(x,y)
