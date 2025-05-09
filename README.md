# EyeStock: Sales and Inventory Management System

EyeStock is a simple command-line-based Sales and Inventory Management System developed as a final project requirement for our school using Python as the programming language. It simulates the core functionalities of a small optical retail business, allowing an admin to manage stocks and a customer to purchase items.

---

## 💡 Features

### 🛠 Admin Functions
- Set and manage business capital
- Purchase stocks from manufacturers
- Add and update inventory (stock quantity & resale prices)
- View all available inventory
- Remove stocks from inventory

### 🛍 Customer Functions
- Browse available products
- Add items to cart and make purchases
- View generated receipts with payment and change breakdown

---

## 📋 Usage

Run the Python script using any Python 3 environment.  
Upon launching, users can choose between:

1. **Admin** – Requires login (default: `admin` / `admin123`)
2. **Customer** – No login needed, direct shopping experience
3. **Exit** – Terminates the program

---

## 👩‍💻 How It Works

- Admin sets the initial capital.
- Stocks are purchased from a pre-defined manufacturer catalog.
- Stocks can be updated, retrieved, or removed.
- Customers can purchase from available stocks and receive receipts.
- Sales revenue is added to the business capital.

---

## 🗂 Sample Stock Items

| Product                | Default Cost | Resale Price (set by admin) |
|------------------------|--------------|------------------------------|
| Eyeglass               | $120         | Customizable                 |
| Eye Drops              | $49          | Customizable                 |
| Colored Contact Lens   | $200         | Customizable                 |
| Repair Kit             | $80          | Customizable                 |
| ...and more!           |              |                              |

---

## 🛡 Requirements

- Python 3.x
- No external libraries required

---

## ⚙️ How to Run

```bash
python eyestock.py
