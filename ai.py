import requests
import json
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from datetime import datetime
import textwrap

# requests to unsplash API for random image
response = requests.get('https://source.unsplash.com/random/1080x720')
img = Image.open(BytesIO(response.content))
# img = Image.open('random.png')

# making image opacity 0.5
# img = img.convert("RGBA")
# img.putalpha(200)

img = img.point(lambda p : p * 0.5)

# getting image width and height
width, height = img.size

# saving image to destination with file format
# img.save('random.png')

# requests to quotable API for random quote
response = requests.get('https://api.quotable.io/random')

# converting response text into json data
data = json.loads(response.text)

draw = ImageDraw.Draw(img)

# setting the fonts from font family in fonts folder
font = ImageFont.truetype('fonts/Roboto-MediumItalic.ttf', size=30)

# setting width and height for quote line
(x, y) = (30, height/2)

# extracting quote and author from json data object
quote = data['content']
author = data['author']
author = "> "+author

# setting text color white
color = 'rgb(255, 255, 255)'

# setting width and height for author line
(p, q) = (30, height/1.1)

# if quote is multiline then adjusting and making fittable in image
new_quote = ""
quotes = textwrap.wrap(quote, width=75)
for i in range(len(quotes)):
	new_quote += quotes[i]+"\n"

# multiline quote will be printed on image
draw.multiline_text((x, y), new_quote, fill=color, font=font, spacing=2, align="left")

# sigleline author name printed on image
draw.text((p, q), author, fill=color, font=font)

font_tip = ImageFont.truetype('fonts/Roboto-Italic.ttf', size=20)

# singleline tip name printed on image
draw.text((width-150, height-50), "@source.9", fill=color, font=font_tip)

# getting current time for setting up image name
date_time = datetime.now()
img.save('images/'+str(date_time)+'.png')
