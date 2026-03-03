f = open("hello.txt")
lines = f.read()
print(lines)
f.close()

f = open("hello.txt", "a")
f.write(" Rohit")
f.close()

lines = f.read()
print(lines)

with open("hello.txt", "a") as f:
    f.write("\nHello Christa")

lines = f.read()
print(lines)
