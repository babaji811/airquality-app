from django.shortcuts import render
import requests


def home(request):
    r = requests.get('https://api.rootnet.in/covid19-in/stats/latest')
    r_json = r.json()

    if(request.method == 'GET'):
        total = r_json['data']['unofficial-summary'][0]['total']
        recovered = r_json['data']['unofficial-summary'][0]['recovered']
        deaths = r_json['data']['unofficial-summary'][0]['deaths']
        active = r_json['data']['unofficial-summary'][0]['active']
        source = r_json['data']['unofficial-summary'][0]['source']
        lastRefreshed = r_json['lastRefreshed']
        lastOriginUpdate = r_json['lastOriginUpdate']

        context = {}
        context['total'] = total
        context['recovered'] = recovered
        context['deaths'] = deaths
        context['active'] = active
        context['source'] = source
        context['lastRefreshed'] = lastRefreshed
        context['lastOriginUpdate'] = lastOriginUpdate
        return render(request, template_name='lookup/home.html', context=context)
    else:
        stateName = request.POST['stateName']
        stateName = ''.join(stateName.split()).lower()

        context = {}

        for region in r_json['data']['regional']:
            if (''.join(region['loc'].split()).lower()) == stateName.lower():
                context['confirmedCasesIndian'] = region['confirmedCasesIndian']
                context['confirmedCasesForeign'] = region['confirmedCasesForeign']
                context['discharged'] = region['discharged']
                context['deaths'] = region['deaths']
                context['loc'] = region['loc']
                context['totalConfirmed'] = region['totalConfirmed']

        return render(request, template_name='lookup/state.html', context=context)

        
        
        

def about(request):
    return render(request, template_name='lookup/about.html')
