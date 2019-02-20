a = ["bir", "iki", "üç", "dörd", "beş", "altı", "yeddi", "səkkiz", "doqquz"]

b = ["on", "iyirmi", "otuz", "qırx", "əlli", "altmış", "yetmiş", "səksən", "doxsan"]

n = int(input("ədəd daxil edin: "))
o = 0

spell = ""

while(n > 0):
        r = n % 10
        n = n // 10
        if o == 0:
                spell = a[r - 1] + spell
        else:
                spell = b[r - 1] + spell
        o += 1
print(spell)
