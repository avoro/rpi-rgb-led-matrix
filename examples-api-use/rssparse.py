import os, time, random
import feedparser
import signal
from bs4 import BeautifulSoup
from PIL import Image, ImageFont, ImageDraw
import subprocess
from subprocess import Popen
import shlex

# contain text data for each stock
items=[]
# converted images for each text data
displayItems=[]
# individual stock RSS feed
feeds=["https://www.nasdaq.com/aspxcontent/NasdaqRSS.aspx?data=quotes&symbol=GS",
             "https://www.nasdaq.com/aspxcontent/NasdaqRSS.aspx?data=quotes&symbol=TSLA",
             "https://www.nasdaq.com/aspxcontent/NasdaqRSS.aspx?data=quotes&symbol=BABA",
             "https://www.nasdaq.com/aspxcontent/NasdaqRSS.aspx?data=quotes&symbol=Z",
             "https://www.nasdaq.com/aspxcontent/NasdaqRSS.aspx?data=quotes&symbol=CRON",
             "https://www.nasdaq.com/aspxcontent/NasdaqRSS.aspx?data=quotes&symbol=AAPL",
             "https://www.nasdaq.com/aspxcontent/NasdaqRSS.aspx?data=quotes&symbol=RDFN",
             "https://www.nasdaq.com/aspxcontent/NasdaqRSS.aspx?data=quotes&symbol=MA",
             "https://www.nasdaq.com/aspxcontent/NasdaqRSS.aspx?data=quotes&symbol=ABBV",
             "https://www.nasdaq.com/aspxcontent/NasdaqRSS.aspx?data=quotes&symbol=DOCU",
             "https://www.nasdaq.com/aspxcontent/NasdaqRSS.aspx?data=quotes&symbol=GOOG",
             "https://www.nasdaq.com/aspxcontent/NasdaqRSS.aspx?data=quotes&symbol=AMZN",
             "https://www.nasdaq.com/aspxcontent/NasdaqRSS.aspx?data=quotes&symbol=MSFT",
             "https://www.nasdaq.com/aspxcontent/NasdaqRSS.aspx?data=quotes&symbol=NFLX",
             "https://www.nasdaq.com/aspxcontent/NasdaqRSS.aspx?data=quotes&symbol=CRM",
             "https://www.nasdaq.com/aspxcontent/NasdaqRSS.aspx?data=quotes&symbol=INTC",
             "https://www.nasdaq.com/aspxcontent/NasdaqRSS.aspx?data=quotes&symbol=AKAM",
             "https://www.nasdaq.com/aspxcontent/NasdaqRSS.aspx?data=quotes&symbol=IBM",
             "https://www.nasdaq.com/aspxcontent/NasdaqRSS.aspx?data=quotes&symbol=INTU",
             "https://www.nasdaq.com/aspxcontent/NasdaqRSS.aspx?data=quotes&symbol=EXPE",
             "https://www.nasdaq.com/aspxcontent/NasdaqRSS.aspx?data=quotes&symbol=ADI",
             "https://www.nasdaq.com/aspxcontent/NasdaqRSS.aspx?data=quotes&symbol=AMD",
             "https://www.nasdaq.com/aspxcontent/NasdaqRSS.aspx?data=quotes&symbol=ORCL",
             "https://www.nasdaq.com/aspxcontent/NasdaqRSS.aspx?data=quotes&symbol=JD",
             "https://www.nasdaq.com/aspxcontent/NasdaqRSS.aspx?data=quotes&symbol=JPM",
             "https://www.nasdaq.com/aspxcontent/NasdaqRSS.aspx?data=quotes&symbol=PYPL",
             "https://www.nasdaq.com/aspxcontent/NasdaqRSS.aspx?data=quotes&symbol=ADBE",
             "https://www.nasdaq.com/aspxcontent/NasdaqRSS.aspx?data=quotes&symbol=WDAY",
             "https://www.nasdaq.com/aspxcontent/NasdaqRSS.aspx?data=quotes&symbol=NDAQ",
             "https://www.nasdaq.com/aspxcontent/NasdaqRSS.aspx?data=quotes&symbol=DATA",
             "https://www.nasdaq.com/aspxcontent/NasdaqRSS.aspx?data=quotes&symbol=TRVG",
             "https://www.nasdaq.com/aspxcontent/NasdaqRSS.aspx?data=quotes&symbol=V",
             "https://www.nasdaq.com/aspxcontent/NasdaqRSS.aspx?data=quotes&symbol=C",
             "https://www.nasdaq.com/aspxcontent/NasdaqRSS.aspx?data=quotes&symbol=FB",
             "https://www.nasdaq.com/aspxcontent/NasdaqRSS.aspx?data=quotes&symbol=DBX",
             "https://www.nasdaq.com/aspxcontent/NasdaqRSS.aspx?data=quotes&symbol=NVDA",
             "https://www.nasdaq.com/aspxcontent/NasdaqRSS.aspx?data=quotes&symbol=SAP",
             "https://www.nasdaq.com/aspxcontent/NasdaqRSS.aspx?data=quotes&symbol=BKNG",
             "https://www.nasdaq.com/aspxcontent/NasdaqRSS.aspx?data=quotes&symbol=GRPN",
             "https://www.nasdaq.com/aspxcontent/NasdaqRSS.aspx?data=quotes&symbol=AXP",
             "https://www.nasdaq.com/aspxcontent/NasdaqRSS.aspx?data=quotes&symbol=TLRY",
             "https://www.nasdaq.com/aspxcontent/NasdaqRSS.aspx?data=quotes&symbol=ACB",
             "https://www.nasdaq.com/aspxcontent/NasdaqRSS.aspx?data=quotes&symbol=SFTBY",
             "https://www.nasdaq.com/aspxcontent/NasdaqRSS.aspx?data=quotes&symbol=UPWK",
             "https://www.nasdaq.com/aspxcontent/NasdaqRSS.aspx?data=quotes&symbol=ALLO",
             "https://www.nasdaq.com/aspxcontent/NasdaqRSS.aspx?data=quotes&symbol=CGC",
             "https://www.nasdaq.com/aspxcontent/NasdaqRSS.aspx?data=quotes&symbol=PLAN",
             "https://www.nasdaq.com/aspxcontent/NasdaqRSS.aspx?data=quotes&symbol=SQ",
             "https://www.nasdaq.com/aspxcontent/NasdaqRSS.aspx?data=quotes&symbol=SHOP",
             "https://www.nasdaq.com/aspxcontent/NasdaqRSS.aspx?data=quotes&symbol=CELG"]

# returns a random gba color
def colorRandom():
    return (random.randint(0,255), random.randint(0,255), random.randint(0,255))

# clears all ppm images from the working directory
# append text info to the list 
def populateItems():
    # clear out everything both variables
    del items[:]
    del displayItems[:]
    # delete images from the working directory
    # get the path
    dir_path = os.getcwd()
    # get the directory
    directory = os.listdir(dir_path)
    # remove all images from the directory
    # .ppm format only
    for imgs in directory:
        if imgs.endswith(".ppm"):
            os.remove(os.path.join(dir_path, imgs))
    # populate items list with title posts
    for url in feeds:
        # parse the feed
        feed=feedparser.parse(url)
        # store all entries
        posts=feed["entries"]
        # load the table description as a BS4 object
        bs = BeautifulSoup(posts[0]["description"], "html.parser")
        # find all table data 
        tds = bs.findAll("td")
        # string that contains info on each stock
        stock_data = ""
        for td in tds:
            if(td.text.find("As") == -1 and td.text.find("View") == -1):
                data = td.text.strip()
                stock_data = stock_data + " " + data
        print(stock_data)
        # append each stock data to the list of items
        for post in posts:
            items.append(stock_data)

# gather stock data and make images using the data
def createLinks():
    try:
        # gather stock data
        populateItems()
        for idx, item in enumerate(items):
            writeImage(unicode(item), idx)
    except ValueError:
        print("Error working with stock data")
    finally:
        print("\nWill get more news later!\n\n")

# write formated images to the file system
def writeImage(url, count):
    link, headLine="", url[:]
    text = ((headLine, 255, 255, 255), (link, colorRandom()))
    font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSans.ttf", 16)
    all_text = ""
    for text_color_pair in text:
        t = text_color_pair[0]
        all_text = all_text + t
    width, ignore = font.getsize(all_text)
    im = Image.new("RGB", (width + 30, 16), "black")
    draw = ImageDraw.Draw(im)
    x = 0;
    # draw the text into the image
    for text_color_pair in text:
        t = text_color_pair[0]
        c = text_color_pair[1]
        draw.text((x, 0), t, c, font=font)
        x = x + font.getsize(t)[0]
    # set the name for the file
    filename=str(count)+".ppm"
    displayItems.append(filename)
    # save the image to the file system
    im.save(filename)    

# display all formated images on LED Displays
def showOnLEDDisplay():
    # go thorugh all images to display
    for disp in displayItems:
        # pre-build the command
        cmd_string = "sudo ./demo --led-no-hardware-pulse --led-rows 16 --led-cols 32 --led-chain 3 -D1 "
        # complete the command with image to display
        cmd = shlex.split(cmd_string + disp)
        # create a process
        output = Popen(cmd, shell = False)
        # let the image scroll for 30 sec
        time.sleep(30)
        # kill the process
        os.system("sudo pkill -f 'demo'")
        
        
# main driver
def run():
    print("Stock Data Fetched at {}\n".format(time.ctime()))
    createLinks()
    showOnLEDDisplay()

if __name__ == '__main__':
    run()
