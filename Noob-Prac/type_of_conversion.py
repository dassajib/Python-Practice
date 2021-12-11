# ডাটাটাইপ কনভার্সন বলতে ভ্যারিয়েবল কে এক টাইপ থেকে অন্য টাইপ এ কনভার্ট করা বুঝায়। একে টাইপ কাস্টিং ও বলা হয়ে থাকে। পাইথনে টাইপ কাস্টিং এর জন্যে কিছু বিল্টইন ফাংশন বানানো আছে। আমরা চাইলে সহজেই সেগুলো ব্যবহার করতে পারি। এখন পর্যন্ত আমরা integers, floats, এবং strings ডাটাটাইপ সম্পর্কে জেনেছি। এই টাইপে কনভার্ট করার জন্য ফাংশন গুলো যথাক্রমে হচ্ছে - int(), float(), str()

birth_year = input("enter birth year: ")
# এখানে int() ব্যাবহার করা হয়েছে কারণ birth_year ভ্যারিএবল টি একটি স্ট্রিং। 
age = 2021 - int(birth_year)
print(age)

# str()
songkha = 123
string = str(songkha)
print(string)

# float()
songkha_two = "123"
float_songkha = float(songkha_two)
print(float_songkha)