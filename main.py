import tkinter as tk
from tkinter import messagebox

# Custom Set ADT using List
class SetADT:
    def __init__(self):
        self.elements = []

    def add(self, item):
        if item not in self.elements:
            self.elements.append(item)

    def display(self):
        return self.elements

    def union(self, other):
        result = SetADT()
        for i in self.elements:
            result.add(i)
        for i in other.elements:
            result.add(i)
        return result

    def intersection(self, other):
        result = SetADT()
        for i in self.elements:
            if i in other.elements:
                result.add(i)
        return result

    def difference(self, other):
        result = SetADT()
        for i in self.elements:
            if i not in other.elements:
                result.add(i)
        return result


eventA = SetADT()
eventB = SetADT()


def get_participant_id():
    pid = entry.get()
    if pid.isdigit():
        return int(pid)
    else:
        messagebox.showerror("Error", "Enter valid numeric Participant ID")
        return None


def add_event_a():
    pid = get_participant_id()
    if pid is not None:
        eventA.add(pid)
        messagebox.showinfo("Success", "Participant added to Event A")
        entry.delete(0, tk.END)


def add_event_b():
    pid = get_participant_id()
    if pid is not None:
        eventB.add(pid)
        messagebox.showinfo("Success", "Participant added to Event B")
        entry.delete(0, tk.END)


def show_event_a():
    output.set("Event A Participants:\n" + str(eventA.display()))


def show_event_b():
    output.set("Event B Participants:\n" + str(eventB.display()))


def show_union():
    result = eventA.union(eventB)
    output.set("Total Unique Participants:\n" + str(result.display()))


def show_intersection():
    result = eventA.intersection(eventB)
    output.set("Common Participants:\n" + str(result.display()))


def show_difference():
    result = eventA.difference(eventB)
    output.set("Only in Event A:\n" + str(result.display()))


# GUI Setup
root = tk.Tk()
root.title("Event Registration & Attendance Management System")
root.geometry("500x500")

tk.Label(root, text="Participant ID", font=("Arial", 12)).pack(pady=5)
entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=5)

tk.Button(root, text="Add to Event A", command=add_event_a, width=25).pack(pady=5)
tk.Button(root, text="Add to Event B", command=add_event_b, width=25).pack(pady=5)

tk.Button(root, text="Show Event A Participants", command=show_event_a, width=25).pack(pady=5)
tk.Button(root, text="Show Event B Participants", command=show_event_b, width=25).pack(pady=5)

tk.Button(root, text="Show Total Unique Participants", command=show_union, width=25).pack(pady=5)
tk.Button(root, text="Show Common Participants", command=show_intersection, width=25).pack(pady=5)
tk.Button(root, text="Show Only Event A Participants", command=show_difference, width=25).pack(pady=5)

output = tk.StringVar()
tk.Label(root, textvariable=output, wraplength=450, font=("Arial", 11)).pack(pady=15)

root.mainloop()
