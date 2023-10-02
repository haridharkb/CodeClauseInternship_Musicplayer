from tkinter import filedialog # used to provides classes and factory functions for creating file/dir slection windows
from tkinter import *
import pygame 
import os 
co1 = "#ffffff" #white
co2 = "#3C1DC6" #purple
co3 = "#191414"#black
co4 = "#CFC7F8"#l purple
co5= "#1db954"
# window = Tk()
# window.title("Music player")
# window.geometry('325x255')
# window.configure(background=co1)
# window.resizable(width=False,height=False)
# #frames

# left_frame=Frame(window,width=150,height=150,background=co1)
# left_frame.grid(row=0,column=0,padx=1,pady=1)

# right_frame=Frame(window,width=250,height=150,background=co3)
# right_frame.grid(row=0,column=1,padx=0)

# down_frame=Frame(window,width=400,height=100,background=co4)
# down_frame.grid(row=1,column=0,columnspan=3,padx=0,pady=1)

root = Tk()
root.title('Music player')
root.geometry("500x300")
pygame.mixer.init() #just initlizes pygame mixer in which allows audio


#adding the menu bar
menubar = Menu(root)
root.config(menu=menubar)

songs=[]
current_song = ""
paused=False
#to make an action on buttons ,select folder
def load_music():
    global current_song
    root.directory = filedialog.askdirectory() #used to select an folder.
    #for laod the fold:iterating the file in dir
    for song in os.listdir(root.directory):
        name,ext= os.path.splitext(song) #spliting the file into the name and extension
        if ext=='.mp3':
            songs.append(song) #mp3 ext are (songs)are stored in songs
    for song in songs:#adding to songlist or listbox
        songlist.insert("end",song)
    songlist.selection_set(0)#0 refers to select the top or first song
    current_song = songs[songlist.curselection()[0]] #basically currentsong to is to selct the song which has been selected



#for the btn
def play_music():
    global current_song,paused

    if not paused:
        pygame.mixer.music.load(os.path.join(root.directory,current_song))
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.unpause()
        paused=False


def pause_music():
    global paused
    pygame.mixer.music.pause()
    paused=True


def next_music(): #we use try except bec to prevents the error that if the songs are no more in list 
    global current_song,paused
    try:
        songlist.selection_clear(0,END)
        songlist.selection_set(songs.index(current_song)+1)
        current_song = songs[songlist.curselection()[0]]
        play_music()
    except:
        pass
        

def prev_music():
    global current_song,paused
    try:
        songlist.selection_clear(0,END)
        songlist.selection_set(songs.index(current_song)-1)
        current_song = songs[songlist.curselection()[0]]
        play_music()




    except:
        pass



organise_menu = Menu(menubar,tearoff=False) #tearoff used to remove the dashed  lines
organise_menu.add_command(label='select folder',command=load_music)
menubar.add_cascade(label='Organise',menu=organise_menu)





songlist = Listbox(root,bg=co3,fg=co1,width=100,height=15)
songlist.pack()#it will add on the window  


play_btn_image = PhotoImage(file='play.png')
pause_btn_image = PhotoImage(file='pause.png')
previous_btn_image = PhotoImage(file='previous.png')
next_btn_image = PhotoImage(file='next.png')

control_frame = Frame(root)
control_frame.pack()

play_btn = Button(control_frame, image=play_btn_image,borderwidth=0,command=play_music)
pause_btn = Button(control_frame, image=pause_btn_image,borderwidth=0,command=pause_music)
previous_btn = Button(control_frame, image=previous_btn_image,borderwidth=0,command=prev_music)
next_btn = Button(control_frame, image=next_btn_image,borderwidth=0,command=next_music)


play_btn.grid(row=0,column=1,padx=7,pady=10)
pause_btn.grid(row=0,column=2,padx=7,pady=10)
previous_btn.grid(row=0,column=0,padx=7,pady=10)
next_btn.grid(row=0,column=3,padx=7,pady=10)











root.mainloop()
