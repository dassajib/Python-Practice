# পাইথনে খুবই গুরুত্বপূর্ণ ডেটা টাইপ হলো স্ট্রিং । একগুচ্ছ ক্যারেক্টার বা কিছু ওয়ার্ডের সিকুয়েন্সকে সাধারণত স্ট্রিং বলা হয়ে থাকে। পাইথনে যে কোন সেনটেন্সকেই স্ট্রিং হিসেবে ব্যবহার করা যায় সিঙ্গেল(' '), ডাবল(" ") কিংবা ট্রিপল(""" """) কোটেশন এর মাধ্যমে
py = "We all love Python"
print(py)

# ইন্টিজার বা ফ্লটের মত, স্ট্রিংকেও যোগ করা যায় যাকে কনক্যাটেনেশন বলা হয়।
first_name = "Virat"
middle_name = " "
last_name = "Kholi"
full_name = first_name + middle_name + last_name
print (full_name)

# যোগের মত স্ট্রিং নিয়ে গুনও করা যায়, একে রিপিটেশন বলে। তবে এই গুন হতে হবে একটি স্ট্রিং এর সাথে একটি ইন্টিজার নাম্বারের। স্ট্রিং এবং স্ট্রিং এর মধ্যে নয় অথবা ফ্লট টাইপের ডাটার সাথে নয়।
print("Sajib" * 3)

# নন স্ট্রিং ডাটার সাথে স্ট্রিং টাইপের ডাটাকে যুক্ত করে সুন্দর স্ট্রিং আউটপুট তৈরি করতে format মেথড ব্যবহার করা হয়। এর মাধ্যমে একটি স্ট্রিং এর মধ্যে থাকা কিছু আর্গুমেন্টকে রিপ্লেস বা সাবস্টিটিউট করা যায়। format মেথডের মধ্যের প্রত্যেকটি আর্গুমেন্ট দিয়ে এর সামনে থাকা স্ট্রিং এর মধ্যের প্লেস হোল্ডার গুলোকে রিপ্লেস করা হয়। প্লেস হোল্ডার গুলো {} এর সাথে ইনডেক্স বা নাম ব্যবহার করে ডিফাইন করা হয়। একটি উদাহরণ দেখলেই বিষয়টি পরিষ্কার হয়ে যাবে
language = ("javascript : {0}, python : {1}, php : {2}, java : {3}").format(7,6,5,4)
print(language)

# lower() , upper() ব্যাবহার করে আমরা স্ট্রিং এর ক্যারেক্টার গুলা ছোট হাতের এবং বড় হাতের করতে পারি 
my_name = "Sajib Das"
upper_case = my_name.upper()
print(upper_case)
lower_case = my_name.lower()
print(lower_case)

# isupper() , islower() ব্যবহার করে আমরা বুলিয়ান এর মত আপার কেস এবং লোয়ার কেস চেক করতে পারি
is_upper_case = my_name.upper().isupper()
is_lower_case = my_name.lower().islower()
print(is_upper_case)
print(is_lower_case)

# len() ব্যাবহার করে আমরা স্ট্রিং এর লেনথ জানতে পারি
anthem = "Amar sonar Bangla, ami tomay valobashi"
print(len(anthem))

# [] ব্র্যাকেটের ভেতরে ইনডেক্স সংখ্যা বসিয়ে আমরা উক্ত ইনডেক্সর ক্যারেক্টার কি সেটা চেক করতে পারি
print(anthem[7]) 
print(anthem[8])
print(anthem[33])

# স্ট্রিং এ এর যে কোনও ক্যারেকটার index() এর পরে বসিয়ে আমরা উক্ত ইনডেক্স সংখ্যা জানতে পারি 
print(anthem.index("s"))
print(anthem.index("o"))

# replace() ব্যাবহার করে আমরা স্ট্রিং এ চেঞ্জ করতে পারি 
print(anthem.replace("Bangla", "Bangladesh"))

# find() মেথড এবং in অপারেটর । find() ইনডেক্স রিটার্ন করে এবং in অপারেটর বুলিয়ান আউটপুট দেয়। 
print(anthem.find("Bangla"))
print("Bangladesh" in anthem)