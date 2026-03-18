import customtkinter as ctk

# --- Logic Section ---
def get_settlement(total, participants):
    if not participants: return ["Add participants first!"]
    share = total / len(participants)
    balances = {name: paid - share for name, paid in participants.items()}
    givers = [[n, a] for n, a in balances.items() if a < 0]
    receivers = [[n, a] for n, a in balances.items() if a > 0]
    
    plan = []
    while givers and receivers:
        g, r = givers[0], receivers[0]
        amt = min(abs(g[1]), r[1])
        plan.append(f"💸 {g[0]} pays {r[0]}: {amt:.2f} AED")
        g[1] += amt
        r[1] -= amt
        if abs(g[1]) < 0.01: givers.pop(0)
        if abs(r[1]) < 0.01: receivers.pop(0)
    return plan if plan else ["Everything is balanced!"]

# --- UI Section ---
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Smart Splitter")
        self.geometry("400x700") # Made taller to fit the list
        ctk.set_appearance_mode("light")
        
        self.participants = {}

        # UI Elements
        self.label = ctk.CTkLabel(self, text=" Smart Splitter: ", font=("Arial", 24, "bold"))
        self.label.pack(pady=20)

        self.total_entry = ctk.CTkEntry(self, placeholder_text="Total Bill Amount (AED)")
        self.total_entry.pack(pady=10)

        self.name_entry = ctk.CTkEntry(self, placeholder_text="Name")
        self.name_entry.pack(pady=5)
        
        self.amt_entry = ctk.CTkEntry(self, placeholder_text="Amount Paid")
        self.amt_entry.pack(pady=5)

        self.add_btn = ctk.CTkButton(self, text="Add Person", command=self.add_person, fg_color="#d36e2a")
        self.add_btn.pack(pady=10)

        # --- NEW: Participants List Section ---
        self.list_label = ctk.CTkLabel(self, text="Participants List:", font=("Arial", 12, "bold"))
        self.list_label.pack(anchor="center", padx=50, pady=(10, 0))
        
        self.scrollable_list = ctk.CTkScrollableFrame(self, width=300, height=120, fg_color="#ffffff")
        self.scrollable_list.pack(pady=5)
        

        self.calc_btn = ctk.CTkButton(self, text="Calculate Settlement", command=self.calculate, fg_color="#d36e2a")
        self.calc_btn.pack(pady=10)

        self.result_box = ctk.CTkTextbox(self, width=300, height=150,corner_radius=15,border_width=2, border_color="#000000")
        self.result_box.pack(pady=20)

    def add_person(self):
        name = self.name_entry.get()
        try:
            amt = float(self.amt_entry.get())
            self.participants[name] = amt
            person_info = ctk.CTkLabel(self.scrollable_list, text=f"• {name}: {amt} AED")
            person_info.pack(anchor="w", padx=10)
            
            self.name_entry.delete(0, 'end')
            self.amt_entry.delete(0, 'end')
            print(f"Added {name}")
        except ValueError:
            print("Invalid Amount")

    def calculate(self):
        try:
            total = float(self.total_entry.get())
            results = get_settlement(total, self.participants)
            self.result_box.delete("0.0", "end")
            self.result_box.insert("0.0", "\n".join(results))
        except ValueError:
            self.result_box.insert("0.0", "Error: Enter a total amount!")

if __name__ == "__main__":
    app = App()
    app.mainloop()