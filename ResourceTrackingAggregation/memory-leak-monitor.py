def memory_leak_monitor(ram, K):
    current = 0
    for mem in range(1, len(ram)):
        if ram[mem] > ram[mem-1]:
            current += 1
            if current >= K:
                return True
        else:
            current = 0
    return False

def main():
    ram = [512, 520, 530, 525, 540, 550, 560]
    print(memory_leak_monitor(ram, 3))

if __name__ == "__main__":
    main()