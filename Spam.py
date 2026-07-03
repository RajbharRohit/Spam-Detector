# Linear Search - Spam Detector

bl = ["spam", "fake", "offer", "ads", "b3"]

s = "offer"

f= False

for i in bl:
    if i== s:
        f= True
        break

if f:
    print("Spam Found")
else:
    print("Safe!")
