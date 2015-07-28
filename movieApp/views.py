from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Context, loader
from django.template import RequestContext
import re

from django.db.models import Q



# Create your views here.
#rendering data from the Movie database
from movieApp.models import Movie
def index(request):
    movie_list = Movie.objects.all()
    t = loader.get_template('index.html')
    c = Context({'movie_list': movie_list,})
    return HttpResponse(t.render(c))


#implementing search functionality
def normalize_query(query_string,
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):
    ''' Splits the query string in invidual keywords, getting rid of unecessary spaces
        and grouping quoted words together.
        Example:
        
        >>> normalize_query('  some random  words "with   quotes  " and   spaces')
        ['some', 'random', 'words', 'with quotes', 'and', 'spaces']
    
    '''
    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)] 

def get_query(query_string, search_fields):
    ''' Returns a query, that is a combination of Q objects. That combination
        aims to search keywords within a model by testing the given search fields.
    
    '''
    query = None # Query to search for every search term        
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None # Query to search for a given term in each field
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query
    
def search(request):
    query_string = ''
    found_entries = None
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']
        option = request.GET['ip']
        #print "----------->>>>"
        #print option
        
        if option=='n':
            entry_query = get_query(query_string, ['name',])
        
            found_entries = Movie.objects.filter(entry_query)#.order_by('-imdb_score')
        #elif option == 'i':
          #  entry_query = get_query(query_string, ['imdb_score'])
        
            #found_entries = Movie.objects.filter(entry_query)
           # print "----------------------"
           # print query_string
            #print "-----------------------"
           # print entry_query
           # print "---------------------"
           # print found_entries
        elif option == 'p':
            entry_query = get_query(query_string, ['popularity',])
            found_entries = Movie.objects.filter(entry_query)
        elif option == 'd':
            entry_query = get_query(query_string, ['director',])
            found_entries = Movie.objects.filter(entry_query)
        else :
            entry_query = get_query(query_string, ['genre',])
            found_entries = Movie.objects.filter(entry_query)
       
        
      
        if found_entries :
            t = loader.get_template('search_results.html')
            c = Context({'movie_list': found_entries,})
            return HttpResponse(t.render(c))
        #return a html template withthe message result not found if no search result is found
        else :
            t = loader.get_template('search_not_found.html')
            c = Context()
            return HttpResponse(t.render(c))
    