website = "https://jaccount.sjtu.edu.cn/jaccount/captcha"
import urllib
def main():
    for i in range(100,350):
        urllib.urlretrieve(website, "./images/"+str(i)+".jpg")
if __name__ == "__main__":
    main()
