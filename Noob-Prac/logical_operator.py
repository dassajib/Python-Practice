#and এই অপারেটর দুটো আর্গুমেন্ট নিয়ে যাচাই করে এবং সত্য হয় যখন দুটো আর্গুমেন্টই সত্য হয়।
# উপরে উল্লেখিত and অপারেটর এর মতই or এরও দুটো আর্গুমেন্ট থাকে কিন্তু এটি সত্য হয় যদি উক্ত দুটো আর্গুমেন্টের যেকোনো একটি সত্য হয়
# অন্য দুটি অপারেটর এর মত not দুটো আর্গুমেন্ট নিয়ে কাজ করে না। বরং এর জন্য একটি আর্গুমেন্টই যথেষ্ট। এটি দিয়ে চেক করা হয় কোন লজিক না হয় কিনা।

is_musician = True
is_good = True
is_reader = False

if(is_musician and is_reader):
    print("We can be friend")
elif(is_musician or is_reader):
    print("we can talk")
elif(is_reader and is_musician and not is_good):
    print("we cant talk anymore")