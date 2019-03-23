import requests
import json
import sys

def ocr_space(filename, overlay=False, api_key='helloworld', language='eng'):
    payload = {'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               'isCreateSearchablePdf': True,
               'isSearchablePdfHideTextLayer': True,
	       'isOverlayRequired': True,
	       'detectOrientation': True,
	       'scale': True,
               'isTable': True,

               }
    with open(filename, 'rb') as f:
        r = requests.post('https://api.ocr.space/parse/image',
                          files={filename: f},
                          data=payload,
                          )
    return r.json()

program_name = sys.argv[0]
filename = sys.argv[1]
output_name = sys.argv[2]

# generate json from ocr.space api
result = ocr_space(filename, language='eng')

# download PDF from url
url = result ['SearchablePDFURL']
r = requests.get(url)
with open(output_name+".pdf", "wb") as code:
    code.write(r.content)
