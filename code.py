from tkinter import *
from tkinter import messagebox

# List of boycott brands
boycott_brands = ["Visa", "Caterpillar", "Hyundai Heavy Industries", "Alstom", "GE (General Electric)", "Bosch", 
    "Sanofi", "GlaxoSmithKline (GSK)", "Novartis", "Abbott", "Eli Lilly", "Comcast", "Fox News", 
    "Sony", "Warner Music Group", "Universal Music Group", "Ryanair", "Hilton Hotels", "Marriott", 
    "Avis", "Hardees", "Apple", "Microsoft", "Google", "Amazon", "Facebook", "McDonald's", "KFC", 
    "Tesla", "Samsung", "Intel", "IBM", "Cisco", "Oracle", "Adobe", "Salesforce", "Netflix", 
    "PayPal", "Unilever", "Procter & Gamble", "Johnson & Johnson", "Pfizer", "Merck", "PepsiCo", 
    "Coca-Cola", "Nestle", "Danone", "Kellogg's", "Boeing", "Lockheed Martin", "Airbus", "Siemens", 
    "Hitachi", "Panasonic", "Sharp", "LG Electronics", "Xiaomi", "Huawei", "Tencent", "Alibaba", 
    "eBay", "Walmart", "Target", "Costco", "FedEx", "UPS", "DHL", "Volkswagen", "Toyota", "Ford", 
    "BMW", "Mercedes-Benz", "Nissan", "Audi", "Ferrari", "Lamborghini", "Porsche", "Rolls-Royce", 
    "Hyatt", "InterContinental Hotels", "Delta Airlines", "American Airlines", "Southwest Airlines", 
    "Qantas", "Etihad Airways", "Emirates"]

# Convert all brands to lowercase for case-insensitive comparison
boycott_brands = [brand.lower() for brand in boycott_brands]

# Function to check if the brand is boycotted
def check_brand():
    brand_name = entry.get().strip().lower()  # Convert user input to lowercase
    if brand_name in boycott_brands:
        messagebox.showinfo("Result", f"The brand '{brand_name}' is boycotted.")
    else:
        messagebox.showinfo("Result", f"The brand '{brand_name}' is not boycotted.")

# Create the main window
window = Tk()
window.title("Brand Boycott Checker")
window.geometry("500x200")  # Adjusted width for longer brand names

# Label
label = Label(window, text="Enter a brand name:", font=("Arial", 12))
label.pack(pady=10)

# Entry field
entry = Entry(window, width=40, font=("Arial", 12))  # Increased width for clarity
entry.pack(pady=5)

# Button to check the brand
button = Button(window, text="Check", command=check_brand, font=("Arial", 12), bg="lightblue")
button.pack(pady=10)

# Run the application
window.mainloop()