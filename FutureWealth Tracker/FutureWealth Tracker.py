import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# --- Logic Section ---
def calculate_wealth(monthly, rate, years_count):
    # Convert rate to a decimal (e.g., 8 becomes 0.08)
    decimal_rate = rate / 100
    years = list(range(1, int(years_count) + 1))
    
    values = []
    for y in years:
        # Standard compound interest formula for monthly contributions
        if decimal_rate == 0:
            total = monthly * 12 * y
        else:
            total = (monthly * 12) * ((pow(1 + decimal_rate, y) - 1) / decimal_rate)
        values.append(total)
    return years, values

# --- UI Section ---
class WealthApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("FutureWealth Tracker 🌞")
        self.geometry("950x850")
        ctk.set_appearance_mode("dark")
        
        # Color Palette
        self.orange_pop = "#FF8C00" 
        self.yellow_sun = "#FFD700"
        self.bubble_font = ("Comic Sans MS", 14)
        
        self.configure(fg_color="#0f172a") 

        # Main Centered Card
        self.main_card = ctk.CTkFrame(self, fg_color="#1e293b", corner_radius=25, 
                                      border_width=2, border_color="#000000")
        self.main_card.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.9, relheight=0.95)

        # Header
        self.header = ctk.CTkLabel(self.main_card, text="🌞 FutureWealth Tracker", 
                                   font=("Comic Sans MS", 28, "bold"), text_color=self.yellow_sun)
        self.header.pack(pady=(15, 5))

        # --- SLIDERS AREA ---
        self.input_container = ctk.CTkFrame(self.main_card, fg_color="transparent")
        self.input_container.pack(pady=10, padx=40, fill="x")

        # 1. Monthly Savings Slider
        self.savings_label = ctk.CTkLabel(self.input_container, text="Monthly Savings: 500 AED", 
                                          font=self.bubble_font, text_color=self.orange_pop)
        self.savings_label.pack()
        self.savings_slider = ctk.CTkSlider(self.input_container, from_=100, to=10000, 
                                            button_color=self.orange_pop, progress_color=self.yellow_sun,
                                            command=self.update_plot)
        self.savings_slider.set(500)
        self.savings_slider.pack(pady=(0, 15), fill="x")

        # 2. Interest Rate Slider
        self.rate_label = ctk.CTkLabel(self.input_container, text="Expected Return: 8%", 
                                       font=self.bubble_font, text_color=self.yellow_sun)
        self.rate_label.pack()
        self.rate_slider = ctk.CTkSlider(self.input_container, from_=1, to=15, 
                                         button_color=self.yellow_sun, progress_color=self.orange_pop,
                                         command=self.update_plot)
        self.rate_slider.set(8)
        self.rate_slider.pack(pady=(0, 15), fill="x")

        # 3. Time Period Slider
        self.years_label = ctk.CTkLabel(self.input_container, text="Time Period: 5 Years", 
                                        font=self.bubble_font, text_color="#FFFFFF")
        self.years_label.pack()
        self.years_slider = ctk.CTkSlider(self.input_container, from_=1, to=30, 
                                          button_color="#FFFFFF", progress_color=self.yellow_sun,
                                          command=self.update_plot)
        self.years_slider.set(5)
        self.years_slider.pack(pady=(0, 15), fill="x")

        # --- GRAPH AREA ---
        self.graph_container = ctk.CTkFrame(self.main_card, fg_color="#0f172a", 
                                            corner_radius=20, border_width=2, border_color="#000000")
        self.graph_container.pack(expand=True, fill="both", padx=30, pady=(0, 20))
        
        self.fig, self.ax = plt.subplots(figsize=(5, 4), facecolor='#0f172a')
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.graph_container)
        self.canvas.get_tk_widget().pack(fill="both", expand=True, padx=10, pady=10)

        self.update_plot()

    def update_plot(self, event=None):
        # 1. Get values from all 3 sliders
        monthly = self.savings_slider.get()
        rate = self.rate_slider.get()
        years_count = self.years_slider.get()

        # 2. Update the text labels
        self.savings_label.configure(text=f"✨ Monthly Savings: {int(monthly)} AED")
        self.rate_label.configure(text=f"📈 Expected Return: {int(rate)}%")
        self.years_label.configure(text=f"⏳ Time Period: {int(years_count)} Years")
        
        # 3. Run the math logic
        years_list, values = calculate_wealth(monthly, rate, years_count)

        # 4. Update the Graph
        self.ax.clear()
        self.ax.set_facecolor('#0f172a')
        self.ax.plot(years_list, values, color=self.yellow_sun, marker='o', 
                     markersize=8, linewidth=3, markerfacecolor=self.orange_pop)
        self.ax.fill_between(years_list, values, color=self.orange_pop, alpha=0.3)
        
        self.ax.tick_params(colors='white', labelsize=9)
        self.ax.set_title(f"{int(years_count)}-Year Growth Projection", color='white', fontname="Comic Sans MS")
        self.ax.spines['top'].set_visible(False)
        self.ax.spines['right'].set_visible(False)
        self.ax.grid(True, linestyle='--', alpha=0.1)
        
        self.canvas.draw()

if __name__ == "__main__":
    app = WealthApp()
    app.mainloop()