# 📱 Smartphone Class Project

## 📌 Overview
This project demonstrates **Object-Oriented Programming (OOP)** in Python using a `Smartphone` class and its subclass `GamingPhone`.  
It covers:
- Class design with attributes and methods  
- Constructors (`__init__`) for initialization  
- Inheritance and Polymorphism  
- Real-world object modeling in code  

---

## 🚀 Features

### 🔹 Smartphone Class
- **Attributes**:  
  - `brand` → Brand of the phone  
  - `model` → Model name  
  - `storage` → Storage capacity in GB  
  - `battery` → Battery percentage (0–100%)  

- **Methods**:  
  - `make_call(number)` → Simulates making a call  
  - `charge(amount)` → Charges the phone battery  
  - `__str__()` → Displays phone details in a readable format  

---

### 🔹 GamingPhone Class (inherits from Smartphone)
- **Extra Attribute**:  
  - `cooling_system` → Describes the cooling system  

- **Extra Method**:  
  - `play_game(game_name)` → Plays a game and reduces battery  

- **Polymorphism**:  
  - Overrides `make_call()` to include “Gaming Mode”  

---

## 🖥️ Example Usage

```python
# Create normal phone
phone1 = Smartphone("Samsung", "Galaxy S22", 128, 80)
print(phone1)
phone1.make_call("123-456-7890")
phone1.charge(15)

# Create gaming phone
gaming_phone = GamingPhone("Asus", "ROG Phone 6", 256, 60, "Liquid Cooling")
print(gaming_phone)
gaming_phone.make_call("987-654-3210")
gaming_phone.play_game("PUBG")
