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
        #
        # TO DO
        #

        # attack button
        self.attack_bttn = tk.Button(self, text = "Attack", command = self.attack_clicked)
        self.attack_bttn.grid(row = 0, column = 0, sticky = tk.W)

        self.p1attack = tk.Label(self, text = '')
        self.p1attack.grid(row = 0, column = 1, sticky = tk.N)
        self.p2attack = tk.Label(self, text = '')
        self.p2attack.grid(row = 1, column = 1, sticky = tk.N)

        # headers
        tk.Label(self, text = "You").grid(row = 4, column = 0, sticky = tk.N)
        tk.Label(self, text = "Computer").grid(row = 4, column = 1, sticky = tk.N)
        
        #image of players
        player1_image = tk.PhotoImage(file="images/" + self.player1.large_image)
        w = tk.Label(self, image = player1_image)
        w.photo = player1_image
        w.grid(row = 5, column = 0)
        player2_image = tk.PhotoImage(file="images/" + self.player2.large_image)
        w = tk.Label(self, image = player2_image)
        w.photo = player2_image
        w.grid(row = 5, column = 1)

        # stating health
        self.player1_text_hp = tk.Label(self, text = str(self.player1.hit_points) + "/" + str(self.player1_max_hp) + " HP")
        self.player2_text_hp = tk.Label(self, text = str(self.player2.hit_points) + "/" + str(self.player2_max_hp) + " HP")
        self.player1_text_hp.grid(row = 6, column = 0, sticky = tk.N)
        self.player2_text_hp.grid(row = 6, column = 1, sticky = tk.N)

        

        
        
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
        #
        # TO DO
        #

        # make variables for the strings that update who hit who and for how much
        self.p1attack['text'] = self.player1.attack(self.player2)
        if self.player2.hit_points > 0:
            self.p2attack['text'] = self.player2.attack(self.player1)

        # ignore for now (this was to put hit points underneath)
        self.player1_text_hp["text"] = str(self.player1.hit_points) + "/" + str(self.player1_max_hp)
        self.player2_text_hp["text"] = str(self.player2.hit_points) + "/" + str(self.player2_max_hp)
        #tk.Label(self, text = self.player2_max_hp).grid(row = 6, column = 1, sticky = tk.N)
        
        # ignor for now (to update who won at the end)
        if self.player2.hit_points <= 0:
            win = str(self.player1.name) + " is victorious!"
            tk.Label(self, text = win).grid(row = 2, column = 1, sticky = tk.N)
            # quit button and delete attack button
            self.attack_bttn.destroy()
            tk.Button(self, text = "Exit!", command = self.exit_clicked).grid(row = 7, column = 1, sticky = tk.E)
        elif self.player1.hit_points <= 0:
            win = str(self.player2.name) + " is victorious!"
            tk.Label(self, text = win).grid(row = 2, column = 1, sticky = tk.N)
            # quit button and delete attack button
            self.attack_bttn.destroy()
            tk.Button(self, text = "Exit!", command = self.exit_clicked).grid(row = 7, column = 1, sticky = tk.E)
                                            
    def exit_clicked(self):
        ''' This method is called when the Exit button is clicked. 
            It passes control back to the callback method. '''        
        self.callback_on_exit()
        pass
  
            
            
            
            