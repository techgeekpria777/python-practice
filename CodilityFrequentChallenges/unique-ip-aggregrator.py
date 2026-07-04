def most_frequent_ip(ips):
    count = {}
    for ip in ips:
        count[ip] = count.get(ip, 0) + 1
    best_ip = None
    best_count = 0
    for ip, count in count.items():
        if count > best_count:
            best_ip = ip
            best_count = count
    return best_ip

#the production way with Counter
from collections import Counter
def most_frequent_ip_counter(ips):
    return Counter(ips).most_common(1)[0][0]