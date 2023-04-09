import time

def print_progress_bar(progress, end):
    print("[{0}{1}] {2}%".format("█" * progress, "-" * (end - progress), progress), end="\r")
    if progress == end:
        print()

for i in range(0, 101):
    print_progress_bar(i, 100)
    time.sleep(0.05)