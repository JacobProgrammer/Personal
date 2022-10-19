
/**
 * Calculates Home Prices and Preferences
 * All values for budget before 1,000,000 are without the zeros
 * e.g. 600 = 600,000
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
   
   public static void main(String[] args)
    {
        System.out.println("Hello! I will help you find the home of your dreams");
        Scanner homestate = new Scanner(System.in);
        
        System.out.println("What state are you shopping in?");
        String readHomestate = homestate.nextLine();
        int userPrice = price();
        if (readHomestate.equals(("Alabama")) || readHomestate .equals(("alabama")))
            if (userPrice > 1000000)
            {
                System.out.println("The optimal city for you to shop in is Orange Beach");
            }
        
            else if (userPrice < 999 && userPrice > 500)
            {   
                System.out.println("The optimal city for you to shop in is Vesatvia Hills");
            }
            else 
            {
                System.out.println("The optimal city for you to shop in is Hoover");
            }
            
        if (readHomestate.equals(("Alaska")) || readHomestate.equals(("alaska")))
            if (userPrice > 1000000)
            {
                System.out.println("The optimal city for you to shop in is The optimal city for you to shop is Juneau");
            }
        
            else if (userPrice < 999 && userPrice > 500)
            {
                System.out.println("The optimal city for you to shop in is Anchorage");
            }
        
            else
            {
                System.out.println("The optimal city for you to shop in is Fairbanks");
            }
        
        if (readHomestate.equals((
    }
}
