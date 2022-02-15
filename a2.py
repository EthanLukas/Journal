from genericpath import exists
from pathlib import Path
from tkinter import E
import ui
from Profile import Profile
from Profile import Post


profile = Profile()

def run(admin, input1, command):
    global profile
    ''' Main function that manages inputs and conditions based on options and commands '''
    #Try and except format used to handle errors gracefully, by printing that there is an error and then with the function is called again, requesting new input 
    #The command as the first character in the input
    if admin == True:
    #Puts program into admin mode

        input1 = input()
        command = input1[:1]

        while(command!='Q' and command!='q'):
        #Loops until the user inputs to quit the program
            try:
                while((command.upper() != 'C' and command.upper() != 'O' and command.upper() != 'E' and command.upper() != 'P' and input1.upper() != 'Q') or len(input1)<=1):
                #Requests new input while the command is invalid
                    print('ERROR')
                    input1 = input()
                    command = input1[:1]

                while(input1[1] != ''):
                #Requests new input while the command is invalid
                    print('ERROR')
                    input1 = input()
                    command = input1[:1]

                if command.upper()=='C':                 
                #Creates a new file in the specified directory 
                    new_path = ui.admin_create(profile, input1)
                    if new_path != 'opened':
                        profile = Profile(dsuserver = new_path)
                        profile.save_profile(new_path)

                elif command.upper() == 'O':
                #Loads a file
                    try:
                        path1 = input1[2:]
                        ui.open_file(profile, path1)
                    except:
                        print('ERROR')
                
                elif command.upper() == 'E':
                #Edits the dsu file contents
                    ui.edit_file(profile, input1)

                elif command.upper() == 'P':
                #Prints data in the file loaded or created
                    ui.print_file(profile, input1)

                elif command.upper() == 'Q':
                #Quits program
                    quit()

                input1 = input()
                command = input1[:1]

            except:
            #Handles errors
                if command=='Q' or command=='q':
                    quit()
                print('ERROR.')
                input1 = input()
                command = input1[:1]
                run(admin, input1, command)
        #Program quit when loop ends (q entered)        
        quit()
                
              

    elif admin == False: 
        #Non-admin mode
        try:
            #Loops until user inputs Q to quit
            while(input1!='Q' and input1!='q'):

                while(input1.upper() != 'C' and input1.upper() != 'O' and input1.upper() != 'E' and input1.upper() != 'P' and input1.upper() != 'Q'):
                #Requests new input while the command is invalid
                    print('ERROR')
                    print('What would you like to do next?')
                    print('C. Create a new profile')
                    print('O. Open/load an existing profile')
                    print('E. Edit an existing profile')
                    print('P. Print')
                    print('Q. Quit')
                    input1 = input()
                    command = input1[:1]

                if command.upper()=='C':                    
                #Creates a new file 
                    try:
                        username1 = input("Enter username: ")
                        password1 = input("Enter password: ")
                        bio = input("Enter bio: ")
                        path2 = input("Enter path: ")
                        name1 = input('What would you like to name the profile: ')
                        if name1.strip() != '':
                            name1 = str(name1 + ".dsu")
                            p = Path(path2) / name1
                            new_path = str(path2 + "/" + name1)
                            new_path1 = str(Path(path2) / name1)
                            dir_path = Path(".") / path2

                            #Checks if the path is valid
                            if not dir_path.exists():
                                print('ERROR. Invalid path.')
                            else: 
                                if p.exists():
                                    ui.open_file(profile, new_path)
                                    print("File already exists, loaded instead.")
                                elif not p.exists():
                                    if username1.strip() != '' and password1.strip() != '' and ui.whitespace(username1) == False and ui.whitespace(password1) == False:
                                    #Checks if the username and password are empty or if they contain whitespace
                                        p.touch()
                                        profile = Profile(dsuserver = new_path1, username = username1, password = password1)
                                        if bio.strip() != '':
                                            profile.bio = bio
                                        profile.save_profile(new_path1)
                                    else:
                                        print('ERROR')
                        else:
                            print('ERROR')
                        
                    except:
                        print('ERROR')


                elif command.upper() == 'O':
                #Opens the file with given path
                    try:
                        path1 = input("Enter path to open: ")
                        ui.open_file(profile, path1)
                    except:
                        print('ERROR')
                

                elif command.upper() == 'E':
                #Edits file in user interface mode
                    ui.interface_edit(profile)


                elif command.upper() == 'P':
                #Prints contents of file in user interface mode
                    ui.interface_print(profile)

                elif command.upper() == 'Q':
                    quit()

                else:
                    print('ERROR')
                

                print('What would you like to do next?')
                print('C. Create a new profile')
                print('O. Open/load an existing profile')
                print('E. Edit an existing profile')
                print('P. Print')
                print('Q. Quit')

                #Takes input before looping again
                input1 = input()
                command = input1[:1]
            
            quit()

        except:
        #Error handlng
            if command=='Q' or command=='q':
                    quit()
            print('ERROR.')
            run(admin, input1, command)


if __name__ == '__main__':
    #Starts off the program with main menu
    print('Welcome to the ICS 32 Journal! Input Q to exit the program')
    print("Welcome! Do you want to create or load a DSU file (type 'c' to create or 'o' to open/load): ")

    input1 = input()
    command = input1[:1]
    while(input1.upper() != 'C' and input1.upper() != 'O' and input1.upper() != 'Q' and input1.upper()!='ADMIN'):
    #Requests new input while the command is invalid
        print('ERROR. Try again')
        input1 = input()
        command = input1[:1]
    if input1.upper() == 'Q':
        quit()

    #Checks whether to enter admin mode in run function
    admin = False
    
    if input1.upper() == 'ADMIN':
        admin = True
        print('Welcome to Admin Mode')
    else: 
        admin = False

    run(admin, input1, command)
