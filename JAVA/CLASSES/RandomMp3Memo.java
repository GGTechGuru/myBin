// ls /home/sbp366x24/Desktop/IPW/EASY_VOICE_RECORDER/*.mp3 | sort -R | head -1

/* Pseudocode:
   Open the location of the target MP3's
   Read the contents of the folder & select just mp3 files
   Take a random number from 0 to 1 less than the end of the list
   Return the full path of the file
*/

import java.util.ArrayList;
import java.io.File;

public class RandomMp3Memo {

    public String returnMemo() {

        // Get entries in dir
        String MEMO_FOLDER="/home/sbp366x24/Desktop/IPW/EASY_VOICE_RECORDER";

        File folder = new File(MEMO_FOLDER);
        File[] all_files = folder.listFiles();

        String fname = "";

        ArrayList<String> mp3s = new ArrayList<String>(0);

        for (File fObj : all_files) {
            fname = fObj.getName();

            // If it ends in ".mp3" append it to a list
            if (fname.endsWith(".mp3"))
                mp3s.add(fname);
        }


        // Get a random number between 0 and the end of the list
        int rand_index = (int)(Math.random() * mp3s.size());

        // Concatenate the directory path with the file name
        String mp3_path = MEMO_FOLDER + System.getProperty("file.separator") + mp3s.get(rand_index);

        // Return the concatenated path
        return mp3_path;
    }

    public static void main(String args[]) {

        System.out.println((new RandomMp3Memo()).returnMemo());

    }
}
