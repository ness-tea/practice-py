from decodeNYTpage import decodeWebPage

def writeToFile(content):
    with open('NYT_webpages.txt','w') as open_file:
        open_file.write(content)

if __name__=="__main__":
    writeToFile(decodeWebPage())
