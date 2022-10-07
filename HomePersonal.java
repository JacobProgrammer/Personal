
/**
 * Calculates Home Prices and Preferences
 *
 * @author (Jacob Olshanskiy)
 * @version (10-6-22)
 */
import java.util.Scanner;

public class HomePersonal
{
   public static int price()
    {
        Scanner price = new Scanner(System.in);
        System.out.println("What is your price range");
        int readPrice = price.nextInt();
        price.nextLine();
        return readPrice;
    }
    
   public static String greeting()
   {
       Scanner greeting = new Scanner(System.in);
       System.out.println("Great let me do some research");
       String readGreeting = greeting.nextLine();
       return readGreeting;
   }
   
   public static void main(String[] args)
    {
        System.out.println("Hello! I will help you find the home of your dreams");
        Scanner homestate = new Scanner(System.in);
        System.out.println("What state are you shopping in?");
        String readHomestate = homestate.nextLine();
        if (readHomestate == "Alabama")
        {
            int userPrice = price();
            greeting();
            if(userPrice > 1000000)
            {
                System.out.println("The optimal city for you to shop in is Orange Beach");
            }
            else if(999 > userPrice && userPrice > 500)
            {
                System.out.println("The optimal city for you to shop in is Vesatvia Hills");             
            }
            else
            {
                System.out.println("The optimal city for you to shop in is Hoover"); 
            }
        }
    }
}