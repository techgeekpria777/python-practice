def detect_latency(logs):
    breached = set()
    for line in logs:
        service, _, latency = line.split(",")
        if int(latency.replace("ms", "")) > 300:
            breached.add(service)
    return list(breached)

def main():
    logs = ["api_v1,200,50ms", "api_v2,500,1200ms", "api_v1,200,350ms"]
    print(detect_latency(logs))

if __name__ == "__main__":
    main()