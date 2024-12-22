# List of books represented by their titles
books = [
    "Harry Potter",
    "The Great Gatsby",
    "War and Peace",
    "Moby Dick",
    "Pride and Prejudice",
    "The Hobbit",
    "To Kill a Mockingbird",
    "The Catcher in the Rye",
    "Lord of the Rings",
]

# Function to print sorted books with titles and their lengths
def print_books(sorted_books):
    for book in sorted_books:
        print(f"{book} (Length: {len(book)})")

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if len(arr[j]) > len(arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if len(arr[j]) < len(arr[min_index]):
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and len(key) < len(arr[j]):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if len(L[i]) < len(R[j]):
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

# Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if len(x) < len(pivot)]
    middle = [x for x in arr if len(x) == len(pivot)]
    right = [x for x in arr if len(x) > len(pivot)]
    return quick_sort(left) + middle + quick_sort(right)

#print unsorted list of books
print("Unsorted list:\n")
print_books(books)

# Testing all sorting algorithms
import time

algorithms = {
    "Bubble Sort": bubble_sort,
    "Selection Sort": selection_sort,
    "Insertion Sort": insertion_sort,
    "Merge Sort": merge_sort,
    "Quick Sort": quick_sort
}

for name, sort_function in algorithms.items():
    books_copy = books.copy()
    start_time = time.time()
    sorted_books = sort_function(books_copy)
    end_time = time.time()
    print(f"\n{name} Results:")
    print_books(sorted_books)
    print(f"Execution Time: {end_time - start_time:.10f} seconds")