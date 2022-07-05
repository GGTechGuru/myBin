// Pseudocode:
//   Get the user/login name
//   Read /etc/passwd line by line
//   Split each line by ":" and get the login name & full-name fields
//   If the login name matches, split the full name by " " and
//   return the first name.
//

import java.io.FileReader;
import java.io.BufferedReader;


public class MyName {

public final int UNAME_INDEX=0;
public final int NAME_INDEX=4;

    public String getFirstName() {

        String firstName = null;
    
        try {

            String userName = System.getProperty("user.name");

            BufferedReader br=new BufferedReader(new FileReader("/etc/passwd"));

            String pwdEntry;

            while ((pwdEntry=br.readLine()) != null) {

               // System.out.println(pwdEntry);
        
               String[] splitEntry = pwdEntry.split(":");
        
               if (userName.equals(splitEntry[UNAME_INDEX])) {
        
                   String fullName = splitEntry[NAME_INDEX];
        
                   firstName = fullName.split(" ")[0];
        
                   break;
               }
        
               
            }
        }
        catch(Exception e) {

            System.out.println("EXCEPTION: " + e.getMessage());
        }

        return firstName;
    }

    public static void main(String args[]) {
        System.out.println((new MyName()).getFirstName());
    }
}
