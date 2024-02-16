class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        // 1.sort each character in the array so that we can put them in the same category in a diff array


        //hashmap
        HashMap<String, List<String>> map = new HashMap<>();

        for(int i = 0; i < strs.length; i++){
            //break each word into its character and sort them and put them back into the string.
            //convert em into character array and then sort that character array.
            char[] charArray = strs[i].toCharArray();
            Arrays.sort(charArray);


            //Convert that sorted char array into string again.
            String sortedString = new String(charArray);

            //check if the map contains the key and if it doesn't make a new entry for that key and its value to be a list.
            if(!map.containsKey(sortedString)){
                //add the key and its value to be a new arraylist to that we can add future anagram words.
                map.put(sortedString, new ArrayList<>());
            }
            //the key already exists so add that key to the array.
            //the value is an array.  add the word to that array.
            map.get(sortedString).add(strs[i]);
        }

        //return new multidimensional array.
        return new ArrayList<>(map.values());

  


        
    }
}