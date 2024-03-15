from getPrices import firstPrices, secondPrices
f =  [] # без воздействия
s = [] #после воздействия

for key, value in firstPrices.items():
    f.append(value)

for key, value in secondPrices.items():
    s.append(value)




f.sort(reverse=True)
s.sort(reverse=True)

b = []
a = []

for i in range(len(f)):
    b.append((f[i], i + 1, "b"))

for i in range(len(s)):
    a.append((s[i], i + 1, "a"))

i, j = 0, 0

gal_arr = []

while i < len(a) and j < len(b):
    if a[i][0] >= b[j][0]:
        gal_arr.append(a[i])
        i += 1
    else:
        gal_arr.append(b[j])
        j += 1

while i < len(a):
    gal_arr.append(a[i])
    i += 1

while j < len(b):
    gal_arr.append(b[j])
    j += 1

ind_b = set()
ind_a = set()

for i in range(len(gal_arr)):
    if gal_arr[i][2] == "b":
        if gal_arr[i][1] in ind_a:
            continue
        else:
            ind_b.add(gal_arr[i][1])
    else:
        if gal_arr[i][1] in ind_b:
            continue
        else:
            ind_a.add(gal_arr[i][1])
# дописать формулу вероятности
print(len(ind_a))

numerator = len(s) - len(ind_a) + 1
denumerator =  len(s) + 1

print(
    f"Вероятность того, что бесполезное воздействие будет казатьсся не менее эффективным, чем воздействие, эффективное по Гальтону: {numerator} / {denumerator}")
