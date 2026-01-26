package grind75.l0383;


import java.util.HashMap;
import java.util.Map;

public class RansomNotes {
    public boolean canConstruct(String ransomNote, String magazine) {
        Map<Character, Integer> hm = new HashMap<>();
        for (Character ch: magazine.toCharArray()) {
            int cur = hm.getOrDefault(ch, 0);
            hm.put(ch, cur + 1);
        }

        for (Character ch: ransomNote.toCharArray()) {
            if (!hm.containsKey(ch) || hm.get(ch) == 0) {
                return false;
            }
            else {
                hm.put(ch, hm.get(ch)-1);
            }
        }
        return true;
    }
}
    

