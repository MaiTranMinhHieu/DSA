def stable_bubble_sort_records(records):
    n = len(records)
    for i in range(n):
        for j in range(0, n-i-1):
            if records[j]['key'] > records[j+1]['key']:
                records[j], records[j+1] = records[j+1], records[j]
    return records

if __name__ == "__main__":
    arr = [{'key': 2, 'val': 'A'}, {'key': 1, 'val': 'B'}, {'key': 2, 'val': 'C'}]
    result = stable_bubble_sort_records(arr)
    print(result)