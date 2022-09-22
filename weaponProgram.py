import weaponClass as w
import csv


'''
- Craete a program that will read the contents of the file 'weapons.txt'. Each record in the file represents the specs to a weapon.
- Create an instance of the weapon object for each record. 
- Create a dictionary that will contain the name of the weapon as the key and the number of bullets as the value. 
- Print out details of each weapon using the object's methods only (as per comments below). 
- Fire all bullets of the weapon and print a countdown of bullets remaining (run exe file to visualize, HINT: use end='\r' in your print statement).
- Print out the name of the weapon and the number of bullets from the dictionary.

HINT: Follow the comments for each line to help with the logic of the problem.
'''


# creating a file object to open the file in read mode
file = open("weapons.txt",'r')

# creating a csv object from the file object
content=csv.reader(file)

#using next function to skip header 
next(content,None)

#create an empty dictionary named 'weapons_dict'
weapons_dict={}

#using a for loop to iterate through every row of the csv file
for weapon_name,speed,range1 in content:

    name = weapon_name
    speed = speed
    range1 = range1

    # Creating an instance of Class Weapon
    weapon = w.Weapon(name,speed,range1)
    
    # adding the name as key and bullet count as value  to 'weapons_dict' dictionaring
    weapons_dict[name]= weapon.get_bullets()
   
    # print out the name of the weapon using the appropriate method of the object 
    print("\n Name:",weapon.get_name())
    # print out the speed of the weapon using the appropriate method of the object
    print(" Speed:",weapon.get_speed())
   
    # print out the range of the weapon using the appropriate method of the object
    print(" Range:",weapon.get_range())

    #storing the value of bullets since its random and 
    # keeps on changing everytime whenever get_bullets method is called
    bullet_cnt = weapon.get_bullets()

    # print out the number of bullets of the weapon using the appropriate method of the object
    print(" Bullets:",bullet_cnt)


    #use an input statement to halt the program and wait for the user - 
    input(" Press any key to fire the weapon")

    # storing the initial bullet count to a variable
    a= bullet_cnt 

    #loop to handle the firing of bullets
    #added +1 in order to check the functionality of the get_status() method

    for i in range(0,bullet_cnt+1):
        weapon.fire_bullet(a)
        a= weapon.get_bullets()                     # storing the current bullet which is reduced by 1
        print(" bullets remaining ...",a,end='\r')
    print('\n Current Status:',weapon.get_status()) 
  
        

#using a loop print out the name and number of bullets from the dictionary
print()
print("************Printing Weapon Name and Bullet Count using Dictionary**************")
for name ,no_of_bullets in weapons_dict.items():
    
    print('Name:',name,'Bullets',no_of_bullets)


    


    



