import java.util.*;

class TopKFrequent {
    public static int[] topKFrequent(int[] nums, int k) {
        // iterate through the entire array and use a hashmap
        // hashmap key will be the integer array number
        // hashmap value will be the count of that number
        HashMap<Integer, Integer> map = new HashMap<>();

        // priority queue to sort, sort based on the hash -> Integer, compare(hm.)map
        // values
        PriorityQueue<Integer> pq = new PriorityQueue((a, b) -> Integer.compare(map.get(a), map.get(b)));

        for (int i : nums) {
            // put in i, and if i has a count, return i otherwise return 0
            map.put(i, map.getOrDefault(i, 0) + 1);
        }

        for (Integer i : map.keySet()) {
            pq.add(i);

            // way to improve runtime is to remove a low value if the size is bigger than k
            if (pq.size() > k)
                pq.poll(); // pq.poll will take off the smallest value.
        }
        // create a new array and populate it with the highest k counts
        int[] arr = new int[k];
        for (int i = 0; i < k; i++) {
            arr[i] = pq.poll(); // taking items off of the priority queue.
        }

        return arr;

    }

    public static void main(String[] args) {
        int[] arr = { 1, 1, 1, 2, 2, 3 };
        int[] result = topKFrequent(arr, 2);

        for (int i = 0; i < result.length; i++) {
            System.out.println(result[i]);
        }

    }
}