import tkinter as tk
class MotorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Stepper Motor Control")

        self.label = tk.Label(master, text="Stepper Motor Control GUI")
        self.label.pack()

        self.button_forward = tk.Button(master, text="UP", command=self.move_forward)
        self.button_forward.pack()

        self.button_backward = tk.Button(master, text="DOWN", command=self.move_backward)
        self.button_backward.pack()

        self.button_stop = tk.Button(master, text="LEFT", command=self.stop_motor)
        self.button_stop.pack()
        self.quit_button = tk.Button(master, text="RIGHT", command=master.quit)
        self.quit_button.pack()

    def move_forward(self):
        print("Moving forward...")
    def move_backward(self):
        print("Moving backward...")
    def stop_motor(self):
        print("Motor stopped.")

if __name__ == "__main__":
    root = tk.Tk()
    gui = MotorGUI(root)
    root.mainloop()
