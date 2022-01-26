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

        tk.Label(self, text = "Hit Points").grid(row = 0, column = 2, sticky = tk.N)
        tk.Label(self, text = "Dexterity").grid(row = 0, column = 3, sticky = tk.N)
        tk.Label(self, text = "Strength").grid(row = 0, column = 4, sticky = tk.N)

        for character in self.roster.character_list:
            # store in a variable?
            tk.Radiobutton(self, text = f"{character.name}", variable = self.character_index, value = self.roster.character_list.index(character)).grid(row = row_num, column = 0, sticky = tk.W)
            tk.Label(self, text = character.hit_points).grid(row = row_num, column = 2)
            tk.Label(self, text = character.dexterity).grid(row = row_num, column = 3)
            tk.Label(self, text = character.strength).grid(row = row_num, column = 4)
            
            small_image = tk.PhotoImage(file="images/" + character.small_image)
            w = tk.Label(self, image = small_image)
            w.photo = small_image 
            w.grid(row = row_num, column = 1)

            row_num += 1 

        tk.Button(self, text = "Character Selected!", command = self.selected_clicked(), width = 10).grid(row = row_num + 1, column = 0, sticky = tk.W + tk.E)

    def selected_clicked(self):
        ''' This method is to be called when the "Character Selected!" button is clicked. 
            Notice that it passes self.character_index back to the callback method. '''
         
        self.callback_on_selected(self.character_index.get())