public class Main1_2{
    public static void main(Strings[] args){
	int x = 0;
	int y = 0;
	System.out.println("x and y are" + x + "and" + y);
	x++;
	System.out.println("But now x is" + x);
        ++x;
	System.out.println("The result for x now after the pre-increment" + x);
	System.out.println("Lets now reset x back to 0");
	x = 0;
	System.out.println("--------------------------------");
	y = x++;
	System.out.println("Whats the value of y?:" + y);
	System.out.println("Y has just given the post- increment of x");
	System.out.println("Therefore now x is " + x);
	System.out.println("--------------------------------");
	y = ++x;
	System.out.println("The pre-fix of x is given when (++x) and is" + y);
	System.out.println("Then x has a value" + x);
	System.out.println("--------------------------------");
