from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from forms import MyRegistrationForm
from django.shortcuts import render

#experiment - 03.07.2014 - tomc
from django.http import HttpResponse
from django.template.loader import render_to_string
from trade.models import Part


def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('safe_login.html', c)


def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpResponseRedirect('/accounts/invalid')


def loggedin(request):
    return render_to_response('loggedin.html',
                              {'full_name': request.user.username})


def invalid_login(request):
    return render_to_response('invalid_login.html')


def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')

def register_user(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register_success')
    args ={}
    args.update(csrf(request))

    args['form'] = MyRegistrationForm()

    return render_to_response('register.html', args)

def register_success(request):
    return render_to_response('register_success.html')


#some experiments

def ua_display_good1(request):

    var = 001


    return HttpResponse(render_to_string('experiments.html', {'id_number': var}))

#def search(request):
#    if 'q' in request.GET:
#        message = request.GET['q']
#    else:
#        message = 'You submitted an empty form.'
#
#
#    data_received = message
#    return HttpResponse(render_to_string('partsearch.html', {'id_number': data_received}))


def search(request):
    if 'q' in request.GET and request.GET['q']:

        q = request.GET['q']

        #proform some operations on the search entered - ie. remove spaces - change all letters to upper case
        q.upper()
        print q
        q = q.replace(" ", "")
        print q

        #run a query on the database
        part_object = Part.objects.filter(part_number__icontains=q)

        print part_object


        #To work out how many rows we need to generate for our HTML table we count "<Part:" that is found
        #in the string and output this into the variable 'table_rows'

        string_to_find = "<Part:"
        table_rows = str(part_object).count(string_to_find)


        #convert table_rows into a number variable
        table_rows = int(table_rows)


        part_list = convert_string_to_variables(str(part_object))

        print "Part List:     " + str(part_list)

        length_of_list = len(part_list)

        print length_of_list
        print "Table Rows to Generate : " + str(table_rows)

        print "List Element" + str(part_list[0]),str(part_list[1]),str(part_list[2])

        #Create a new list out of 'part_list' ordering the list so that each line represents 7? cells with the
        #part info in it. This list should be easier to sort through using the django template.

        sorted_part_list =[]
        count_row = 1
        count_cell = 0
        cursor_count = 0

        while cursor_count < length_of_list:
            while count_row < 7:
                print "Working on cell: " + str(part_list[count_cell])
                #strip cell elements of white space and unwanted characters
                sorted_part_list.append(part_list[count_cell])
                count_cell += 1
                count_row += 1
        cursor_count += 1
        print "Results of Loops :     " + str(sorted_part_list)


        return render(request, 'partsearch.html', {'search_query': 'Please submit a search term.', 'part_search_results' : 'part_list', 'table_rows' : 'table_rows', 'length_of_list' : 'length_of_list'})

        #return render(request, 'partsearch.html', {'part': Part.objects.get(part_number__icontains=q), 'search_query': q })

        #return render_to_response('article.html',
        #{'article': Article.objects.get(id=article_id)})

    else:
        return render(request, 'partsearch.html', {'search_query': 'Please submit a search term.'})




def convert_string_to_variables(string):

    string = strip_string_of_unwanted_characters(string)
    print "String Before Split:     " + string
    string_list = string.split(":")
    print "String List:     " + str(string_list)
    return string_list


def strip_string_of_unwanted_characters(string):
    string = string.replace("<Part:","")
    string = string.replace(">","")
    return string

def strip_list_of_unwanted_whitespace(string):
    #
    return string