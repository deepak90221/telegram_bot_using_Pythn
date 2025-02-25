from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

TOKEN = "Your_HTTP_API_Pass_code"

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Hello! Welcome to the bot. Use /help to see available commands.")

async def help_command(update: Update, context: CallbackContext):
    await update.message.reply_text("""Available Commands:
    /youtube - Get YouTube URL
    /linkedin - Get LinkedIn profile URL
    /gmail - Get Gmail URL
    /geeks - Get GeeksforGeeks URL
    /dsa - Get a structured DSA learning path
    /python - Get a structured Python learning path
    /coding - Get coding platforms for DSA practice
    /resources - Get extra resources to master DSA with Python""")

async def gmail_url(update: Update, context: CallbackContext):
    await update.message.reply_text("Gmail Link => https://mail.google.com/")

async def youtube_url(update: Update, context: CallbackContext):
    await update.message.reply_text("YouTube Link => https://www.youtube.com/")

async def linkedin_url(update: Update, context: CallbackContext):
    await update.message.reply_text("LinkedIn URL => https://www.linkedin.com/")

async def geeks_url(update: Update, context: CallbackContext):
    await update.message.reply_text("GeeksforGeeks URL => https://www.geeksforgeeks.org/")

async def dsa_learning_path(update: Update, context: CallbackContext):
    await update.message.reply_text("""DSA Learning Path:
1️⃣ Basics of DSA: https://takeuforward.org/data-structure/striver-a2z-dsa-course/
2️⃣ Arrays & Strings: https://takeuforward.org/arrays/
3️⃣ Recursion & Backtracking: https://takeuforward.org/backtracking/
4️⃣ Linked Lists & Stacks: https://takeuforward.org/linked-list/
5️⃣ Trees & Graphs: https://takeuforward.org/graph/
6️⃣ Dynamic Programming: https://takeuforward.org/dynamic-programming/
7️⃣ Interview Problems: https://takeuforward.org/interview-experience/
📌 Full Course: http://takeuforward.org/data-structure""")

async def python_learning_path(update: Update, context: CallbackContext):
    await update.message.reply_text("""Python Learning Path:
1️⃣ Python Basics: https://www.w3schools.com/python/
2️⃣ Object-Oriented Programming: https://realpython.com/python3-object-oriented-programming/
3️⃣ Data Structures in Python: https://www.geeksforgeeks.org/python-data-structures/
4️⃣ Algorithms & Complexity: https://www.programiz.com/dsa
5️⃣ Machine Learning with Python: https://www.kaggle.com/learn/python
📌 Complete Python Roadmap: https://realpython.com""")

async def coding_platforms(update: Update, context: CallbackContext):
    await update.message.reply_text("""Best Coding Platforms for DSA:
1️⃣ **LeetCode** (Competitive coding & Interviews) - https://leetcode.com/
2️⃣ **CodeChef** (Competitive Programming) - https://www.codechef.com/
3️⃣ **Coding Ninjas** (DSA in Python, Java, C++) - https://www.codingninjas.com/
4️⃣ **GeeksforGeeks Coding** (Practice with solutions) - https://practice.geeksforgeeks.org/
5️⃣ **HackerRank** (Coding Challenges) - https://www.hackerrank.com/domains/tutorials/10-days-of-python
6️⃣ **TopCoder** (Advanced Competitive Coding) - https://www.topcoder.com/
📌 **First Preference for Python**: Start with LeetCode and Coding Ninjas for structured Python-based DSA learning.""")

async def dsa_resources(update: Update, context: CallbackContext):
    await update.message.reply_text("""📚 Extra Resources to Master DSA with Python:

📝 **Books**:
1️⃣ **Data Structures and Algorithms in Python** - https://www.amazon.com/dp/1118290275
2️⃣ **Grokking Algorithms (Python-based)** - https://www.amazon.com/dp/1617292230
3️⃣ **Problem-Solving with Algorithms and Data Structures Using Python** - https://runestone.academy/runestone/books/published/pythonds/index.html

🎥 **YouTube Playlists**:
1️⃣ **Striver's DSA Course** (Highly Recommended) - https://www.youtube.com/playlist?list=PLgUwDviBIf0rQ6cnlaHRMuOp4HjCrA8ds
2️⃣ **Python DSA by Abdul Bari** - https://www.youtube.com/playlist?list=PLlPZYPUh5asWgpFukQYRsj7MgeGjIIjZv
3️⃣ **Neetcode's Python DSA Course** - https://www.youtube.com/playlist?list=PL7g1jYj15RUO7X3I9OZ5x5fd0x6PPhQ9p

🖥️ **Online Courses**:
1️⃣ **CS50’s Introduction to Algorithms with Python (Harvard)** - https://cs50.harvard.edu/ai/
2️⃣ **Udemy: Python for Data Structures and Algorithms** - https://www.udemy.com/course/python-for-data-structures-algorithms-and-interviews/
3️⃣ **MIT OpenCourseWare - Introduction to Algorithms** - https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/

📄 **Cheat Sheets**:
1️⃣ **Python DSA Cheat Sheet** - https://cheatography.com/davechild/cheat-sheets/python-data-structures/
2️⃣ **Big-O Complexity Guide** - https://www.bigocheatsheet.com/
3️⃣ **LeetCode Patterns Guide** - https://seanprashad.com/leetcode-patterns/

🚀 **Practice Strategy**:
✅ Start with **Python DSA Basics** (GeeksforGeeks, RealPython, W3Schools)
✅ Move to **LeetCode Easy → Medium** problems
✅ Use **Striver’s A2Z DSA Sheet** (https://takeuforward.org/)
✅ Solve **100 LeetCode Problems**
✅ Learn **Graph & DP Concepts**
✅ Participate in **CodeChef, CodeForces Contests**
✅ Revise **Common Interview Patterns** (Sliding Window, Two Pointers, etc.)

📌 **Python is powerful for DSA!** Master it with these resources and keep practicing! 💻🔥""")

async def unknown(update: Update, context: CallbackContext):
    await update.message.reply_text(f"Sorry, '{update.message.text}' is not a valid command.")

async def unknown_text(update: Update, context: CallbackContext):
    await update.message.reply_text(f"Sorry, I can't recognize what you said: '{update.message.text}'")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("youtube", youtube_url))
app.add_handler(CommandHandler("linkedin", linkedin_url))
app.add_handler(CommandHandler("gmail", gmail_url))
app.add_handler(CommandHandler("geeks", geeks_url))
app.add_handler(CommandHandler("dsa", dsa_learning_path))
app.add_handler(CommandHandler("python", python_learning_path))
app.add_handler(CommandHandler("coding", coding_platforms))
app.add_handler(CommandHandler("resources", dsa_resources))

app.add_handler(MessageHandler(filters.COMMAND, unknown))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, unknown_text))

print("Bot is running...")
app.run_polling()
