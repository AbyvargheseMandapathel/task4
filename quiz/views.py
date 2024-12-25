from django.shortcuts import render
import random

# Create your views here.


def generate_number():
    num1 = random.randint(0,100)
    num2 = random.randint(0,100)
    operator = random.choice(['+', '-', '*'])
    
    question = f"{num1} {operator} {num2}"
    
    answer = eval(question)
    
    return question,answer

def home(request):
    question, answer = generate_number()
    
    # Store the question and answer in the session
    request.session['answer'] = answer
    request.session['question'] = question
    
    # Initialize the score in the session if not already present
    if 'score' not in request.session:
        request.session['score'] = 0

    return render(request, 'home.html', {
        'question': question,
        'score': request.session['score'],  # Pass the current score to the template
    })
    
    
def answer(request):
    if request.method == "POST":
        user_answer = int(request.POST.get('score', 0))  # Get the user's answer
        correct_answer = request.session.get('answer')  # Retrieve the correct answer
        question = request.session.get('question')  # Retrieve the question
        
        # Initialize score from the session
        score = request.session.get('score', 0)
        
        if user_answer == correct_answer:
            message = 'Correct answer'
            score += 1  # Increment the score
            request.session['score'] = score  # Save updated score in the session
        else:
            message = 'Wrong answer'

        return render(request, 'home.html', {
            'message': message,
            'correct_answer': correct_answer,
            'question': question,
            'score': score,
        })
    
# def answer(request):
    
#     question = None
#     answer = None
#     message = ""
    
#     print(question ,answer)
    
#     if request.method == 'POST':
#         question ,answer = generate_number()
#         user_answwer = int(request.POST.get('score',0))
#         # correct_answer = int(request.POST.get('correct_answer'))
        
        
        
#         print(user_answwer)
#         print(answer)
        
#         if(user_answwer ==answer ):
#             message = 'Correct answer'
#         else:
#             message = 'Wrong answer'
            
    
    
#     return render(request, 'home.html', {
#         'question': question,
#         'answer': answer,
#        'message': message
#     })
    
    