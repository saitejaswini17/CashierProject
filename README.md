CashierProject
A simple Python console application that simulates a cashier’s workflow at a supermarket. The program allows a cashier to enter purchased products, calculates subtotals, applies membership discounts, and displays the final amount.

Features
Product Entry: Add multiple products and their quantities to a bill.
Price Calculation: Automatically calculates the subtotal for each item using preset prices.
Membership Discounts: Supports three membership levels (Gold, Silver, Bronze) with tiered discounts for bills over $25.
Summary Output: Displays the total bill, any discounts applied, and the final amount due.
How to Use
Run the Script:
Execute cashierproject.py using Python 3.

bash
python cashierproject.py
Enter Products:

Press A to add a new product.
Type the product name and quantity.
Repeat for each item.
Press Q when all items are entered.
Enter Membership:

When prompted, enter the customer’s membership level: gold, silver, bronze, or leave blank for none.
View Bill:

The script displays the subtotal for each product, any discount applied, and the final amount.
Product Price List
Product	Price ($)
biscuit	3
chicken	5
egg	1
fish	3
coke	2
bread	2
apple	3
onion	3
Discount Policy
Bill $25 or more:
Gold: 20% off
Silver: 10% off
Bronze: 5% off
Bill under $25: No discount
Example
Code
press A to add product and Q to quit : A
enter product : biscuit
enter quantity : 2
press A to add product and Q to quit : Q
enter customer membership : gold
biscuit$3x2=6
20% off for gold membership on total amount :$4.8
the discounted amount is $ 4.8
Notes
Only products listed in the price table are accepted.
Input is case-sensitive; enter product names exactly as shown.
License
This project is provided for educational purposes.

Feel free to modify the content to better fit your project’s goals!

