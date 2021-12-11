# যেকোনো মেশিন বা যন্ত্র যখন বানানো হয় তখন তার কাজের জন্য যেমন কিছু যন্ত্রপাতির সেটআপ দরকার হয় তেমনি সেই মেশিনে ইনপুট হিসেবে কিছু কাঁচামাল দিতে হয় যেগুলো প্রক্রিয়াজাত করে মেশিন আমাদের চাহিদা মোতাবেক জিনিষ তৈরি করে দেয় বা এর থেকে আউটপুট পাওয়া যায়।
# ধরে নিচ্ছি আমাদের বানানো মেশিনটির এক পাশ দিয়ে ময়দা, চিনি, দুধ, ক্রিম এসব দিলে আরেক পাশ দিয়ে সুন্দর কেক তৈরি হয়ে বের হয়। তাহলে সেই ময়দা, চিনি, দুধ, ক্রিম এসব হচ্ছে সেই মেশিনের আর্গুমেন্ট আর কেক বানানোর জন্য মেশিনের মধ্যে বিভিন্ন যন্ত্রের যে সেটআপ আছে সেটাকে বলা যেতে পারে ফাংশন বডি। আর শেষে যে সুস্বাদু কেক পাওয়া যায় তাকে বলা যেতে পারে ফাংশনের রিটার্ন ভ্যালু। এখন এরকম একটি মেশিন তৈরি হয়ে গেলে এই মেশিনকে যতবার ইচ্ছা ব্যবহার করা যাবে এবং এর থেকে কেক পাওয়া যাবে। কিন্তু অবশ্যই প্রতিবার সঠিকভাবে কেক পেতে হলে এই মেশিনের আর্গুমেন্ট তথা কাঁচামাল গুলো দিতে হবে

# আর্গুমেন্টকে ফাংশনের দুটি প্রথম বন্ধনীর মধ্যে ডিফাইন করতে হয়
def squre_count(number):
    print (number * number)


squre_count(3)
squre_count(100)

# উপরে squre_count ফাংশনের আর্গুমেন্ট একটি। আর তাই যখনই আমরা এই ফাংশনকে কল করেছি বা ব্যবহার করতে চেয়েছি তখনি সেই ফাংশনের আর্গুমেন্ট (মেশিনের ক্ষেত্রে ইনপুট) পাঠিয়ে দিয়েছি এভাবে squre_count। একবার কল করার সময় ইনপুট দিয়েছি 3 আবার আরেকবার কল করার সময় ইনপুট দিয়েছি 100 এবং আমাদের ফাংশনের কাজ হচ্ছে এর কাছে আসা যেকোনো আর্গুমেন্টকে দ্বিগুণ করে স্ক্রিনে প্রিন্ট করে। তাই দুইবারই আমাদের ফাংশন কাজটি সঠিক ভাবে করেছে

# একটি ফাংশন কিন্তু একাধিক আর্গুমেন্ট নিয়ে কাজ করতে পারে অর্থাৎ এর একাধিক আর্গুমেন্ট থাকতে পারে। এটাই তো যৌক্তিক, তাই না? কারণ, একটি ফাংশন তথা মেশিনকে জটিল জটিল জিনিষ বানাতে বা আউটপুট দিতে তাকে অনেক গুলো ইনপুট নিয়ে কাজ করতে হতেই পারে

def multiply(x,y):
    z = x * y
    print(z)


multiply(9,3)

# মনে করুন, আপনি sum ফাংশনটিতে অনেকগুলো প্যারামিটার পাঠাতে চাচ্ছেন যেমন, 10, 20, 30 ... ইত্যাদি। যদি আপনি sum (a, b) হিসেবে ডিক্লেয়ার করেন তাহলে দুইটার বেশি প্যারামিটার পাঠাতে পারবেন না। সেক্ষেত্রে কোড হবে এইরকম

def sum(*args):
    sum = 0
    for num in args:
        sum += num
    return sum


print(sum(1,2,3,4,5,6,7))

# পাইথনে * এর অর্থ 
# * এর আর্গুমেন্টে ভ্যালু Tuple হিসেবে প্যাকড থাকে। এর মানে * দিয়ে প্যারামিটার ডিক্লেয়ার করলে আমরা যেকোন সংখ্যক পজিশনাল আর্গুমেন্ট পাস করতে পারি। যেমন করলাম make_sum এর ক্ষেত্রে। শুরুতে make_sum মাত্র দুইটা আর্গুমেন্ট নিলেও পরবর্তীতে আমরা প্যারামিটারে * বসিয়ে দিলাম তখন সে অনেকগুলো আর্গুমেন্ট পাস করতে পারছে

# পাইথনে ** এর অর্থ 
# আমরা চাইলে ফাংশনের প্যারামিটারে ডাবল অ্যাস্টেরিস্কস বসিয়েও ডিক্লেয়ার করতে পারি। ডাবল স্টারের মানে হল যেকোন সংখ্যক named parameter থাকতে পারে। এই মানগুলো ডিকশনারি হিসেবে প্যাকড থাকে
def print_dict(**kwargs):
    print(kwargs)


print_dict(a=1, b=2, c=3)