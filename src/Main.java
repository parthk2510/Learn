public class Main {
    public static void main(String[] args) {
        int[] nums = {11, 23, 34, 45, 67, 89, 47};
        int target = 67;
        int ans = linearSearch(nums, target);
        System.out.println(ans);

    }

    static int linearSearch(int[] arr, int target) {
        if (arr.length == 0) {
            return -1;
        }


        for (int i = 0; i < arr.length; i++) {
            int element = arr[i];
            if (element == target) {
                System.out.println("Element is at position " + i);
                return i ;
            }
        }
        return -1;

    }
}

