#  FutureWealth Tracker

**FutureWealth Tracker** is an interactive financial forecasting tool. Instead of looking at a static spreadsheet, I built this to turn abstract savings goals into a visual reality, showing exactly how wealth can grow over a 30-year horizon.

---

###  How it's calculated
The core of this application is built on the **Compound Interest Formula**. While most people understand the concept, seeing it mapped out on a graph reveals the "Snowball Effect" of consistent investing.

The app calculates your future balance using:

$$A = P(1 + \frac{r}{n})^{nt}$$

**The variables I used:**
* **P:** Your starting capital (Principal).
* **r:** The annual interest rate (e.g., 7% or 10%).
* **n:** How many times interest is compounded per year.
* **t:** The total time in years (capped at 30 for this model).

I used **Matplotlib** to take these mathematical results and plot them on a coordinate system, allowing you to see the "elbow" of the curve where growth starts to accelerate exponentially.

---

### 💡 Why is this useful?
I built this tool to solve three specific problems:
1. **Visual Motivation:** It’s easier to stay disciplined when you can see your 10, 20, and 30-year milestones as a tangible curve.
2. **Scenario Testing:** You can instantly see the massive difference a 2% change in interest makes over three decades.
3. **Planning for the Future:** Whether it's for retirement or a major purchase, this tool gives you a clear target to aim for based on actual math.

---

### 🛠️ Technical Features
* **Dynamic Graphing:** The plot updates instantly as you adjust your inputs.
* **Modern UI:** Built with **CustomTkinter** to ensure a high-contrast, professional interface that avoids the "boring" look of traditional banking apps.
* **Logic-Driven:** Handles precise floating-point math to ensure the projections stay accurate to the cent.

---

### 🚀 How to Run
1. Ensure you have `customtkinter` and `matplotlib` installed.
2. Run the Python file:
```bash
python "FutureWealth Tracker.py"
