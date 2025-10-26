class chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()

    
    def menu(self):
        user_input = input("""Welcome to chatbook !! How would you like to procees.
                           1. Press 1 to Signup
                           2. Press 2 to login
                           3. Press 3 to write a post
                           4. Press 4 to message a friend
                           5. Press any key to exit
        """)

        if user_input == '1':
            self.signup()
        elif user_input == '2':
            self.signin()
        elif user_input == '3':
            self.my_post()
        elif user_input == '4':
            self.sendmsg()
        else:
            exit()

    def signup(self):
        email = input('enter your email id ->')
        pwd = input('setup your password here ->')
        self.username = email
        self.password = pwd
        print('you have successfully signed up')
        print("\n")
        self.menu()

    def signin(self):
        if self.username == '' and self.password == '':
            print('please signup first by pressing 1 in the main menu')
        else:
            uname = input('enter your username here ->')
            pwd = input('enter your password ->')
            if self.username == uname and self.password == pwd:
                print('you have successfully signed in')
                self.loggedin = True
            else:
                print('please enter the corrrect credentials')
        print("\n")
        self.menu()

    def my_post(self):
        if self.loggedin == True:
            txt = input('Enter your post here ->')
            print(f'you post has been posted')
        else:
            print('please login first')
        print("\n")
        self.menu()

    def sendmsg(self):
        if self.loggedin == True:
            txt = input('Enter your message here ->')
            frnd = input('enter the name of the friend')
            print(f'you message has been sent')
        else:
            print('please login first')
        print("\n")
        self.menu()



user1 = chatbook()