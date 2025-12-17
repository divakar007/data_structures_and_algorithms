class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> freq = new HashMap<>();

        for (int num: nums){
            freq.put(num, freq.getOrDefault(num, 0) + 1);
        }

        List<List<Integer>> counts = new ArrayList<>();

        for (int i=0; i<= nums.length; i++){
            counts.add(new ArrayList());
        }

        for (Integer num : freq.keySet()){
            int frequency = freq.get(num);
            counts.get(frequency).add(num);
        }

        int[] res = new int[k];
        int curr = 0;

        for (int i=counts.size()-1; i >= 0 && curr < k; i--){
            for (int num: counts.get(i)){
                res[curr] = num;
                curr += 1;
                if (curr == k){
                    return res;
                }
            }
        }

        return res;
    }
}