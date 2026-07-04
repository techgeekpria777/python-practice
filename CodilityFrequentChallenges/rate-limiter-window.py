def rate_limiter(request_stream):
    last_seen = {}
    allowed = []
    for user, ts in request_stream:
        if user not in last_seen or ts - last_seen[user] >= 2:
            allowed.append((user, ts))
            last_seen[user] = ts
    return allowed

def main():
    request_stream = [("user1", 1), ("user2", 2), ("user1", 2), ("user1", 5)]
    print(rate_limiter(request_stream))

if __name__ == "__main__":
    main()