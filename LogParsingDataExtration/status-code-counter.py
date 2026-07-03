from collections import Counter

def count_level_dif(logs):
    return dict(Counter(line.split()[1] for line in logs))

def count_levels(logs):
    counts = {}
    for line in logs:
        parts = line.split()
        level = parts[1]
        counts[level] = counts.get(level, 0) + 1
    return counts

def main():
    logs = ["10:00:00 INFO 200", "10:01:00 ERROR 500", "10:02:00 WARN 400"]
    #print(count_levels(logs))
    print(count_level_dif(logs))

if __name__ == "__main__":
    main()
