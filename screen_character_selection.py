import tkinter as tk

class Screen_CharacterSelection (tk.Frame):

    def __init__ (self, master, roster, callback_on_selected):
        super().__init__(master)

       # Save the CharacterRoster  
        self.roster = roster

        # Save the method reference to which we return control after the player hits "Character Selected"
        self.callback_on_selected = callback_on_selected

        self.grid()
        self.create_widgets()
        

    def create_widgets (self):
        '''
        This method creates all of the widgets character selector page.
        The information about each character should be derived from self.roster, 
        which is a CharacterRoster loaded from battle_characters.txt. 
        The layout should NOT be hard-coded: if you re-order, alter, or remove entries 
        in battle_characters.txt, the layout should automatically reflect those changes. 
        
        ########
        
        The radio buttons on this page should all use the variable "self.character_index_index".  
        The values of the radio buttons must be a number equally the position of the character in the list. 
        For example, if the characters listed are Troll, Elf, Human, and Dwarf.  self.character_index would equal 0 
        for the Troll, 1 for the Elf, and so forth.  
        
        The variable self.character_index has been instantiated for your convenience below.
        
        ########

        Here is some sample code for including an image on a page:   (char is a Character object)
            
            imageSmall = tkinter.PhotoImage(file="images/" + char.small_image);
            w= tkinter.Label (self,
                        image = imageSmall, 
                         )
            w.photo = imageSmall # saving the image as a property is required for "saving" the image. It's odd.

            w.grid (ADD PARAMETERS HERE)
        '''
        self.character_index = tk.StringVar()
        self.character_index.set(None)
        
        row_num = 1

        # headers
        tk.Label(self, text = "Hit Points", font = "Helvetica 16 bold").grid(row = 0, column = 2, sticky = tk.N)
        tk.Label(self, text = "Dexterity", font = "Helvetica 16 bold").grid(row = 0, column = 3, sticky = tk.N)
        tk.Label(self, text = "Strength", font = "Helvetica 16 bold").grid(row = 0, column = 4, sticky = tk.N)

        # loops through all characters in character list 
        for index in range(len(self.roster.character_list)): 
            
            character = self.roster.character_list[index]

            # creates radio buttons and labels to display each character
            tk.Radiobutton(self, text = f"{character.name}", font = "Garamond 18", variable = self.character_index, value = index).grid(row = row_num, column = 0, sticky = tk.W)
            tk.Label(self, text = character.hit_points, font = "Garamond 20").grid(row = row_num, column = 2, sticky = tk.N+tk.S)
            tk.Label(self, text = character.dexterity, font = "Garamond 20").grid(row = row_num, column = 3, sticky = tk.N+tk.S)
            tk.Label(self, text = character.strength, font = "Garamond 20").grid(row = row_num, column = 4, sticky = tk.N+tk.S)
            
            # creates and displays image for each character 
            small_image = tk.PhotoImage(file="images/" + character.small_image)
            w = tk.Label(self, image = small_image)
            w.photo = small_image 
            w.grid(row = row_num, column = 1)

            # increment value 
            row_num += 1  

        # labels that don't do anything except to adjust column width 
        tk.Label(self, width = 10).grid(row = row_num + 1, column = 0, sticky = tk.N)
        tk.Label(self, width = 10).grid(row = row_num + 1, column = 2, sticky = tk.N)

        # add character selected button with function
        tk.Button(self, text = "Character Selected!", font = "Helvetica 18", highlightbackground = "#a62117", command = self.selected_clicked).grid(row = row_num + 1, column = 3, columnspan = 2, sticky = tk.N)


    def selected_clicked(self):
        ''' This method is to be called when the "Character Selected!" button is clicked. 
            Notice that it passes self.character_index back to the callback method. '''
         
        self.callback_on_selected(self.character_index.get())