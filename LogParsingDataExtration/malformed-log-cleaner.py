def log_cleaner(logs):
    clean = []
    for line in logs:
        try:
            user, action = line.split(",")
            clean.append((user, action))
        except ValueError:
            continue
    return clean

def log_cleaner_diff(logs):
    clean = []
    for line in logs:
        parts = line.split(",")
        if len(parts) == 2:
            clean.append((parts[0], parts[1]))
    return clean

def main():
    logs = ["user1,LOGIN", "", "user2,LOGOUT,extra_field", "corrupted_line", "user3"]
    print(log_cleaner(logs))
    print(log_cleaner_diff(logs))

if __name__ == "__main__":
    main()