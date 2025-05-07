import java.util.Scanner;
public class Exercise_Quards{
    public static void main(Sting[] Strings){
	Scanner input = new Scanner(System in);
		

	System.out.print("Input a:");
	double a = input.nextDouble(); 
	System.out.print("Input b:");
	double b = input.nextDouble(); 
	System.out.print("Input c:");
	double c = input.nextDouble();

	double result = b*b - 4 * a * c;

	if (result > 0.0){
	    double r1 = (-b+math.pow (result, 0.5)) /  2.0 * a);
	    double r2 = ( -b-math.pow (result, 0.5)) /  2.0 * a);
            System.out.println("The roots for r1 is :" + r1 " and root for r2 is " + r2);

          
}else if (result == 0){
             double r1 = (-b /2 * a);
                System.out.println("The root of the quadratic equation is:" r1);
        }else {
            System.out.println("The quadratic equation has no root");
}

    }
}
       


    
    
	    
	   

	   
	
