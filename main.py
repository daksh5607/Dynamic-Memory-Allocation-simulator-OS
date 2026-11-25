from algorithms import first_fit, best_fit, worst_fit


def display_result(name, result, memory):
    print("\\n" + "=" * 45)
    print(name)
    print("=" * 45)
    print("Process Size\\tAllocated Block")

    for process, block in result:
        if block is None:
            print(f"{process}\\t\\tNot Allocated")
        else:
            print(f"{process}\\t\\tBlock {block}")

    print("\\nRemaining Memory:")
    for i, size in enumerate(memory):
        print(f"Block {i + 1}: {size}")

    print("Total Free Memory:", sum(memory))


print("DYNAMIC MEMORY ALLOCATION SIMULATOR")

n = int(input("\\nEnter number of memory blocks: "))
blocks = []

for i in range(n):
    size = int(input(f"Enter size of block {i + 1}: "))
    blocks.append(size)

m = int(input("\\nEnter number of processes: "))
processes = []

for i in range(m):
    size = int(input(f"Enter size of process {i + 1}: "))
    processes.append(size)

print("\\nOriginal Memory Blocks:", blocks)
print("Processes:", processes)

result1, memory1 = first_fit(blocks, processes)
result2, memory2 = best_fit(blocks, processes)
result3, memory3 = worst_fit(blocks, processes)

display_result("FIRST FIT ALGORITHM", result1, memory1)
display_result("BEST FIT ALGORITHM", result2, memory2)
display_result("WORST FIT ALGORITHM", result3, memory3)

print("\\n" + "=" * 45)
print("ALGORITHM COMPARISON")
print("=" * 45)
print("First Fit Allocated:", sum(1 for p, b in result1 if b is not None))
print("Best Fit Allocated:", sum(1 for p, b in result2 if b is not None))
print("Worst Fit Allocated:", sum(1 for p, b in result3 if b is not None))
