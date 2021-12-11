# পাইথনে ৬ ধরণের বিল্ট ইন টাইপ আছে। সেগুলো হচ্ছে - numeric, sequence, mapping, class, instance এবং exception. সব থেকে ব্যাসিক ডাটা স্ট্রাকচারটি হচ্ছে sequence. এর প্রত্যেকটি এলিমেন্টের জন্য একটি নাম্বার অ্যাসাইন করা হয় যাকে ইনডেক্স বা পজিশন বলা যায়। প্রথম ইনডেক্স শূন্য, তারপর ১ এবং এরপর ক্রমিক আকারে বাড়তে থাকে
# পাইথনে আবার ৩ ধরণের ব্যাসিক sequence টাইপ আছে যেগুলো হচ্ছে list, tuple, এবং xrange object. এই চ্যাপ্টারে আমরা আলোচনা করবো list নিয়ে
words = ["Hello", "world", "!"]
print(words[0])
print(words[1])
print(words[2])

# আমরা আগে দেখেছি লিস্ট থেকে কিভাবে ইনডেক্স দিয়ে একটি মাত্র ভ্যালু অ্যাক্সেস করা যায়। এখন দেখবো কিভাবে একটি লিস্টকে ভাগ করে আরেকটি লিস্ট তৈরি করা যায় অথবা অন্যভাবে বলতে গেলে কিভাবে একটি লিস্ট থেকে একাধিক ভ্যালু নিয়ে আরেকটি লিস্ট হিসেবে অ্যাক্সেস করা যায়। এ কাজের জন্য [] এর মধ্যে শুধুমাত্র একটি ইনডেক্স না লিখে বরং কোলন দিয়ে একাধিক ইনডেক্স লিখতে হয়
marks = [10,20,30,40,50,60,70,80,90,100]
highest_marks = marks[7:]
average_mark = marks[4:7]
poor_marks = marks[0:3]
print(average_mark)
print(highest_marks)
print(poor_marks)

# লিস্ট স্লাইসের সময় শুরু ও শেষ ইনডেক্স বাদে ধাপও উল্লেখ করে দেয়া যায়। অর্থাৎ, উল্লেখিত ইনডেক্সের মধ্যবর্তী ভ্যালু গুলো সিলেক্ট হবে কিন্তু সেখান থেকে উল্লেখিত ধাপ পরিমাণ ইনডেক্স জাম্প করে করে ভ্যালু নেয়া হবে
some_numbers = [91,92,93,94,95,96,97,98,99,100]
print(some_numbers[1:8:2])


# আমরা দেখেছি কিভাবে শুরু ও শেষ ইনডেক্স নির্ধারণ করে দিয়ে, একটি লিস্ট থেকে মধ্যবর্তী কিছু ভ্যালু নিয়ে এর স্লাইস তৈরি করা যায়। চাইলে এভাবে স্লাইস না করে - মুল লিস্টের শুরুর ইনডেক্স নির্ধারণ করে দিয়ে এবং শেষ থেকে উল্টা ইনডেক্স নির্ধারণ করে দিয়েও একটি স্লাইসড লিস্ট পাওয়া যায়
again_numbers = [12,4,45,7,35,23,24,57,87,23,678,6783,235,77]
print(again_numbers[3:-4])

all_numbers = [11,22,33,44,55,66,77]
max_number = all_numbers[0]
for number in all_numbers:
    if (number > max_number):
        max_number = number

print(max_number)