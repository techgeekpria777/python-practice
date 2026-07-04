def smallest_missing_ids(ids):
    present = set(ids)
    id = 1
    while id in present:
        id += 1
    return id

def main():
    ids = [1, 3, 6, 4, 1, 2]
    print(smallest_missing_id(ids))

if __name__ == "__main__":
    main()