a = str(input('Enter your Name:'))
Name = str
print('Hello', a)
print('******* Welcome to OFFERBAZAR.com*******')
print('Are you the employee of one of the following company ?')
print('1)ABz\n2)W\n3)Star\n YES or NO')
w = str(input('Enter your ans: '))
if w == 'YES' :
     print ('YAY!! You can avail super offers and\n Follow these easy steps to grab exciting offers')
     a = int(input("Enter your recent achieved target amount :"))
     #a = Achieved target
     if a == 100000 :
         Amount = 100000*0.10
         print ("You get incentive of 10% Incentive amount ", Amount)
     if a == 200000 :
         Amount = 100000*0.12
         print ("You get incentive of 12%  Incentive amount ", Amount)
     if 100000<a<200000 :
         Amount = 100000*0.10
         print ("You get incentive of 10% Incentive amount ", Amount)
     if a > 200000 :
         Amount = 100000*0.12
         print ("You get incentive of 12%  Incentive amount ", Amount)
         print ("CONGRATULATIONS !! \n YOU WILL ALSO GET A FREE MOBILE PHONE")  
         Brands = ['Apple','Realme','Samsung']
         print('Which mobile brand would you like to choose from the list.')
         b = str(input('Enter Brand:'))
         if b in Brands :
             print('Thanks for proceeding')
         
         if b == 'Apple' :
              print('_Model: 1)Iphone SE 2020 \n Operating system: iOS \n Screen: 4.7 inch LCD display \n Rear camera: 12 Megapixel (wide angle) \n Front camera: 7 Megapixel \n Storage: 3GB \n Colours available: Red\nWhite\nBlack \n Price: Starting from Rs.29,999')    
              print('You will receive your product in 3-5 working days \n Continue Shopping')
              
     if b =='Realme' :
              print ('Model: Realme X7 MAX \n Operating system: android  \n Screen: 6.43 HD+ display \n Rear camera:Triple Rear camera (64MP + 8MP + 2MP) \n Front Camera: 16MP \n Storage: 8GB \n Colours available: Black\nSilver \n Price: Rs.26,000')
              print('You will receive your product in 3-5 working days \n Continue Shopping')
     else :
          print ("Better luck next time")  
else :
    print ('Thanks for your response \n ..Continue your shopping..')
      

a = int(input('Enter amount spent on shopping:'))
if 1000<a<= 3000 :
    print ('You get discount of 20% on your purchase of amount Rs',a)
    print ('You have to pay only Rs. -', a-(a*0.2))
if 1000<a<= 5000 :
    print('You get discount of 35% on your purchase of amount Rs',a)
    print ('You have to pay only Rs.-', a-(a*0.35)) 
else :
    print('Buy more to avail discount')

c = str(input('Do you want to proceed to pay? \n YES or NO :')) 

if c == 'YES' :
    print('Select payment mode')
    print('UPI')
    print('Net Banking')
    print('COD')
    d = str(input('Enter your payment mode:')) 
v = ['UPI','Net Banking','COD']
if v == ['UPI','Net Banking','COD'] :
    print('Thanks for shopping \n Your order will deliver soon')
else :
    print ('..Continue your shopping..')

print('For more OFFERS and DISCOUNT \n *** Play an easy Game ***')
t = str(input ('Would you like to try your luck \n YES or NO \n Enter your response :'))
if t == 'YES':
    print(' Let us Play!')
    import random
    List =[0,1,2,3,4,5]
    a = int(input('Enter any number from 0 to 5 :'))
    b = random.randrange(5)
    print('The number is -', b)
    if a == b :
        print('Yay!! You won the price.')
    else :
        print (' Better luck next time..')
else :
    print('****Thank you for shopping**** \n VISIT AGAIN')
         

