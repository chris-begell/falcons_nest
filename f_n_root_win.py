


# ((((((((((((((((((((((((((((((((()))))))))))))))))))))))))))))))))
# ||||||||||||||||||||||||  IMPORT LIST  |||||||||||||||||||||||||||
# ((((((((((((((((((((((((((((((((()))))))))))))))))))))))))))))))))  


import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter.font as font
from datetime import datetime
from pathlib import Path
import json
import random




# ()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()
# ||||||||||||||||||||||||||| ROOT WINDOW ||||||||||||||||||||||||||||||||
# ()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()

root = tk.Tk()
root.resizable(width=False, height=False)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = root.winfo_screenwidth()-100
window_height = root.winfo_screenheight()-100
center_x = int(screen_width/2-window_width/2)
center_y = int(screen_height/2-window_height/2)
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}'
)
root.columnconfigure(1, weight=2)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=3)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)
root.rowconfigure(4, weight=1)
root.rowconfigure(5, weight=1)
root.rowconfigure(6, weight=1)
root.rowconfigure(7, weight=1)

root.iconbitmap('polish-falcon-icon.ico')
root.title("Falcon's Nest Euchre Tournament")
root.configure(background='red4')
image = Image.open("polish_eagle_1.png")
photo_falcon = ImageTk.PhotoImage(image)

label_falcon = tk.Label(root, image=photo_falcon, border= 0)
label_falcon.grid(column=3, row=1, rowspan=7, sticky="e")

copperplate = font.Font(family='Copperplate', size= 36,
weight='bold'
)
copperplate_large = font.Font(family='Copperplate',
size= 50, weight='bold'
)
copperplate_small = font.Font(family='Copperplate',
size=16, weight='bold'
)

title_label_1 = tk.Label(root, background='red4',
foreground='white', font=copperplate_large,
text="Falcon's Nest"
)
title_label_2 = tk.Label(root, background='red4',
foreground='white',font=copperplate,
text="Euchre Tournament"
)



title_label_1.grid(column=1, row=1, sticky="s")
title_label_2.grid(column=1, row=2, sticky="n")

t_date_label = tk.Label(root, background='red4',
foreground='white',font=copperplate,
justify='left', text= 'Tournament Date',
anchor=tk.S
)
t_date_label.grid(column=1, row=3, sticky="s")


t_m = datetime.now().month
t_d = datetime.now().day
t_y = datetime.now().year
current_day = f'{t_m}/{t_d}/{t_y}'
t_date = tk.Label(root, background='red4',
foreground='white', font=copperplate, 
justify='center', text= current_day,
)
t_date.grid(column=1, row=4, sticky="n")

new_player = tk.Label(root, background='red4',
foreground='white',font=copperplate, justify='left',
text='Add New Player', anchor=tk.S
)
new_player.grid(column= 1, row=5, sticky="s")


text_string = tk.StringVar()
textbox = ttk.Entry(root,background='white',
foreground='red4',font=copperplate_small,
width=26, textvariable= text_string
)
textbox.grid(column=1, row=6, sticky="n")


add_player_button = tk.Button(root, text='Add Player',
background='red4', foreground='white',
font=copperplate_small, justify='left', 
command=lambda:button_func(text_string)
)
add_player_button.grid(column=1, row=6, sticky="s")

select_players_label = tk.Label(root, background='red4',
foreground='white', font=copperplate, justify='center',
text="Select Players"
)
select_players_label.grid(column=2, row=2, sticky="s")

path = Path('player_list.json')
contents = path.read_text()
players = json.loads(contents)
choose_players_list = tk.Variable(value=players) 

select_players = tk.Listbox(root, background= 'red4',
foreground='white', justify= 'center',
font=copperplate_small,
selectmode= tk.MULTIPLE, height=20,
listvariable=choose_players_list)

select_players.grid(column=2, row=3, rowspan=3, sticky="n")

v_scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL,
command=select_players.yview)
select_players['yscrollcommand'] = v_scrollbar.set

v_scrollbar.grid(column=2, row=3,rowspan=3, pady=10, sticky="e") 



#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#()()()()()()()()())()()()  ROOT WINDOW FUNCTIONS  ()()()()()()()()()()
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
    

def button_func(text_string):
#Download player list from JSON file, create listbox,
#Create new player entry, and add new player to listbox    
    
    players = list()
    path = Path('player_list.json')
    contents = path.read_text()
    players = json.loads(contents)
    # print(players)
    new_player = (text_string.get())
    new_player = new_player
#Check if playa name already in file and add new player   
    if new_player in players:
        print("That name is already in use.")
        name_used = tk.Toplevel(root)
        name_used.geometry('500x200+120+120')
        name_used.resizable(width=False, height=False)
        name_used.iconbitmap('polish-falcon-icon.ico')
        name_used.title('That Player already exists')
        name_used.configure(background= 'red4')
        name_used.attributes('-alpha',0.95)
        name_name = tk.Label(name_used, background='red4', foreground='white',
        font='copperplate',
        text="THAT NAME IS ALREADY IN USE")
        name_name.pack()
    elif new_player == "":
        pass
    else:
        players = players  + [new_player]
        contents = json.dumps(players)
        path.write_text(contents)
        textbox.delete(0, tk.END)
        select_players.insert(tk.END, new_player)



   
        
    
start_button = tk.Button(root, background="red4", foreground="white",
font=copperplate_small, text="Select Players", 
command=lambda:tourney())

start_button.grid(column=2, row=6, sticky="n")

# }{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{
# |||||||||||||||||||||  TOURNAMENT WINDOW  ||||||||||||||||||||||||||||
# }{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{
               

def tourney():
    tournament = tk.Toplevel(root)
    tournament.resizable(width=False, height=False)
    screen_width = tournament.winfo_screenwidth()
    screen_height = tournament.winfo_screenheight()
    window_width = tournament.winfo_screenwidth()-100
    window_height = tournament.winfo_screenheight()-100
    center_x = int(screen_width/2-window_width/2)
    center_y = int(screen_height/2-window_height/2)
    tournament.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}'
    )
    tournament.columnconfigure(0, weight=1)
    tournament.columnconfigure(1, weight=1)
    tournament.columnconfigure(2, weight=1)
    tournament.columnconfigure(3, weight=1)
    tournament.columnconfigure(4, weight=1)
    tournament.columnconfigure(5, weight=1)
    tournament.columnconfigure(6, weight=1)
    tournament.columnconfigure(7, weight=1)
    tournament.columnconfigure(8, weight=1)
    tournament.columnconfigure(9, weight=1)
    tournament.columnconfigure(10, weight=1)
    tournament.columnconfigure(11, weight=1)
    tournament.rowconfigure(0, weight=1)
    tournament.rowconfigure(1, weight=1)
    tournament.rowconfigure(2, weight=1)
    tournament.rowconfigure(3, weight=1)
    tournament.rowconfigure(4, weight=1)
    tournament.rowconfigure(5, weight=1)
    tournament.rowconfigure(6, weight=1)
    tournament.rowconfigure(7, weight=1)
    tournament.rowconfigure(8, weight=1)
    tournament.rowconfigure(9, weight=1)
    tournament.rowconfigure(10, weight=1)
    tournament.rowconfigure(11, weight=1)
    tournament.configure(background='red4',border=0)
    tournament.title("Falcon's Nest Tournament")
    tournament.iconbitmap('polish-falcon-icon.ico')
    
    leaders = tk.Frame(tournament, background='red4'
    )
    lead_teams = tk.Frame(tournament, background='red4'
    )
    scoring_grid = tk.Frame(tournament, background='red4'
    )
    
    leaders.grid(column=0, columnspan=2, row=0, rowspan=3)
    lead_teams.grid(column=3, columnspan=8, row=0, rowspan=3)
    scoring_grid.grid(column=0, columnspan=12, row=4, rowspan=9)
    
    
    
    
    import tkinter.font as font
    copperplate = font.Font(family='Copperplate', size= 36,
    weight='bold'
    )
    copperplate_large = font.Font(family='Copperplate',
    size= 50, weight='bold'
    )
    copperplate_small = font.Font(family='Copperplate',
    size=16, weight='bold'
    )   
    place_1 = tk.Label(leaders, background='red4', foreground='white',
    justify='right', font=copperplate, text="FIRST PLACE" 
    )
    place_2 = tk.Label(leaders, background='red4',
    foreground='white', justify='right', text="SECOND PLACE",
    font= copperplate 
    )
    place_3 = tk.Label(leaders, background='red4',
    foreground='white', justify='right',font= copperplate, 
    text='THIRD PLACE'
    )
    place_1.pack(side='top', anchor=tk.W)
    place_2.pack(side='top', anchor=tk.W)
    place_3.pack(side='top', anchor=tk.W)

   # <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
   # ||||||||||||||||||||  TOURNAMENT FUNCTIONS  ||||||||||||||||||||||||
   # <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><> 

    teams = []
    
    
    
    def players_select():
        selected_players = select_players.curselection()
        players_selected = [select_players.get(i) for i in selected_players]
        
        num_players = int(len(players_selected))
        if num_players % 2 != 0:
            uneven_err()
            tournament.destroy()
        else:
            random.shuffle(players_selected)
            print(players_selected)
            num_teams = len(players_selected)/2
            print(f"There are {int(num_teams)} teams for this tournament.")
            for number in range(0, int(num_teams)):
                teams.append({int(number):[players_selected.pop(0), players_selected.pop()]})
            for dic in teams:
                return teams
                    
                    
    players_select()

    print(f'these are the teams: {teams}')
    def grid_layout():
        grid_height = (len(teams))
        grid_width = (len(teams))
        for i in range(int(grid_height)):
            for j in range(int(grid_width)+2):
                b = tk.Entry(scoring_grid,background='white')
                b.grid(row=i, column=j)
                
                
    grid_layout()
    
    
    
    def labls():
        for val in teams:
    
                for key in val.keys():
                    lt = key
                    rza = key
                    print(lt)
                    for value in val.values():
                        pt = (f"{value[1]} / {value[0]}")
                        lt = tk.Label(scoring_grid,text=pt, background='red4', foreground='white', 
                        font=copperplate_small, anchor='e')
        
                        lt.grid(column=0, row=rza,)

                    

                   

        
    

        

    labls()
          
    
    
    
    
    tournament.mainloop()

# [][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]
# |||||||||||||||||||||  UNEVEN PLAYERS WINDOW  ||||||||||||||||||||||||
# [][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]


def uneven_err():
    print("Uneven number of players")
    uneven_players = tk.Toplevel(root)
    uneven_players.columnconfigure(1, weight=1)
    uneven_players.rowconfigure(1, weight=1)
    uneven_players.geometry('800x200+120+120')
    uneven_players.resizable(height=False, width=False)
    uneven_players.iconbitmap('polish-falcon-icon.ico')
    uneven_players.title('Error')
    uneven_players.configure(background='red4')
    errormess = tk.Label(uneven_players, background='red4',
    foreground='white',font=copperplate_small, justify='center',
    text="Uneven number of players, please add or remove a player")
    close_button = tk.Button(uneven_players, background='white',
    foreground='red4', command=lambda:(uneven_players.destroy()),
    font=copperplate_small, text='Close' 
    )
    
    
    errormess.grid(row=1, column=1, sticky='n')
    close_button.grid(row=1, column=1, sticky='s', rowspan=9)
    uneven_players.lift()
    uneven_players.mainloop


        

    







 
root.mainloop()