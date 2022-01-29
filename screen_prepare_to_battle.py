import tkinter as tk

class Screen_PrepareToBattle (tk.Frame):
    def __init__ (self, master, player1, player2, callback_on_commence_battle):
        super().__init__(master)

        # Save player character object references
        self.player1 = player1
        self.player2 = player2
        
        # Save the method reference to which we return control after the player hits "Next"
        self.callback_on_commence_battle = callback_on_commence_battle
        
        self.create_widgets()
        self.grid()
        
    
    def create_widgets (self):
        '''
        This method creates all of the widgets the prepare to battle page.
        '''

        # create headers
        tk.Label(self, text = "You", font = "Helvetica 16 bold").grid(row = 0, column = 0, sticky = tk.N)
        tk.Label(self, text = "Computer", font = "Helvetica 16 bold").grid(row = 0, column = 1, sticky = tk.N)

        #insert images for selected characters
        player1_image = tk.PhotoImage(file="images/" + self.player1.large_image)
        w = tk.Label(self, image = player1_image)
        w.photo = player1_image
        w.grid(row = 1, column = 0)

        player2_image = tk.PhotoImage(file="images/" + self.player2.large_image)
        w = tk.Label(self, image = player2_image)
        w.photo = player2_image
        w.grid(row = 1, column = 1)

        # showing information / attributes of chosen characters
        tk.Label(self, text = f"{self.player1.hit_points} HP", font = "Garamond 18").grid(row = 3, column = 0, sticky = tk.N)
        tk.Label(self, text = f"{self.player1.dexterity} Dexterity", font = "Garamond 18").grid(row = 4, column = 0, sticky = tk.N)
        tk.Label(self, text = f"{self.player1.strength} Strength", font = "Garamond 18").grid(row = 5, column = 0, sticky = tk.N)

        tk.Label(self, text = f"{self.player2.hit_points} HP", font = "Garamond 18").grid(row = 3, column = 1, sticky = tk.N)
        tk.Label(self, text = f"{self.player2.dexterity} Dexterity", font = "Garamond 18").grid(row = 4, column = 1, sticky = tk.N)
        tk.Label(self, text = f"{self.player2.strength} Strength", font = "Garamond 18").grid(row = 5, column = 1, sticky = tk.N)

        # creates plain label for visual purposes 
        tk.Label(self).grid(row = 6, column = 0, sticky = tk.W)

        # add commence battle button and function
        tk.Button(self, text = "Commence Battle!", font = "Helvetica 18", highlightbackground = "#a62117", command = self.commence_battle_clicked).grid(row = 7, column = 1, sticky = tk.E)
    
 
    def commence_battle_clicked(self):
        ''' This method is called when the Battle button is clicked. 
            It passes control back to the callback method. '''         
        self.callback_on_commence_battle()
            
        