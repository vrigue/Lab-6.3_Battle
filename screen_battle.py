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
        tk.Label(self, text = "You").grid(row = 4, column = 0, sticky = tk.N)
        tk.Label(self, text = "Computer").grid(row = 4, column = 1, sticky = tk.N)
        
        player1_image = tk.PhotoImage(file="images/" + self.player1.large_image)
        w = tk.Label(self, image = player1_image)
        w.photo = player1_image
        w.grid(row = 5, column = 0)
        player2_image = tk.PhotoImage(file="images/" + self.player2.large_image)
        w = tk.Label(self, image = player2_image)
        w.photo = player2_image
        w.grid(row = 5, column = 1)

        tk.Label(self, text = str(self.player1.hit_points) + " HP").grid(row = 6, column = 0, sticky = tk.N)
        tk.Label(self, text = str(self.player2.hit_points) + " HP").grid(row = 6, column = 1, sticky = tk.N)

        
        
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
                                            
    def exit_clicked(self):
        ''' This method is called when the Exit button is clicked. 
            It passes control back to the callback method. '''        
        #self.callback_on_exit()
        pass
  
            
            
            
            