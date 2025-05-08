class Animal{
    public void animalSound(){
	System.out.println("Animal make sounds");
    }
	    
    public void animalEat(){
	System.out.println("Animal eat ");
    }
}
//Subclass created overriding methods of the the superclass
class Dog extends Animal{
    public void animalSound(){
	System.out.println("The dog barks: Woof! Woof!");
    }
    public void animalEat(){
	System.out.println("The dog eats: Bones");
    }
}
class Pig extends Animal{
    public void animalSound(){
	System.out.println("The pig says: Weee! Weee!");
    }
    public void animalEat(){
	System.out.println("The pig eats:Trash");
    }
}
class Polymophisim{
    public static void main(String[] args){
	Animal myAnimal = new Animal(); //An object created for Animal.
	Dog myDog = new Dog (); //An object created for a Dog
	Pig myPig = new Pig ();//An object created for a Pig
	myAnimal.animalSound();
	myAnimal.animalEat();
	myDog.animalSound();
	myDog.animalEat();
	myPig.animalSound();
	myPig.animalEat();
    }
}
// NOTE: Running this code in the termial will require you to write this way.
//java Polymophisim
//Why shouldn't we include .java in the end of the statement Here is the catch :
//java is used to run compiled files .class file not source file like .java files.
