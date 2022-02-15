from distutils import command
from tkinter import W
from Profile import Profile
from Profile import Post
from pathlib import Path
import a2

p = Path()
def admin_create(profile: Profile, input1):
    '''Creates a file in admin mode'''
    try:
        index2 = -1
        #Finds path within input
        for i in reversed(range(len(input1)-3)):
            if (input1[i:i+4]==' -n '):
                index2=i
                break
        path1 = input1[2:index2]
        name_new_file =  input1[index2+4:]
        name_new_file = name_new_file + '.dsu'
        p = Path(path1) / name_new_file
        dir_path = Path(".") / path1

        if not dir_path.exists():
        #Checks if the path is valid
            print('ERROR. Invalid path.')
            return 'opened'
        else:
            if p.exists():
                path1 = str(Path(path1) / name_new_file)
                open_file(profile, path1)
                #returns opened to signify error
                return 'opened'
            elif not p.exists():
            #If the file does not exist, it gets created
                p.touch()
        new_path = str(Path(path1) / name_new_file)
        #Returns the path for a2 to use to save
        return new_path
    except:
        print('ERROR')
        #returns opened to signify error
        return 'opened'



def open_file(profile: Profile, path1):
    ''' Opens/Loads a file '''

    if path1[-4:] != '.dsu':
    #Checks if the file is of dsu type
        print('ERROR')
        return

    p = Path(".") / path1
    if not p.exists():
    #Checks if the file to be loaded exists
        print('ERROR. Does not exist')
        return
    profile.load_profile(path1)
    #Prints loaded file simple contents
    print("Username is", profile.username)
    print("Password is", profile.password)
    if profile.bio != "":
        print("Bio is", profile.bio)
    print("File has been loaded successfully")


def edit_file(profile: Profile, input1):
    '''Edits contents of the file'''
    try:
        temp = input1[2:]

        #Checks what to split by
        #Depends on what type of quotations are used: double or single
        ctr = 0
        for i in input1:
            if i=='\"':
                ctr=1
            elif i=='\'':
                ctr=2
        if ctr == 1:
            c_list = temp.split("\"")
            c_list = c_list[0:-1]
        elif ctr == 2:
            c_list = temp.split("\'")
            c_list = c_list[0:-1]
        else:
            c_list = temp.split(" ")
        #Loops through operations of editing
        for i in range(0, len(c_list), 2):
            strip_cmd = c_list[i].strip()
            if strip_cmd == '-usr':
            #Edit username
                if not " " in c_list[i+1] and c_list[i+1].strip() != '':
                    profile.username = c_list[i+1]
                    profile.save_profile(profile.dsuserver)
            elif strip_cmd == '-pwd':
            #Edit password
                if not " " in c_list[i+1] and c_list[i+1].strip() != '':
                    profile.password = c_list[i+1]
                    profile.save_profile(profile.dsuserver)
            elif strip_cmd == '-bio':
            #Edit bio
                if c_list[i+1].strip() != '':
                    profile.bio = c_list[i+1]
                    profile.save_profile(profile.dsuserver)
            elif strip_cmd == '-addpost': 
            #Adds a post
                if c_list[i+1].strip() != '':
                    profile.add_post(Post(entry = c_list[i+1]))
                    profile.save_profile(profile.dsuserver)
            elif strip_cmd == '-delpost':
            #Deletes a post based on index
                try:
                    profile.del_post(int(c_list[i+1]))
                    profile.save_profile(profile.dsuserver)
                except: 
                    print('ERROR')
                    return
            else:
            #If the operation doesn't exist
                print('ERROR')
                return
    except:
        print('ERROR')
        return

    
def print_file(profile: Profile, input1):
    '''Prints contents of the file'''
    try:
        temp1 = input1[2:]
        command_list = temp1.split(" ")
        #Loops through operations of printing
        for i in range(0, len(command_list)):
            cmd = command_list[i].strip()
            if cmd == '-usr':
            #Prints username
                print("Username:", profile.username)
            elif cmd == '-pwd':
            #Prints password
                print("Password:", profile.password)
            elif cmd == '-bio':
            #Prints bio
                print("Bio:", profile.bio)
            elif cmd == '-posts':
            #Prints all posts
                for post1 in range(len(profile._posts)):
                    print(str(post1) + '.', profile._posts[post1].get_entry())
            elif cmd == '-post':
            #Prints specific post based on index
                num1 = int(command_list[i+1])
                print(str(i) + '.', profile._posts[num1].get_entry())
            elif cmd == '-all':
            #Prints all contents
                print("Username:", profile.username)
                print("Password:", profile.password)
                print("Bio: ", profile.bio)
                for post1 in range(len(profile._posts)):
                    print(str(post1) + '.', profile._posts[post1].get_entry())
    except:
        print('ERROR')
        return


def interface_edit(profile: Profile):
    '''Edits the file in user interface mode'''

    print("What would you like to edit")
    print("usr: Username")
    print("pwd: Password")
    print("bio: Bio")
    print("addpost: Add a post")
    print("delpost: Delete a post")
    try:
        cmd2 = input()
        c_list = cmd2.split(" ")
        #Loops through operations of editing in interface/non admin mode
        #Checksto make sure entries are not empty strings
        for i in range(0, len(c_list)):
            cmd1 = c_list[i]
            if cmd1 == 'usr':
            #Edits the username
                temp_user = input("Enter a new username: ")
                if not " " in temp_user and temp_user.strip() != '':
                    profile.username = temp_user
                    profile.save_profile(profile.dsuserver)
            elif cmd1 == 'pwd':
            #Edits the password
                temp_pass = input("Enter a new password: ")
                if not " " in temp_pass and temp_pass.strip() != '':
                    profile.password = temp_pass
                    profile.save_profile(profile.dsuserver)
            elif cmd1 == 'bio':
            #Edits the bio
                temp_bio = input("Enter a new bio: ")
                if temp_bio.strip() != '':
                    profile.bio = temp_bio
                    profile.save_profile(profile.dsuserver)
            elif cmd1 == 'addpost':
            #Adds a post
                entry1 = input("What entry to add: ")
                if entry1.strip() != '':
                    profile.add_post(Post(entry = entry1))
                    profile.save_profile(profile.dsuserver)
            elif cmd1 == 'delpost':
            #Deletes a post
                integer1 = input("What ID to delete: ")
                try:
                    profile.del_post(int(integer1))
                    profile.save_profile(profile.dsuserver)
                except:
                    print('ERROR')
                    return
            else:
            #For unknown operations entered
                print('ERROR')
                return
    except:
        print('ERROR')
        return

def interface_print(profile: Profile):
    ''' Prints file contents in user interface mode '''
    try:
        print("What would you like to print")
        print("usr: Username")
        print("pwd: Password")
        print("bio: Bio")
        print("posts: Posts")
        print("post: Specific post by ID")
        print("all: All content stored in profile object")
        cmd2 = input()
        c_list = cmd2.split(" ")
        #Loops through print operations
        for i in range(0, len(c_list)):
            cmd1 = c_list[i]
            if cmd1 == 'usr':
            #Prints username
                print("Username:", profile.username)
            elif cmd1 == 'pwd':
            #Prints password
                print("Password:", profile.password)
            elif cmd1 == 'bio':
            #Prints bio
                print("Bio:", profile.bio)
            elif cmd1 == 'posts':
            #Prints posts
                for post1 in range(len(profile._posts)):
                    print(str(post1) + '.', profile._posts[post1].get_entry())
            elif cmd1 == 'post':
            #Prints specific post based on ID integer
                num1 = int(input("ID of post (integer): "))
                print(str(num1) + '.', profile._posts[num1].get_entry())
            elif cmd1 == 'all':
            #Prints all contents
                print("Username:", profile.username)
                print("Password:", profile.password)
                print("Bio: ", profile.bio)
                for post1 in range(len(profile._posts)):
                    print(str(post1) + '.', profile._posts[post1].get_entry())
            else:
                print('ERROR')
                return
    except:
        print('ERROR')
        return

def whitespace(str1):
    ''' Checks string for whitespace '''

    for i in str1:
        if i == ' ':
            return True
    return False
