if __name__=="__main__":
    numbers = [1,2,3,4,5,10]
    min_value = int(min(numbers))
    max_value = int(max(numbers))

    avg_value = 0
    for num in numbers:
        avg_value += num
    avg_value = avg_value / len(numbers)        

    print(f"Min: {min_value}\nMax: {max_value}\nAvg: {avg_value}")