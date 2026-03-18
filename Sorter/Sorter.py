import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 1. Improved Logic: Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                yield arr, j, j + 1, False # False means 'not finished'
    yield arr, -1, -1, True # Signal that we are done!

# 2. AI Hint Logic (Kept your logic, just cleaned the text)
def get_ai_hint(arr):
    n = len(arr)
    swaps = sum(1 for i in range(n-1) if arr[i] > arr[i+1])
    if swaps < n * 0.2:
        return "AI Hint: Nearly sorted. Insertion Sort would be O(n)!"
    elif swaps > n * 0.7:
        return "AI Hint: Highly chaotic. Use QuickSort or MergeSort!"
    return "AI Hint: Standard distribution. Bubble Sort is fine but slow."

# 3. Visualization
def visualize():
    n = 20
    data = [random.randint(10, 100) for _ in range(n)]
    hint = get_ai_hint(data)

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.set_title(f"Sorting Visualizer\n{hint}", fontsize=12, pad=15)
    
    # Using your cool Indigo color
    bar_rects = ax.bar(range(len(data)), data, align="edge", color="#6366f1")
    
    # Set axis limits so the plot doesn't jump around
    ax.set_xlim(0, n)
    ax.set_ylim(0, 110)

    def update(frame):
        arr, idx1, idx2, is_done = frame
        
        for i, (rect, val) in enumerate(zip(bar_rects, arr)):
            rect.set_height(val)
            if is_done:
                rect.set_color("#10b981") # Success Green when finished!
            elif i == idx1 or i == idx2:
                rect.set_color("#ec4899") # Your Pink highlight
            else:
                rect.set_color("#6366f1") # Default Indigo
        
        return bar_rects

    # Increased interval to 100 for a smoother "visual" pace
    anim = FuncAnimation(fig, update, frames=bubble_sort(data), 
                          repeat=False, interval=100, cache_frame_data=False)
    plt.show()

if __name__ == "__main__":
    visualize()