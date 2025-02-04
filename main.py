'''PomoDrip: Pomodoro Timer by the Algo Drip team
   Keep track of your tasks with 25 minute work sessions and 5 minute breaks!
'''
import tkinter as tk
import time
from tkinter import messagebox
from sys import argv

# Constants
TITLE = "PomoDrip"
FONT = "Arial"
BACKGROUND = "#2D142C"
ENTRY_FOREGROUND = "#C72C41"
ENTRY_BACKGROUND = "#510A32"
FONT_SIZE_ENTRIES = 24
FONT_SIZE_TODO = 12

# Create window
root = tk.Tk()

# Time variables
hour = tk.StringVar()
minute = tk.StringVar()
second = tk.StringVar()

# Input for each time variable
hour_entry = tk.Entry(root, font=(FONT, FONT_SIZE_ENTRIES),
                      textvariable=hour, width=5,
                      fg=ENTRY_FOREGROUND, bg=ENTRY_BACKGROUND,
                      justify="center", bd="0")
hour_entry.place(x=10, y=30)

minute_entry = tk.Entry(root, font=(FONT, FONT_SIZE_ENTRIES),
                        textvariable=minute, width=5,
                        fg=ENTRY_FOREGROUND, bg=ENTRY_BACKGROUND,
                        justify="center", bd="0")
minute_entry.place(x=100, y=30)

second_entry = tk.Entry(root, font=(FONT, FONT_SIZE_ENTRIES),
                        textvariable=second, width=5,
                        fg=ENTRY_FOREGROUND, bg=ENTRY_BACKGROUND,
                        justify="center", bd="0")
second_entry.place(x=190, y=30)

# Initialize necessary todo list variables
todo_list_frame = tk.Frame(root)
todo_list = tk.Listbox(todo_list_frame, width=25,
                       height=7, font=(FONT, FONT_SIZE_TODO),
                       bd=0, fg=ENTRY_FOREGROUND,
                       bg=ENTRY_BACKGROUND, activestyle="none")
# Create an entry box for the todo list
todo_list_entry = tk.Entry(root, font=(FONT, FONT_SIZE_TODO),
                           fg=ENTRY_FOREGROUND, bg=ENTRY_BACKGROUND,
                           bd=1, width=26)


def time_input():
    '''Get the values from the hour, minute and seconds entries.
    If the inputted values are correct, start the timer,
    notifying the user when it finishes.
    '''
    timing = 0

    try:
        timing = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())

    except TypeError:
        messagebox.showinfo("Error", "Please check your entry.")

    finally:

        if timing == 0 or timing is None:
            messagebox.showinfo("Error", "Enter a value.")

        else:
            while timing > -1:

                # Convert minutes to seconds
                mins, secs = divmod(timing, 60)
                # Resize the window
                root.geometry("300x200")
                # Convert hours to minutes
                hours = 0
                if mins > 60:
                    hours, mins = divmod(mins, 60)

                # Display 2 digits
                hour.set("{0:2d}".format(hours))
                minute.set("{0:2d}".format(mins))
                second.set("{0:2d}".format(secs))

                # Update the numbers displayed in the entrybox
                root.update()
                time.sleep(1)

                # Time's up display
                if timing == 0:
                    messagebox.showinfo("Timer", "Time's up! 🎊")
                    # Set the timer back to 00 instead of 0
                    hour.set("00")
                    minute.set("00")
                    second.set("00")
                    # Resets the window size
                    root.geometry("650x200")

                # Subtract the time
                timing -= 1


def second_entry_clear(en):
    '''Clear the second entry if it reaches zero'''
    if second_entry.get() == "00" or second_entry.get() == "0":
        second_entry.delete(0, tk.END)


def minute_entry_clear(en):
    '''Clear the minute entry if it reaches zero'''
    if minute_entry.get() == "00" or minute_entry.get() == "0":
        minute_entry.delete(0, tk.END)


def hour_entry_clear(en):
    '''Clear the hour entry if it reaches zero'''
    if hour_entry.get() == "00" or hour_entry.get() == "0":
        hour_entry.delete(0, tk.END)


def new_task():
    '''Add a new task to the todo list'''
    task = todo_list_entry.get()
    if task != "":
        todo_list.insert(tk.END, task)
    else:
        messagebox.showinfo("Error", "Please enter some task.")


def del_task():
    '''Delete a task from the todo list'''
    todo_list.delete(tk.ANCHOR)


def main():
    '''
    ===== SETUP APPLICATION ======
    '''

    # Title
    root.title(TITLE)
    # Window size
    root.geometry("650x200")
    # Window background color
    root.configure(background=BACKGROUND)
    # Disable resizing of the window
    root.resizable(width=False, height=False)

    # Parse args

    # Help
    if "--help" in argv:
        print("usage: pomodrip [--todolist]")
        print("")
        print("PomoDrip is a tkinter-based Pomodoro Timer written in Python.")
        print("")
        print("OPTIONS:")
        print("   --todolist   Enable a todo-list (EXPERIMENTAL)")
        print("")
        print("")
        print("Report bugs to https://github.com/algodrip/pomodrip/issues")
        return

    # Activate Todo list
    show_todo_list = bool("--todolist" in argv)

    # --- TIMER ---

    # Set the values of time to 0
    hour.set("00")
    minute.set("00")
    second.set("00")

    # Labels for the hours, minutes, and seconds
    # -- Unused so we are commenting it out for now
    # hour_text = tk.Label(root, font=(FONT, FONT_SIZE_TODO), fg="#EE4540")

    # Button to activate the timer
    button_entry = tk.Button(root, text="Start!", bd="0",
                             command=time_input, width=38,
                             compound="c",
                             fg=ENTRY_FOREGROUND, bg=ENTRY_BACKGROUND)
    button_entry.place(x=10, y=75)

    # Bind the entry boxes
    hour_entry.bind("<Button-1>", hour_entry_clear)
    minute_entry.bind("<Button-1>", minute_entry_clear)
    second_entry.bind("<Button-1>", second_entry_clear)

    # --- TO-DO LIST ---

    if show_todo_list:
        # Frame used to separate the todo list
        todo_list_frame.place(x=300, y=30)

        # Create the actual todo list
        todo_list.pack(side=tk.LEFT, fill=tk.BOTH)

        # task_list values
        task_list = []

        # Insert a new task
        for item in task_list:
            todo_list.insert(tk.END, item)

        # Scroll bar for todo list
        todo_list_scroll_bar = tk.Scrollbar(todo_list_frame)
        todo_list_scroll_bar.pack(side=tk.RIGHT, fill=tk.BOTH)

        # Control for the scroll bar
        todo_list.config(yscrollcommand=todo_list_scroll_bar.set)
        todo_list_scroll_bar.config(command=todo_list.yview)

        todo_list_entry.place(x=300, y=170)

        # Create a frame for the list buttons
        list_button_frame = tk.Frame(root)
        list_button_frame.place(x=550, y=30)

        # Insert text into the listbox
        addtask_button = tk.Button(list_button_frame, text="Insert",
                                   font=(FONT, FONT_SIZE_TODO), bd=0,
                                   fg=ENTRY_FOREGROUND, bg=ENTRY_BACKGROUND,
                                   width=10, command=new_task)
        addtask_button.pack(fill=tk.BOTH, expand=True, side=tk.TOP)

        # Delete items in the list
        del_task_button = tk.Button(list_button_frame, text="Remove",
                                    font=(FONT, FONT_SIZE_TODO), bd=0,
                                    fg=ENTRY_FOREGROUND, bg=ENTRY_BACKGROUND,
                                    width=10, command=del_task)
        del_task_button.pack(fill=tk.BOTH, expand=True, side=tk.BOTTOM)

    # Loop the window
    root.mainloop()


if __name__ == "__main__":
    main()
