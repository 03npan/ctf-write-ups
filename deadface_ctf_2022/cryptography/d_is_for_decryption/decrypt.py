n = 1049 * 2063
ct = [992478,1726930,1622358,1635603,1385290]
d = 1457215

for num in ct:
     pt = pow(num, d, n)
     print(str(pt))