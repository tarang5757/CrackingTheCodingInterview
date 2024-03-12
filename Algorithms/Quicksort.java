public class Quicksort {
    public static void main(String[] args) {
        // Sample array to be sorted
        int[] array = { 8, 2, 5, 3, 9, 4, 7, 6, 1 };
        // Calls the quickSort function with the entire array
        quickSort(array, 0, array.length - 1);

        // Prints the sorted array
        for (int i : array) {
            System.out.println(i + " ");
        }

    }

    /**
     * Sorts a portion of the array using the Quicksort algorithm.
     *
     * @param array The array to sort.
     * @param start The starting index of the portion of the array to be sorted.
     * @param end   The ending index of the portion of the array to be sorted.
     */
    public static void quickSort(int[] array, int start, int end) {

        if (end <= start) {
            return; // Base case: if the sub-array is empty or has one element, it's already sorted
        }

        // Partition the array and get the pivot's correct position
        int pivot = partition(array, start, end);

        // Recursively apply quickSort to the sub-arrays before and after the pivot
        quickSort(array, start, pivot - 1); // Left sub-array
        quickSort(array, pivot + 1, end); // Right sub-array

    }

    /**
     * Partitions the array around a pivot such that elements less than the pivot
     * are on the left, and elements greater than the pivot are on the right.
     *
     * @param array The array to partition.
     * @param start The starting index for the partitioning.
     * @param end   The ending index for the partitioning.
     * @return The index of the pivot after partitioning.
     */
    public static int partition(int[] array, int start, int end) {

        // Choose the rightmost element as the pivot
        int pivot = array[end];
        int i = start - 1; // Pointer for the greater element

        // Traverse through all elements, rearranging elements around the pivot
        for (int j = start; j <= end - 1; j++) {
            // If current element is smaller than the pivot, swap it with the greater
            // element pointed by i
            if (array[j] < pivot) {
                i++; // Move the pointer for the greater element
                // Swap elements at i and j
                int temp = array[i];
                array[i] = array[j];
                array[j] = temp;
            }
        }
        // Swap the pivot with the element at i+1, so that pivot is at its correct
        // sorted position
        i++;
        int temp = array[i];
        array[i] = array[end];
        array[end] = temp;

        // Return the pivot's position
        return i;

    }

}
