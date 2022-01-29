import tkinter as tk

class Screen_Battle (tk.Frame):
    def __init__ (self, master, player1, player2, callback_on_exit):
        super().__init__(master)
        print("test2")

        # Save references to the two player objects
        self.player1 = player1
        self.player2 = player2

        # Store the maximum number of hit points which are needed on the screen display.
        self.player1_max_hp = player1.hit_points
        self.player2_max_hp = player2.hit_points

        # Save the method reference to which we return control after this page Exits.
        self.callback_on_exit = callback_on_exit

        self.grid()
        self.create_widgets()
        
        
    def create_widgets (self):
        '''
        This method creates all of the (initial) widgets for the battle page.
        '''

        # attack button
        self.attack_bttn = tk.Button(self, text = "Attack!", font = "Helvetica 18", highlightbackground = "#a62117", command = self.attack_clicked)
        self.attack_bttn.grid(row = 0, column = 0, sticky = tk.W)

        # create labels for updating attacks 
        self.p1attack = tk.Label(self, text = '', font = "Garamond 17")
        self.p1attack.grid(row = 0, column = 1, sticky = tk.N)
        self.p2attack = tk.Label(self, text = '', font = "Garamond 17")
        self.p2attack.grid(row = 1, column = 1, sticky = tk.N)

        # creates headers
        tk.Label(self, text = "You", font = "Helvetica 18 bold").grid(row = 4, column = 0, sticky = tk.N)
        tk.Label(self, text = "Computer", font = "Helvetica 18 bold").grid(row = 4, column = 1, sticky = tk.N)
        
        # creates images of players' characters 
        player1_image = tk.PhotoImage(file="images/" + self.player1.large_image)
        w = tk.Label(self, image = player1_image)
        w.photo = player1_image
        w.grid(row = 5, column = 0)

        player2_image = tk.PhotoImage(file="images/" + self.player2.large_image)
        w = tk.Label(self, image = player2_image)
        w.photo = player2_image
        w.grid(row = 5, column = 1)

        # creates label to display HP + stores in variable for later updating
        self.player1_text_hp = tk.Label(self, text = f"{self.player1.hit_points}/{self.player1_max_hp} HP", font = "Garamond 20")
        self.player2_text_hp = tk.Label(self, text = f"{self.player2.hit_points}/{self.player2_max_hp} HP", font = "Garamond 20")
        self.player1_text_hp.grid(row = 6, column = 0, sticky = tk.N)
        self.player2_text_hp.grid(row = 6, column = 1, sticky = tk.N)

        # creates label for visual purposes 
        tk.Label(self).grid(row = 7, column = 0, sticky = tk.W)
        
        
    def attack_clicked(self):
        ''' This method is called when the user presses the "Attack" button.
            
            This method does the following:
            1) Calls the character.attack method for both the player and (if still alive) the computer.
            2) Updates the labels on the top right with the results of the attacks.
            3) Determines if there was a victor, and if so display that info 
            4) If there is a victor, remove the Attack button.  Create an Exit button to replace it.  

            To remove a widget, use the destroy() method. For example:
    
                self.button.destroy()   
        '''        

        # updates previously blank labels with text on who hit who and for how much
        self.p1attack['text'] = self.player1.attack(self.player2)
        if self.player2.hit_points > 0:
            self.p2attack['text'] = self.player2.attack(self.player1)

        # updates HP labels to display current HP levels
        self.player1_text_hp["text"] = f"{self.player1.hit_points}/{self.player1_max_hp} HP"
        self.player2_text_hp["text"] = f"{self.player2.hit_points}/{self.player2_max_hp} HP"
        
        # checks if either player has died, leaving the other victorious
        if self.player2.hit_points <= 0:
            win = str(self.player1.name) + " is victorious!"
            tk.Label(self, text = win, font = "Garamond 20", fg = "#a62117").grid(row = 2, column = 1, sticky = tk.N)

            # creates exit button and deletes attack button
            self.attack_bttn.destroy()
            tk.Button(self, text = "Exit!", font = "Helvetica 18", highlightbackground = "#a62117", command = self.exit_clicked).grid(row = 7, column = 1, sticky = tk.E)

        elif self.player1.hit_points <= 0:
            win = str(self.player2.name) + " is victorious!"
            tk.Label(self, text = win, font = "Garamond 20", fg = "#a62117").grid(row = 2, column = 1, sticky = tk.N)

            # creates exit button and deletes attack button
            self.attack_bttn.destroy()
            tk.Button(self, text = "Exit!", font = "Helvetica 18", highlightbackground = "#a62117", command = self.exit_clicked).grid(row = 7, column = 1, sticky = tk.E)
               
                                            
    def exit_clicked(self):
        ''' This method is called when the Exit button is clicked. 
            It passes control back to the callback method. '''        
        
        self.callback_on_exit()
        
  
            
            
            
            