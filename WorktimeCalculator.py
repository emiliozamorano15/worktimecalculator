import tkinter as tk
from datetime import datetime, timedelta
import sys, os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def main():

    def display_time():
        """
        Function to display current time on a label that updates its value on real time
        """
        current_time = datetime.now().strftime('%H:%M:%S')
        clock_label.config(text=current_time)
        clock_label.after(200, display_time)

    def calculate_time(event=None):
        """
        Function to calculate the number of hours worked so far as well as the earliest shift end based on following inputs
        Input
        - start_time_entry: str Time where the shift started (input from form)
        - work_time_entry: str No. of hours worked previously to the time of calculation

        Output
        - End shift: Earliest shift end time 
        - Hours worked: Total of hours worked 
        """
        current_time = datetime.now()
        current_date = datetime.now().date()

        ## Calculate the end shift time
        if start_time_entry.get():
            start_time = datetime.strptime(start_time_entry.get(), '%H:%M').time()
            
        else:
            start_time = current_time.time()
        
        ## Calculate the hours worked so far
        if work_time_entry.get():
            worked_time = float(work_time_entry.get())
        else:
            worked_time = 0

        start_datetime = datetime.combine(current_date, start_time)
        elapsed = (current_time - start_datetime) #+ timedelta(hours=worked_time)
        worked_hours = round(elapsed.total_seconds()/3600 + worked_time + 0.17,2)
        worked_time_output.config(
            text=worked_hours
            , justify='left')

        end_time = start_datetime + timedelta(hours= 8.17 - worked_time)
        end_time_output.config(
            text=end_time.strftime('%H:%M')
            , justify='left')

        start_time_entry.delete(0, 'end')
        work_time_entry.delete(0, 'end')

        start_time_entry.focus_set()

    window = tk.Tk()
    window.title('Worktime Calculator')
    window.configure(background='white')
    window.resizable(False, False)
    window.attributes('-topmost', 1)
    window_width = 435
    window_height = 350

    # get the screen dimension
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # find the center point
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)

    # set the position of the window to the center of the screen
    window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')  
    # window.iconbitmap(resource_path('assets\\clock.ico'))

  
    ## Main frame
    frame = tk.Frame(window, width = 400, background="white")
    frame.grid(row=6, column=2, padx=20, pady=10, rowspan= 5)

    ## Current time
    clock_info_label = tk.Label(frame
        , font = ('Raleway',12, 'bold')
        , text = 'Current time:'
        , background="white")
    clock_info_label.grid(row=0, column=0, padx=20, pady=10, sticky='w')

    clock_label = tk.Label(frame
        , font = ('Raleway',12, 'bold')
        , padx=20, pady=10
        , background="white")
    clock_label.grid(row=0, column=1, sticky='w')
    
    ## Shift Start
    start_info_frame = tk.LabelFrame(frame
        , text="Shift start info"
        , width = 400
        , background="white")
    start_info_frame.grid(row= 1, column=0, padx=20, pady=10, columnspan=2, sticky='w')

    start_time_label = tk.Label(start_info_frame
        , text='Start of the shift (hh:mm)'
        , background="white"
        , width = 20)
    start_time_label.grid(row=1,column=0, padx=20, pady=10, sticky='w')
    start_time_entry = tk.Entry(start_info_frame)
    start_time_entry.grid(row=1, column=1, padx=20, pady=10, sticky='w')

    work_time_label = tk.Label(start_info_frame
        , text='Hours worked (decimal)'
        , background="white"
        , width = 20)
    work_time_label.grid(row=2,column=0, padx=20, pady=10, sticky='w')
    work_time_entry = tk.Entry(start_info_frame)
    work_time_entry.grid(row=2, column=1, padx=20, pady=10, sticky='w')

    ## Shift End
    end_info_frame = tk.LabelFrame(frame
        , text="Shift end info"
        , width = 400
        , background="white")
    end_info_frame.grid(row= 3, column=0, padx=20, pady=10, columnspan=2, sticky='w')

    end_time_label = tk.Label(end_info_frame, text='End of the shift (hh:mm)'
        , justify='left'
        , background="white"
        , width = 20
        )
    end_time_label.grid(row=3,column=0, padx=20, pady=10, sticky='w')
    end_time_output = tk.Label(end_info_frame, text=''
        , justify='left'
        , background="white"
        , width = 17
        )
    end_time_output.grid(row=3, column=1, padx=20, pady=10, sticky='w')

    worked_time_label = tk.Label(end_info_frame
        , text='Total Hours'
        , justify='left'
        , background="white"
        , width = 20
        )
    worked_time_label.grid(row=4,column=0, padx=20, pady=10, sticky='w')
    worked_time_output = tk.Label(end_info_frame, text=''
        , justify='left'
        , background="white"
        , width = 17
        )
    worked_time_output.grid(row=4, column=1, padx=20, pady=10, sticky='w')

    calculate_btn = tk.Button(frame, text="Calculate", command=calculate_time)
    calculate_btn.grid(row=5, column=0, columnspan=2)
    calculate_btn.bind('<Return>',calculate_time)
 
    display_time()
    start_time_entry.focus_set()
    window.mainloop()

if __name__ == "__main__":
	main()