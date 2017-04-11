from django.shortcuts import render, redirect
import random
import string
KEY_LEN=14

def index(request):
    if not 'random' in request.session:
        number = 1
        generation = [random.choice(string.letters+string.digits) for i in range (KEY_LEN)]
        random_word = ("".join(generation))
        request.session['random']= {"number" :number, "word" :random_word}
    print request.session['random']
    return render(request, "random_word_generator/index.html")

def random_word(request):
    if request.method == "POST":
        generation = [random.choice(string.letters+string.digits) for i in range (KEY_LEN)]
        random_word = ("".join(generation))
        number = request.session['random']['number']+1
        request.session['random']= {"number" :number, "word" :random_word}
        return redirect("/")
    else:
        return redirect("/")

def reset(request):
    if request.method == "POST":
        del request.session['random']
        return redirect('/')

# from django.shortcuts import render, redirect
# import random
#
# def index(request):
# 	# if 'attempt' isn't in session then we can assume this is the first time loading the page
# 	# so we can set both session['attempt'] and session['word']
# 	if not 'attempt' in request.session:
# 		request.session['attempt'] = 0
# 		request.session['word'] = 'Click Generate Button for a Random String'
# 	return render(request, 'random_word/index.html')
#
# def create(request):
# 	random_word = ''
# 	vowels = ['a','e','i','o','u','y']
# 	consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z']
# 	for i in range(7):
# 		cons_index = random.randint(0,len(consonants)-1)
# 		random_word += consonants[cons_index]
# 		vow_index = random.randint(0,len(vowels)-1)
# 		random_word += vowels[vow_index]
# 	request.session['attempt'] += 1
# 	request.session['word'] = random_word
# 	return redirect('/')
#
# def reset(request):
# 	del request.session['attempt']
# 	del request.session['word']
# 	return redirect('/')
