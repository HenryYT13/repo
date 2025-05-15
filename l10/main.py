a = ["KHM.Quân", 2013, 8.8, "Nam"]
print(a)
print(f"Số phần tử của a là: {len(a)}")
print(f"old info")
for item in a:
    print(item)
print(f"added phone number")
a.append("0123456789")
for item in a:
    print(item)