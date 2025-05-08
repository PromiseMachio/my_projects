public class MethodsOverride{
    static int plusMethodInt(int x, int y){
	return x + y;
    }
    static double plusMethodDouble(double x, double y){
	return x + y;
    }
    static int multipyMethodInt(int x, int y){
	return x * y;
    }
    static double multiplyMethodDouble(double x, double y){
	return x * y;
    }
    static int divisionMethodInt(int x, int y){
	return x / y;
    }
    static double divisionMethodDouble(double x, double y){
	return x / y;
    }
					    
    public static void main(String[] args){
	int myNum1 = plusMethodInt(16, 17);// create a plus object on int
	double myNum2 = plusMethodDouble(12.8, 18.9);// create a plus object on double
	int myNum3 = multipyMethodInt(12,7);// create a multiply method on int
	double myNum4 = multiplyMethodDouble(37.9, 12.9);// create multiply on double
	int myNum5 = divisionMethodInt(81, 9);// create a division object on int
	double myNum6 = divisionMethodDouble(123.9, 17.9);//create a division object on double
	// Outputs and the results of the new objects created
	System.out.println("Int of addition of 16 and 17  is :" + myNum1);
	System.out.println("Double of addition 12.8 and 18.9 is:" + myNum2);
	System.out.println("Int of multiplication 12 and 7 is:" + myNum3);
	System.out.println("Double of multiplication of 37.9 and 12.9 is:" + myNum4);
	System.out.println("Int of the division 81 by 9 is:" + myNum5);
	System.out.println("Double of the division 123.9 by 17.9 is:" + myNum6);
    }
}
// Remember there's an overloading of methods where they have same names but different parameters.	    
	
