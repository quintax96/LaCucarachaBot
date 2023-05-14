import threading
import time
from tkinter import messagebox
from tkinter import *
import win32api
import pyautogui as pg
import time
import math
import psutil
import customtkinter
import sys
import os
import webbrowser

class GUI:
    def __init__(self):

        customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
        customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

        
        # Create the main window
        self.root = customtkinter.CTk()

        window_height = 375
        window_width = 550

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))

        self.root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        self.root.resizable(False, False)

        self.root.title("LaCucarachaBot.exe")

        try:
            os.chdir(sys._MEIPASS)
            self.root.iconbitmap("assets\\bug-white.ico")
        except Exception:
            self.root.iconbitmap("C:\\Users\\danquintar\\Pictures\\bug-white.ico")
        
        def start_callback():

            if not self.is_running:
                switch_1.configure(state = "normal")
                switch_1.toggle()
                switch_1.configure(state = "disabled")
                optionmenu_1.set("LOOP TIME")

            loop_time = m.get()

            self.start_thread(loop_time)

        def stop_callback():
            
            if self.is_running:
                switch_1.configure(state = "normal")
                switch_1.toggle()
                switch_1.configure(state = "disabled")
                optionmenu_1.set("LOOP TIME")

            self.stop_thread()

        def menu_callback(choice : str):

            loop_time : int = 30

            if choice.__contains__("sec"):
                loop_time = 30
            else:
                loop_time = int(choice[0:1]) * 60

            m.set(loop_time)

        def payPalMe():
            url = "https://paypal.me/quintax96"
            webbrowser.open(url,new=1)

        frame_1 = customtkinter.CTkFrame(master=self.root)
        frame_1.pack(pady=20, padx=60, fill="both", expand=True)

        label_1 = customtkinter.CTkLabel(font = ("arial", 20), text = "Press START to keep laptop awake!\nPress STOP/close window to stop the App", master=frame_1, justify=customtkinter.CENTER)
        label_1.pack(pady=10, padx=10)

        button_1 = customtkinter.CTkButton(font = ("arial", 18), text = "START", master=frame_1, command=start_callback)
        button_1.pack(pady=10, padx=10)

        button_2 = customtkinter.CTkButton(font = ("arial", 18), text = "STOP", master=frame_1, command=stop_callback)
        button_2.pack(pady=10, padx=10)

        optionmenu_1 = customtkinter.CTkOptionMenu(frame_1, values=["30 sec", "1 min", "2 min", "3 min", "4 min"], command= menu_callback, font = ("arial", 18))
        optionmenu_1.pack(pady=10, padx=10)
        optionmenu_1.set("LOOP TIME")

        switch_1 = customtkinter.CTkSwitch(master=frame_1, text="Running", state="disabled", switch_width = 72)
        switch_1.pack(pady=10, padx=10)

        button_3 = customtkinter.CTkButton(font = ("arial", 18), text = "PAYPAL ME!", master=frame_1, command=payPalMe)
        button_3.pack(pady=10, padx=10)

        # Set the initial value of is_running to False
        self.is_running = False

        m = IntVar()
        m.set(20)

    def start_thread(self, loop_time:int):

        #print(loop_time)

        # Check if the thread is not already running
        if not self.is_running:
            # Set is_running to True
            self.is_running = True
            # Create a new thread and bind it to the run_method method
            self.t = threading.Thread(target=self.run_method , args=(loop_time,))
            # Start the thread
            self.t.start()
        else:
            # Show a popup alert when the thread is stopped
            messagebox.showinfo("App is already running", "chucaracha is working")

    def stop_thread(self):

        # Check if the thread is running
        if self.is_running:
            # Set is_running to False
            self.is_running = False
            # Wait for the thread to finish
            self.t.join()

            # Show a popup alert when the thread is stopped
            # messagebox.showinfo("Thread Stopped", "The thread has been stopped.")
        else: 
            # Show a popup alert when the thread is stopped
            messagebox.showinfo("App is not running", "cucaracha is not working")

    def run_method(self, loop_time):
        # while self.is_running:
        #     # Replace this with your code that you want to run in the thread
        #     time.sleep(5)
        #     print("Running...")

        # Disable the failsafe feature (moving the mouse to the corner of the screen to stop the program)
        pg.FAILSAFE = False
        # Set the amount of time to pause after each PyAutoGUI function call
        pg.PAUSE = 0.001
        # Get the screen resolution
        resolution = pg.size()
        # Set the radius of the circle to move the mouse in
        radius = 35
        # Set the duration of each mouse movement (in seconds)
        duration = 0.0
        # Set the number of steps (or points) on the circle
        steps = 360
        # Calculate the x and y coordinates of the center of the screen
        # mid_x = resolution[0] / 2
        # mid_y = resolution[1] / 2
        
        mid_x = pg.position().x
        mid_y = pg.position().y

        print(mid_x)
        print(mid_y)
        

        # Define a function to calculate the x and y coordinates for a given angle on the circle
        def GetXnY(angle):
            x = radius * math.sin(math.pi * 2 * angle / 360)
            y = radius * math.cos(math.pi * 2 * angle / 360)
            return (x, y)

        # Define a function to move the mouse in a circle
        def DoACircle():
            angle = 0

            # Calculate the actual x and y coordinates of mouse cursor
            mid_x = pg.position().x
            mid_y = pg.position().y

            while angle <= 360:

                # Calculate the x and y coordinates for the current angle
                x, y = GetXnY(angle)

                # Move the mouse to the calculated position
                pg.moveTo((mid_x + x), (mid_y - y), duration=duration)

                # Increment the angle for the next step
                angle = angle + (360 / steps)

            pg.moveTo((mid_x), (mid_y))

        print("starting engine.")
        count = 0
        savedpos = win32api.GetCursorPos()

        def actions(loop_time: int):
            print(pg.size())
            while self.is_running:
                #toast.show_toast("ROBOT V2 !", "Robot is active.", threaded=False, icon_path=None, duration=2)
                for proc in psutil.process_iter():
                    if(proc.name() == "LogonUI.exe"):
                        print ("Locked")
                        exit(1)
                DoACircle()
                pg.press("shift", 3)
                cond(loop_time)

        def cond(loop_time: int):
            count = 0
            while self.is_running:
                savedpos = win32api.GetCursorPos()
                time.sleep(0.5)
                curpos = win32api.GetCursorPos()
                if savedpos == curpos:
                    savedpos = curpos
                    print("Mouse is steady. Elapsed time: ", count, " seconds.")
                    count += 0.5
                    if count >= loop_time:  # if count is greater than 60 it means timeout will occur after mouse is steady for more than
                        # 240 seconds i.e. 4 minutes. (approx.)
                        print("User away for more than 4 minutes, taking control of the system.")
                        actions(loop_time)
                        break
                    else:
                        pass
                else:
                    print("Mouse is moving.")
                    count = 0

        print(loop_time)
        cond(loop_time)

    def on_closing(self):
        # Check if the thread is running
        if self.is_running:
            # Set is_running to False
            self.is_running = False
            # Wait for the thread to finish
            self.t.join()
        sys.exit(0) #kill app
            
    def run(self):
        # Start the GUI loop
        self.root.protocol("WM_DELETE_WINDOW", gui.on_closing)
        self.root.mainloop()

if __name__ == "__main__":
    # Create an instance of the GUI class
    gui = GUI()
    # Start the GUI loop
    gui.run()