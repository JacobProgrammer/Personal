
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


            if (readHomestate.equals(("Alabama")) || readHomestate .equals(("alabama")) || (readHomestate.equals("AL")))
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
                

            if (readHomestate.equals(("Alaska")) || readHomestate.equals(("alaska")) || readHomestate.equals(("AK")))
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
            

            if (readHomestate.equals(("Arizona")) || readHomestate.equals(("arizona")) || readHomestate.equals(("AZ")))
                if (userPrice > 1000000)
                {
                    System.out.println("The optimal city for you to shop is Paradise Valley");
                }
            
                else if (userPrice < 999 && userPrice > 500)
                {
                    System.out.println("The optimal city for you to shop in is Scottsdale");
                }
            
                else
                {
                    System.out.println("The optimal city for you to shop in is Cave Creek");
                }
                

            if (readHomestate.equals(("Arkansas")) || readHomestate.equals(("arizona")) || readHomestate.equals(("AK")))
                if (userPrice > 1000000)
                {
                    System.out.println("The optimal city for you to shop is Fayetteville");
                }
            
                else if (userPrice < 999 && userPrice > 500)
                {
                    System.out.println("The optimal city for you to shop in is Bentonville");
                }
            
                else
                {
                    System.out.println("The optimal city for you to shop in is Rogers");
                }
                

            if (readHomestate.equals(("California")) || readHomestate.equals(("california")) || readHomestate.equals(("CA")))
              if (userPrice > 1000000)
              {
                System.out.println("The optimal city for you to shop is Beverly Hills");
              }
            
              else if (userPrice < 999 && userPrice > 500)
              {
                System.out.println("The optimal city for you to shop in is Los Angeles");
              }
            
              else
              {
                System.out.println("The optimal city for you to shop in is Canoga Park");
              }
                

            if (readHomestate.equals(("Colorado")) || readHomestate.equals(("colorado")) || readHomestate.equals(("CO")))
                if (userPrice > 1000000)
                {
                    System.out.println("The optimal city for you to shop is Aspen/Vail");
                }
            
                else if (userPrice < 999 && userPrice > 500)
                {
                    System.out.println("The optimal city for you to shop in is Denver");
                }
            
                else
                {
                    System.out.println("The optimal city for you to shop in is Lakewood");
                }
                

            if (readHomestate.equals(("Connecticut")) || readHomestate.equals(("connecticut")) || readHomestate.equals(("CT")))
                if (userPrice > 1000000)
                {
                    System.out.println("The optimal city for you to shop is Greenwich");
                }
            
                else if (userPrice < 999 && userPrice > 500)
                {
                    System.out.println("The optimal city for you to shop in is Ridgefield");
                }
            
                else
                {
                    System.out.println("The optimal city for you to shop in is Trumbull");
                }
                

            if (readHomestate.equals(("Deleware")) || readHomestate.equals(("deleware")) || readHomestate.equals(("DE")))
            
                if (userPrice > 1000000)
                {
                    System.out.println("The optimal city for you to shop is Greenwich");
                }
   
                else if (userPrice < 999 && userPrice > 500)
                {
                    System.out.println("The optimal city for you to shop in is Ridgefield");
                }
   
                else
                {
                    System.out.println("The optimal city for you to shop in is Trumbull");
                }

            if (readHomestate.equals(("Florida")) || readHomestate.equals(("florida")) || readHomestate.equals((("FL"))))
                if (userPrice > 1000000)
                { 
                    System.out.println("The optimal city for you to shop is Boca Raton/Palm Beach");
                }
   
                else if (userPrice < 999 && userPrice > 500)
                {
                    System.out.println("The optimal city for you to shop in is Highland Park");
                }
   
                else
                {
                   System.out.println("The optimal city for you to shop in is Sunny Isles");
                }

            if (readHomestate.equals(("Georgia")) || readHomestate.equals(("georgia")) || readHomestate.equals((("GA"))))
                if (userPrice > 1000000)
                { 
                  System.out.println("The optimal city for you to shop is Milton");
                }
     
                else if (userPrice < 999 && userPrice > 500)
                {
                  System.out.println("The optimal city for you to shop in is Atlana");
                }
     
                else
                {
                  System.out.println("The optimal city for you to shop in is Greensboro");
                }

            if (readHomestate.equals(("Hawaii")) || readHomestate.equals(("hawaii")) || readHomestate.equals((("HI"))))
                if (userPrice > 1000000)
                  { 
                    System.out.println("The optimal city for you to shop is Wailea");
                  }
       
                  else if (userPrice < 999 && userPrice > 500)
                  {
                    System.out.println("The optimal city for you to shop in is Kapolei");
                  }
       
                  else
                  {
                    System.out.println("The optimal city for you to shop in is Waianae");
                  }


            if (readHomestate.equals(("Idaho")) || readHomestate.equals(("idaho")) || readHomestate.equals((("ID"))))
                if (userPrice > 1000000)
                { 
                    System.out.println("The optimal city for you to shop is Ketchum");
                }
         
                else if (userPrice < 999 && userPrice > 500)
                {
                    System.out.println("The optimal city for you to shop in is Eagle");
                }
         
                else
                {
                    System.out.println("The optimal city for you to shop in is Star");
                }
        
    }
}
                  
        
          
        
    
