import threading
from queue import Queue
import math
from collections import defaultdict

# ==========================
# Exercise 1: Threaded Prime Checker
# ==========================

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def prime_worker(start, end, output):
    primes = [num for num in range(start, end) if is_prime(num)]
    output.put(primes)

def threaded_prime_checker(start, end, num_threads=4):
    threads = []
    output = Queue()
    step = (end - start) // num_threads
    for i in range(num_threads):
        t_start = start + i * step
        t_end = end if i == num_threads - 1 else t_start + step
        thread = threading.Thread(target=prime_worker, args=(t_start, t_end, output))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    result = []
    while not output.empty():
        result.extend(output.get())

    result.sort()
    print("Prime numbers:", result)


# ==========================
# Exercise 2: Threaded File Processing
# ==========================

def word_count_worker(lines, output):
    word_count = defaultdict(int)
    for line in lines:
        words = line.strip().split()
        for word in words:
            word_count[word.lower()] += 1
    output.put(word_count)

def threaded_word_count(file_path, num_threads=4):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    total_lines = len(lines)
    chunk_size = total_lines // num_threads
    threads = []
    output = Queue()

    for i in range(num_threads):
        start = i * chunk_size
        end = total_lines if i == num_threads - 1 else start + chunk_size
        thread = threading.Thread(target=word_count_worker, args=(lines[start:end], output))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    final_word_count = defaultdict(int)
    while not output.empty():
        partial = output.get()
        for word, count in partial.items():
            final_word_count[word] += count

    print("Word Frequencies:")
    for word, count in sorted(final_word_count.items()):
        print(f"{word}: {count}")


# ==========================
# Example Usage
# ==========================

if __name__ == "__main__":
    print("== Prime Number Checker ==")
    threaded_prime_checker(1, 100, num_threads=4)

    print("\n== Word Count from File ==")
    # Create a sample file for demonstration
    with open("sample_text.txt", "w") as f:
        f.write("This is a sample text file.\n")
        f.write("This file is used to test word count.\n")
        f.write("Word count is important in text processing.\n")

    threaded_word_count("sample_text.txt", num_threads=3)
