import tkinter as tk

class Screen_PrepareToBattle (tkinter.Frame):
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

        tk.Label(self, text = "You").grid(row = 0, column = 0, sticky = tk.N)
        tk.Label(self, text = "Computer").grid(row = 0, column = 1, sticky = tk.N)

        large_image = tk.PhotoImage(file="images/" + self.player.large_image)
        w = tk.Label(self, image = large_image)
        w.photo = large_image
        w.grid(row = 1, column = 0)

        large_image = tk.PhotoImage(file="images/" + self.computer.large_image)
        w = tk.Label(self, image = large_image)
        w.photo = large_image
        w.grid(row = 1, column = 1)

 
    def commence_battle_clicked(self):
        ''' This method is called when the Battle button is clicked. 
            It passes control back to the callback method. '''         
        self.callback_on_commence_battle()
            
        