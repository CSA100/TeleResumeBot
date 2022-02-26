# TeleResumeBot

## The Issue

Crafting resumes is a common problem in Singapore for University students as it is new to them


## Why we want to tackle this issue 
We were all there at one point, starting our job search, clueless and helpless. How do I even create a resume? As a team of freshmen, we are haunted by this question as the summer break approaches. We thought to ourselves, "How can we aid beginner jobseekers like us in their job seeking process?" We believed that a telegram chatbot based resume generator will aid in that process. It has user interface that we are all so familiar with and it provides practical help to users in crafting their resumes.

## Solution
ByteResumes is a chatbot. It is programmed to engage in a conversation with the user, asking for relevant information about the user that is needed to craft a resume. Once all the questions have been asked and read in. The data is converted and generated into a resume template that will be sent back to the user through the chatbot. With that, the user has a better starting point in crafting their resumes and can simply edit the word document to achieve their ideal resumes!

## How we built it
We broke the problem down into 2 parts: building the chatbot, and generation of the resume template.

1. For the building of chatbots, we started from scratch. We started by understanding the basic telegram bot functions. As we learned more about how telegram API works, we scaled up and created more complicated functions that will ask questions and take in user input, then store it systematically in a dictionary for later use.

2. For the generation of the resume template, we utilised the user data collected from our chatbot in the dictionary and passed it to our resume generation function. The function extracts the data from the dictionary and uses the python-docx module to create a formatted resume, which is then sent back to the user as a word file.

## Challenges we ran into
We are all new to how telegram chatbot works, however we found the resources provided by the Indeed Telegram bot workshop incredibly beneficial, as it helped us get off the ground fast.

Initially, we wanted to build a chatbot that is able to make use of Natural language processing to analyse the conversation with the user, rather than forcing a resume structure on them. And also wanted the chatbot to have a more flexible flow that allows the users to customise their resumes. To meet the time constraints, we had to manage the scope and complexity of our project.

## Accomplishments that we're proud of
We are proud to have a produced a minimum viable product (MVP), which shows the potential benefits this project can bring with further development. We also worked well as a team as we delegated responsibilities to each person’s strengths.

## What we learned
We learnt how to work under time contraints to produce functional code, despite working with unfamiliar technologies.

On the more technical side, we learnt how to create functional and practical telegram bots that can add value to users. We also learnt how to use the module python-docx to generate word documents from user data.

## What's next for ByteResumes
This product has untapped potential. With further development of this bot, we can capitalise on machine learning and artificial intelligence to further expand on the bot to improve it’s functionality and customisability, allowing users to be more flexible with their inputs, yet still be able to build a good resume. We can even make use of AI technologies

Especially here in NTU, we can even collaborate with the Career Attachment Office (CAO), to deploy this chatbot to assist students starting out their resume crafting process.
