class Solution {
    public int maxArea(int[] height) {
        int pointerA = 0;
        int pointerB = height.length - 1;
        int max_area = 0;

        for (int i = 0; i < height.length; i++) {
            int width = pointerB - pointerA;
            int waterHeight = 0;

            if (height[pointerA] < height[pointerB]) {
                waterHeight = height[pointerA];
                max_area = Math.max(max_area, waterHeight * width);
                pointerA++;
            }

            else {
                waterHeight = height[pointerB];
                max_area = Math.max(max_area, waterHeight * width);
                pointerB--;
            }

        }
        return max_area;

    }
}