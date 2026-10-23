import sqlite3

def get_customer_spend():
    conn = sqlite3.connect('parts_avatar.db')
    cursor = conn.cursor()
    
    # Task: Join Customers, Orders, and Order_Items to calculate 
    # total spend (price * quantity) per Customer Name.
    query = """
    SELECT Name, SUM(OI.price*OI.quantity) Total_Spend FROM (
    SELECT Name, order_id
    FROM Customers as C
    JOIN
    Orders as O
    ON C.customer_id == O.customer_id
    ) as D
    JOIN
    Order_Items as OI
    ON OI.order_id = D.order_id
    GROUP BY Name
    """
    
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results
print(get_customer_spend())