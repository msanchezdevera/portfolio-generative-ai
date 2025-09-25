# Messy sales processing with nested conditions and duplication

from datetime import datetime

def run(data):
    # data: list of dicts: {"item": str, "price": str, "qty": str, "ts": "YYYY-MM-DD", "role": str, "active": bool}
    total = 0.0
    items = []
    for row in data:
        # permissions logic
        if row.get("role") == "admin":
            if row.get("active") == True:
                pass
            else:
                print("Inactive admin account.")
                continue
        else:
            print("Access denied.")
            continue

        # cleanse
        item = row["item"].strip()
        price = row["price"].strip()
        qty = row["qty"].strip()
        price = float(price)
        qty = int(qty)

        # compute
        s = price * qty
        total = total + s
        items.append({"Item": item, "Price": price, "Qty": qty, "Sale": s})

        # duplicate: parse ts for each row but we never use date object
        d = datetime.strptime(row["ts"], "%Y-%m-%d")  # redundant

    # duplicate: print summary pattern repeated
    print("TOTAL:", total)
    for it in items:
        print(it["Item"], it["Price"], it["Qty"], it["Sale"])

    # return raw structures
    return total, items
