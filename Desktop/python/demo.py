#Armstrong number
# lower=int(input("Enter lower range:"))
# upper=int(input("Enter upper range:"))

# for num in range(lower,upper+1):
    # intialize sum
    # sum=0
    # # find the sum of the cube of each digit
    # temp=num
    # while temp>0:
    #     digit=temp%10
    #     sum+=digit**3
    #     temp//=10
    # if num==sum:
    #     print(num)    



# lower=int(input("Enter lower range:"))
# upper=int(input("Enter upper range:"))

# for num in range(lower,upper+1):
#     sum=0

#     temp=num
#     while temp>0:
#         digit=temp%10
#         sum=sum+digit**3
#         temp//=10
#     if num==sum:
#         print(num) 
   
# lower=int(input("Enter lower number:"))
# upper=int(input("Enter upper number:"))

# for num in range(lower,upper+1):
#     sum=0
#     temp=num

#     while temp>0:
#         digit=temp%10
#         sum+=digit**3
#         temp//=10
#     if (num==sum):
#         print(num)

# Palindrome
# palin=input("Enter any value:")
# rev=palin[::-1]

# if palin==rev:
#    print("Input: {}, Rev: {}".format(palin,rev))
#    print("string is palindrome")
# else:
#    print("Input: {}, Rev: {}".format(palin,rev))
#    print("string is not palindrome")

# palin=input("Enter any value:")
# rev=palin[::-1]

# if rev==palin:
#    print("input: {},Rev:{}".format(palin,rev))
#    print("String is palindrome.")
# else:
#    print("input: {},Rev:{}".format(palin,rev))
#    print("String is not palindrome.")


# prime number

lower=int(input("Enter lower number:"))
upper=int(input("Enter upper number:"))

print("prime numbers between",lower, "and",upper, "are:")
for num in range(lower,upper+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
               break
    else:
         print(num)


