# পাইথনে if স্টেটমেন্ট ব্যবহার করে নির্দিষ্ট একটি কন্ডিশনের উপর ভিত্তি করে কিছু স্টেটমেন্ট বা কোড ব্লককে রান করানো যায়। যদি একটি কন্ডিশন বা এক্সপ্রেশন সত্য হয় তাহলে এর আওতাভুক্ত স্টেটমেন্ট রান হয়। 
# else বস্তুত if এর সাথেই সম্পর্কিত। অর্থাৎ, যদি উল্লেখিত if কন্ডিশনটি সত্য না হয় তাহলে else এর আওতাভুক্ত কোডব্লক রান বা এক্সিকিউট হয়।

is_hot = False
is_cold = True

if is_hot:
    print("It's a hot day")
    print("Drink Water")
elif is_cold:
    print("It's a cold day")
    print("Dont get cold")
else :
    print("It's a rainy day")
    print("Dont get very wet")
