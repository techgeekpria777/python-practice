def max_crashes(times):
    count = 0
    left = 0
    for right in range(len(times)):
        while times[right] - times[left] > 60:
            left += 1
        count = max (count, right - left + 1)
    return count

def main():
    times = [10, 12, 15, 65, 70, 72, 130]
    print(max_crashes(times))

if __name__ == "__main__":
    main()