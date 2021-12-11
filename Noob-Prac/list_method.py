# পাইথন লিস্টের মধ্যে বেশ কিছু মেথড আছে, যা ব্যবহার করে আমরা অনেক কাজ খুব সহজে করতে পারি 
# extend() মেথড ব্যবহার করে আমরা দুইটা লিস্ট কে একসাথে কনক্যাট করে শো করাতে পারি 

list_one = [1,3,5,7,9]
list_two = [2,4,6,8,10]

list_one.extend(list_two)
print(list_one)

# append() মেথড ব্যবহার করে আমরা লিস্টে নিউ ডেটা রাখতে পারি
list_two.append(77)
print(list_two)

# insert() মেথড ব্যবহার করে আমরা নতুন ডেটা ইন্সার্ট করতে পারি। এক্ষেত্রে আমাদের ইনডেক্স নাম্বার এবং ডেটা, এই দুটি জিনিস ইন্সার্ট করতে হয় 
third_list = [1,2,3,4,5]
third_list.insert(3,77)
print(third_list)

# remove() মেথড ব্যবহার করে আমরা উক্ত লিস্টের ডেটা ডিলিট করতে পারি।  এক্ষেত্রে মেথডের মধ্যে রিমুভ করার ডেটা ইন্সার্ট করতে হয়।
third_list.remove(77)
print(third_list)

# clear() মেথড ব্যবহার করে আমরা উক্ত লিস্ট ডেটা গুলা পুরো রিমুব করতে পারি 
third_list.clear()
print(third_list)

# লিস্টের মধ্যে কোন একটি এলিমেন্ট মোট কতবার আছে তার সংখ্যা জানতে নিচের মত করে count() মেথডের ব্যবহার করা যেতে পারে
names = ["Sajib", "Sompod", "Sajib", "Sajib"]
print(names.count("Sajib"))

# লিস্টের কোন ইনডেক্সে অবস্থা করছে সেটা চেক করার জন্য index() মেথড ব্যবহার করা হয়
letters = ['p', 'q', 'r', 's', 'p', 'u']
print(letters.index('r'))
print(letters.index('p'))

# লিস্টের ডেটাগুলো সব শর্ট আকারে রাখার জন্য sort() মেথড ব্যবহার করা হয় 
letters.sort()
print(letters)

# লিস্ট এর ডেটা গুলা উল্টোভাবে সাজাতে হলে আমাদের reverse() মেথড এর ব্যবহার করতে হয়
letters.reverse()
print(letters)

