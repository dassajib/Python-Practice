# এর আগে আমরা লিস্ট সম্পর্কে জেনেছি যেটা এমন এক ধরণের ডাটা স্ট্রাকচার যার মধ্যে এলিমেন্ট গুলো ক্রমিক ইনডেক্স অনুযায়ী সাজানো থাকে। ডিকশনারি আরেক ধরণের ডাটা স্ট্রাকচার যার মধ্যেও লিস্টের মত বিভিন্ন রকম এলিমেন্ট বা অবজেক্ট স্টোর করা যায় - কিন্তু, এ ক্ষেত্রে ওই এলিমেন্ট গুলোকে ম্যানুয়ালি ইনডেক্স করতে হয়। অন্যভাবে বলতে গেলে, আমাদের নিজেদেরকেই প্রত্যেকটা এলিমেন্টের বা value এর জন্য একটি key বা ইনডেক্স নির্ধারণ করে দিতে হয়। অতঃপর একটি key-value জোড় ওয়ালা এলিমেন্টের কালেকশন তৈরি হয়।
# দুটি কার্লী ব্র্যাকেট {} এর মধ্যে কোলন চিহ্ন দিয়ে key-value জোড় তৈরি করে এবং প্রত্যেক জোড় কে কমা , দিয়ে আলাদা করে একটি ডিকশনারি তৈরি করা যায়
month_conversion = {
    "Jan" : "January",
    "Feb" : "Februrary",
    "Mar" : "March",
    "Apr" : "April",
    "May" : "May",
    "June" : "June",
    "Jul" : "July",
    "Aug" : " August",
    "Sep" : "September",
    "Oct" : "October",
    "Nov" : "November",
    "Dec" : "December",
}

print(month_conversion["Jan"])
print(month_conversion["Mar"])
print(month_conversion["Dec"])


# ডিকশনারির মধ্যে যেকোনো টাইপের অবজেক্ট বা এলিমেন্টকেই স্টোর করা যায় শুধু মাত্র এর key গুলো হতে হবে Immutable (অপরিবর্তনীয়) টাইপের যেমন নিচের মত করে একটি ডিকশনারি তৈরি করা যেতে পারে
my_marks = {"Bengali" : [30, 35, 32], "English" : [45, 52, 33], "Math": [60, 74, 58]}
print(my_marks["Math"])