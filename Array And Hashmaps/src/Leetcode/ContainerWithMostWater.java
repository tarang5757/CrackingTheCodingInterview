package Leetcode;

public class ContainerWithMostWater {
    // each element in the array corresponds to height of the bar.
    public int maxArea(int[] height) {
        // two pointer method
        int pointerA = 0;
        int pointerB = height.length - 1;
        // max_arae is going to calculate area at each step
        int max_area = 0;

        // for loop
        for (int i = 0; i < height.length; i++) {
            // initialize and evaluate width
            int width = pointerB - pointerA;
            // initialize height
            int waterHeight = 0;

            // if the height of pointer b is bigger than pointer a height.
            if (height[pointerA] < height[pointerB]) {
                // now we initialize waterHeight to respond to pointerA bar height.
                waterHeight = height[pointerA];
                // get the max area and compare to see if its bigger than previous stored value
                // of maxArea.
                max_area = Math.max(max_area, waterHeight * width);
                // increament pointer to point to next element.
                pointerA++;
            }

            // same thing here instead we check if pointerB > pointerA
            else {
                waterHeight = height[pointerB];
                max_area = Math.max(max_area, waterHeight * width);
                pointerB--;
            }

        }
        // return the max area.
        return max_area;

    }

}
