# handlers
def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Hello there! Welcome to the resume building bot. Enter your full name to begin.\
             Once you have completed all steps a word document containing your genereated resume will be sent to you.\
             Feel free to continue editing it. All the best in your job search!"
    )

def build_resume(update, context):

    questionDict = { 
    'info': { 
        1: "What is your name?",
        2: "What is your contact number?",
        3: "What is your email address?",
        4: "What is your linkedin address" },
    'education': {
        1: "What is the school's name?",
        2: "What certification did you receive from this school? (degree/diploma)",
        3: "What grade did you achieve? (gpa/uas)",
        4: "Between what date to what date did you study there? (DDMMYY - DDMMYY)",
        5: "Any brief descriptions? (scholarships, relevant coursework, projects)" }, 
    'experience': {
        1: "What is the name of the company you worked/interned at?",
        2: "What was your role?",
        3: "Between what date to what date did you work/intern there? (DDMMYY - DDMMYY)",
        4: "Any brief descriptions? (job scope, tasks, projects)" },
    'cca': {
        1: "What is the co-curricular activity you participate in?",
        2: "What was your role?",
        3: "Between what date to what date did you participate? (DDMMYY - DDMMYY)",
        4: "Any brief descriptions? (activities, contributions)" },        
    'volunteer': {
        1: "Where did you volunteer at?",
        2: "Between what date to what date did you work/intern there? (DDMMYY - DDMMYY)",
        4: "Any brief descriptions? (activities, contributions)" },
    'skillsInterest': {
        1: "What languages are you proficient in?",
        2: "What technical skills do you possess? (e.g Data Science, Software Development",
        3: "What are your hobbies and interests?" },
    }   

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="building resume!\n What is your name?"
    )

    
