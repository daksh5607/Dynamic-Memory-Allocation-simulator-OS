def first_fit(blocks, processes):
    memory = blocks.copy()
    result = []

    for process in processes:
        allocated = False

        for i in range(len(memory)):
            if memory[i] >= process:
                result.append((process, i + 1))
                memory[i] -= process
                allocated = True
                break

        if not allocated:
            result.append((process, None))

    return result, memory


def best_fit(blocks, processes):
    memory = blocks.copy()
    result = []

    for process in processes:
        best_index = -1

        for i in range(len(memory)):
            if memory[i] >= process:
                if best_index == -1 or memory[i] < memory[best_index]:
                    best_index = i

        if best_index != -1:
            result.append((process, best_index + 1))
            memory[best_index] -= process
        else:
            result.append((process, None))

    return result, memory


def worst_fit(blocks, processes):
    memory = blocks.copy()
    result = []

    for process in processes:
        worst_index = -1

        for i in range(len(memory)):
            if memory[i] >= process:
                if worst_index == -1 or memory[i] > memory[worst_index]:
                    worst_index = i

        if worst_index != -1:
            result.append((process, worst_index + 1))
            memory[worst_index] -= process
        else:
            result.append((process, None))

    return result, memory
