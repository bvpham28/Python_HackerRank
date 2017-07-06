def average(array):
    sum_array = set(array)
    return sum(sum_array)/len(sum_array)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)