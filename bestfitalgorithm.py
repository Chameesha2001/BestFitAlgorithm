class MemoryBlock:
    def __init__(self, size):
        self.size = size
        self.allocated = False


class Process:
    def __init__(self, id, size):
        self.id = id
        self.size = size
        self.allocated_block = None


def best_fit(blocks, processes):
    for process in processes:
        best_block = None

        for block in blocks:
            # Find the best fit block that is large enough and not fully allocated
            if block.size >= process.size:
                if best_block is None or block.size < best_block.size:
                    best_block = block

        if best_block:
            # Allocate the block to the process and reduce the block size
            best_block.size -= process.size
            process.allocated_block = best_block

    return processes


def display_allocation(processes):
    print("\nProcess ID | Process Size | Allocated Block Size")
    print("-" * 40)
    for process in processes:
        if process.allocated_block:
            print(
                f"{process.id:<10} | {process.size:<12} | {process.allocated_block.size + process.size:<20}"
            )
        else:
            print(f"{process.id:<10} | {process.size:<12} | Not Allocated")


# Get user inputs for memory blocks and processes
def get_inputs():
    # Fixed block sizes of 200, 300, 400, 100, and 150
    block_sizes = [200, 300, 400, 100, 150]
    memory_blocks = []

    print("\nThe number of memory blocks is fixed at 5. The sizes for each block are as follows:")
    for i, size in enumerate(block_sizes):
        memory_blocks.append(MemoryBlock(size))
        print(f"Block {i + 1}: {size} units")

    print("\nEnter the number of processes:")
    num_processes = int(input())
    processes = []

    print("\nEnter the sizes of each process:")
    for i in range(num_processes):
        size = int(input(f"Size of Process {i + 1}: "))
        processes.append(Process(i + 1, size))

    return memory_blocks, processes


# Main program
if __name__ == "__main__":
    print("Welcome to the Best Fit Memory Allocation Simulator")
    memory_blocks, processes = get_inputs()
    allocated_processes = best_fit(memory_blocks, processes)
    display_allocation(allocated_processes)

    # Display remaining block sizes
    print("\nRemaining Memory Block Sizes:")
    for i, block in enumerate(memory_blocks, start=1):
        print(f"Block {i}: {block.size} units")
