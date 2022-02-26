from telegram.ext import Filters, CommandHandler, MessageHandler, Updater
from pprint import pformat
import generator
import os

with open('token.ini', 'r') as file:
    BOT_TOKEN = file.read()

resumeDict = {}

questionDict = { 
    'info': { 
        1: "PERSONAL INFO: \nWhat is your name?",
        2: "What is your contact number?",
        3: "What is your email address?",
        4: "What is your linkedin address?"},
    'education': {
        1: "EDUCATION: \nWhere are currently studying at?\n e.g. Nanyang Technological University",
        2: "What course are you in?\ne.g. Business & Computing",
        3: "What is your current GPA?\ne.g. 5.0",
        4: "What is the start and end date?\ne.g. AUGUST 2021 - MAY 2025",
        5: "Give a brief descriptions of your relevant coursework, scholarships and projects." }, 
    'experience': {
        1: "EXPERIENCE: \nWhere have you worked/interned at?\ne.g. Indeed",
        2: "What was your role there?\ne.g. Software Engineer Intern",
        3: "What is the start and end date?\ne.g. MAY 2022 - AUG 2022",
        4: "Give a brief description of your job scope and contributions." },
    'cca': {
        1: "CO-CURRICULAR ACTIVITY: \nWhat co-curricular activity (CCA) did you particpate in?\ne.g. Basketball",
        2: "What was your role in the CCA?\ne.g. Captain",
        3: "What is the start and end date?\ne.g. JAN 2022 - PRESENT",
        4: "Give a brief descriptions of the activites and your contributions." },        
    'volunteer': {
        1: "VOLUNTEERING ACTIVITY: \nWhere did you volunteer at?\ne.g. Willing Hearts",
        2: "What is the start and end date?\ne.g. JAN 2022 - PRESENT",
        3: "Give a brief descriptions of the activities and your contributions." },
    'skillsInterest': {
        1: "SKILLS & INTERESTS: \nWhat languages are you proficient in?\ne.g. English, Chinese",
        2: "What technical skills do you possess?\ne.g Data Science, Software Development\n",
        3: "What are your hobbies and interests?\ne.g. Basketball, Boxing" }
}


updater = Updater(token=BOT_TOKEN, use_context=True)

def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Hello there! Welcome to the resume building bot.\nOnce you have answered all the questions, a word document containing your generated resume will be sent to you. Feel free to continue editing it. All the best in your job search!\n \nEnter your name to begin."
    )

def build_menu(buttons,
               n_cols, 
               header_buttons=None,
               footer_buttons=None):
 menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
 if header_buttons:
  menu.insert(0, [header_buttons])
 if footer_buttons:
  menu.append([footer_buttons])
 return menu


def check_msg(update, context):
    global resumeDict
    # global timesToRepeat
    
    user_key = str(update.effective_chat.id)
    print("user_key", user_key)
    if not user_key in resumeDict:
        #instantiate userkey in resumeDict
        resumeDict[user_key] = {
            "currentQn": {0: 'info', 1: 1},
            'info':{}, 'education':{}, 'experience':{}, 'cca':{}, 'volunteer':{}, 'skillsInterest':{}
        }

    currentQnObj = resumeDict[user_key]["currentQn"]
    userText = update.to_dict()['message']['text']

    resumeDict[user_key][currentQnObj[0]][currentQnObj[1]] = userText
    print(resumeDict)
    # check msg validity 
    if(userText):
        # save input

        # get next question
        nextQnObj = go_next_qn(questionDict, currentQnObj)
        # section changed
        if(nextQnObj == False):
            # endbot
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text= "Generating your resume..."
                )

            user_data = resumeDict[str(update.effective_chat.id)]
            generator.generate_resume(user_data)

            user_name = user_data["info"][1]
            chat_id = update.message.chat_id
            document = open(f'{user_name}_Resume.docx', 'rb')
            context.bot.send_document(chat_id, document)

            if os.path.exists(f'{user_name}_Resume.docx'): os.remove(f'{user_name}_Resume.docx')

            return        
        isSectChanged = nextQnObj[0] == currentQnObj[1]

        print('next question', nextQnObj[0], nextQnObj[1])
# update user question
        resumeDict[user_key]["currentQn"] = nextQnObj
        # ask the question
        ask_question(update, context, nextQnObj)
    else:    # ask same question
        ask_question(update, context, currentQnObj)

def go_next_qn(qn, currentQn):
    global questionDict

    currentSection = currentQn[0]
    currentQuestion = currentQn[1]

    qnsSections = list(questionDict.keys())
    numOfQns = len(questionDict[currentSection])

    if(currentQuestion == numOfQns):
        # go next section
        nextSectIndex = qnsSections.index(currentSection)+1
        if(nextSectIndex >= len(qnsSections)):
            # no other sections & qns
            return False
        # question object    
        return {0: qnsSections[nextSectIndex], 1: 1}
    else:
        return {0: currentSection, 1: currentQuestion+1}


# Ask question
def ask_question(update, context, qnObj):
    global questionDict
    print("qnobj 0", qnObj[0], qnObj[1])
    
    question = questionDict[qnObj[0]][qnObj[1]]

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text= question
    )

updater.dispatcher.add_handler(
    CommandHandler('start', start)
)


updater.dispatcher.add_handler(
    MessageHandler(Filters.text, check_msg)
)

updater.start_polling()
print('Bot started!')