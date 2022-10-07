package projects;

import java.util.*;

public class Project_01 {

	static Scanner sc=new Scanner(System.in);
	public static void main(String []args) {
		System.out.println("Enter customerName");
		String name=sc.nextLine();
		System.out.println("Enter customerId");
		String id=sc.nextLine();
		bankAccount obj =new bankAccount(name,id);
		obj.show();
	}}

	 class bankAccount{
		float balance;
		float previousTransaction;
		String customerName;
		String customerId;
	
	bankAccount (String customerName,String customerId) {
		this.customerName =customerName;
		this.customerId =customerId;
	}
	 
	public void deposit(float amount) {
		if(amount!=0.0) {
		balance =balance + amount;
		previousTransaction = amount;
			
		}
		
	}
	public void withDraw(float amount) {
		if(amount!=0.0) {
			balance = balance - amount;
			previousTransaction = (-amount);
		}
		else {
			System.out.println("Not enough Money");
		}
	
	
}
	public void getPreviousTransaction() {
		if(previousTransaction> 0) {
			
			System.out.println("Deposit:"+ previousTransaction);
		}
			
		else if(previousTransaction < 0) {
			
		System.out.println("withDraw:"+ Math.abs(previousTransaction));
		}
		
		else {
			System.out.println("NO transaction occured");
		}
		
		
		
		
		
	}
	void show()
	{
		Scanner sc=new Scanner(System.in);
		char ch='\0';
		
		while(true){
			System.out.println("welcome: "+ customerName);
			System.out.println("your id is: "+ customerId);
			System.out.println("A. Balance ");
			System.out.println("B. Deposit");
			System.out.println("C. Withdrawal");
			System.out.println("D. Previous transaction");
			System.out.println("E. Exit");
			System.out.println("----------------------------------------------------");
			System.out.println("Enter an option");
			System.out.println("----------------------------------------------------");
			ch=sc.next().charAt(0);
			System.out.println("\n");
			System.out.println("\n");
			
			switch(ch){
			
			case 'A':
			case 'a':
				System.out.println("------------------------------------------------");
				System.out.println("balance = "+balance);
				System.out.println("------------------------------------------------");
				System.out.println("\n");
				break;
			
			case 'B':
			case 'b':
			System.out.println("----------------------------------------------------");
			System.out.println("Enter an amount to deposit");
			System.out.println("----------------------------------------------------");
			float amount =sc.nextFloat();
			deposit(amount);
			System.out.println("\n");
			System.out.println("\n");
			break;
			  
			case'C':
			case 'c':
				System.out.println("-------------------------------------------------");
				System.out.println("Enter the withdrawal amount");
				System.out.println("-------------------------------------------------");
				float amount2 =sc.nextFloat();
				withDraw(amount2);
				System.out.println("");
				
			break;
			
				
			case 'D':
			case 'd':
				System.out.println("-------------------------------------------------");
				System.out.println("previousTransaction");
				getPreviousTransaction();
				System.out.println("-------------------------------------------------");
				System.out.println("\n");
			
				break;
				
			case 'E':	
			case 'e':
				System.out.println("Thankyou for using our services");
				System.out.println("-------------------Exit------------------------------");
				System.exit(0); 
				
				default:
					System.out.println("Invalid operation");
					break;
			}
			 
		}
		
		
	}
	}
	
	
	
	
	
	

	

