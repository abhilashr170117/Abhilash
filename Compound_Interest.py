#Python program to calculate compound interest

p=eval(input("Enter the principal amount"))
r=eval(input("Enter the rate"))
n=eval(input("Enter the time in years"))
def compound_interest(p,r,n):
	amount=p*(pow((1+r/100),n))
	return amount
amount=compound_interest(p,r,n)
ci=amount-p
print("compound interest is : ",ci)
