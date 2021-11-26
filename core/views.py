from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import requests
# Create your views here.


@csrf_exempt
def index(request):
    context = {
        'status': 'ok'
    }

    if request.method == "POST":
        output = ""
        bold_chars = "𝗔𝗕𝗖𝗗𝗘𝗙𝗚𝗛𝗜𝗝𝗞𝗟𝗠𝗡𝗢𝗣𝗤𝗥𝗦𝗧𝗨𝗩𝗪𝗫𝗬𝗭𝗮𝗯𝗰𝗱𝗲𝗳𝗴𝗵𝗶𝗷𝗸𝗹𝗺𝗻𝗼𝗽𝗾𝗿𝘀𝘁𝘂𝘃𝘄𝘅𝘆𝘇𝟬𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵"
        for character in request.POST['title']:
            if character in bold_chars:
                output += bold_chars[bold_chars.index(character)]
            else:
                output += character
        data = {
            "title": output,
            "body": request.POST['body']
        }
        response = requests.post('https://merapim.azure-api.net/', json=data)
        context['status'] = response.status_code
        return render(request, template_name='index.html', context=context)
    return render(request, template_name='index.html', context=context)
