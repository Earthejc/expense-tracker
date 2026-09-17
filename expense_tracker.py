# ระบบบันทึกรายรับ-รายจ่าย python
import json

try:
    with open("data.json", "r", encoding="utf-8") as f:
        transactions = json.load(f)
except FileNotFoundError:
    transactions = []

while True:
    name = input("กรอกรายการ: ")
    try:
        amount = int(input("จำนวน: "))
    except ValueError:
        print("กรุณากรอกเฉพาะตัวเลขเท่านั้น")
        continue
    total_list = {"name": name, "amount": amount}
    transactions.append(total_list)
    choice = input("ต้องการกรอกต่อไหม (y/n): ")
    if choice == "n":
        break

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(transactions, f, ensure_ascii=False)

print("บันทึกเรียบร้อย")

total = 0
for i in transactions:
    total += i["amount"]

for i in transactions:
    print(f"{i['name']} : {i['amount']}บาท")
print(f"ยอดสุทธิรวมทั้งหมด {total} บาท")
