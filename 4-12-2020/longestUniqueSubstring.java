//Optimized Solution
// O(n) time, O(n) space
class Solution {
public int lengthOfLongestSubstring(String s) {
        if (s == null || s.length() == 0) return 0;
        if (s.length() == 1) return 1;
        int maxSubstring = 0;

        HashSet<Character> characters = new HashSet<Character>();
        int left = 0;
        int right = 1;
        characters.add(s.charAt(left));
        while (right != s.length()) {
                if(characters.contains(s.charAt(right))) {
                        maxSubstring = right - left > maxSubstring ? right - left : maxSubstring;
                        while (s.charAt(right) != s.charAt(left)) {
                                characters.remove(s.charAt(left));
                                left++;
                        }
                        left++;
                        right++;
                } else {
                        characters.add(s.charAt(right));
                        right++;
                }
        }
        maxSubstring = right - left > maxSubstring ? right - left : maxSubstring;
        return maxSubstring;
}
}


//BRUTE FORCE Solution
// O(n^2) time, O(n) space
class Solution {
public int lengthOfLongestSubstring(String s) {
        if (s.length() == 0) return 0;
        if (s.length() == 1) return 1;

        int maxSize = 1;
        for (int i = 0; i < s.length() - 1; i++) {
                for (int j = i + 1; j < s.length(); j++) {
                        String currSubstring = s.substring(i, j + 1);
                        if (isValid(currSubstring) && currSubstring.length() > maxSize) {
                                maxSize = currSubstring.length();
                        }
                }
        }
        return maxSize;
}

public boolean isValid (String substring) {
        HashSet<Character> characters = new HashSet<Character>();
        for (int i = 0; i < substring.length(); i++) {
                if (characters.contains(substring.charAt(i))) return false;
                characters.add(substring.charAt(i));
        }
        return true;
}
}
