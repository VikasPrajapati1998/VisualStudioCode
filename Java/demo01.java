import java.util.Scanner;

public class demo01 {
    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        System.out.print("Enter you name : ");
        String name = scn.nextLine();
        System.out.println("Hello Programmer " + name);
        scn.close();
    }
}

