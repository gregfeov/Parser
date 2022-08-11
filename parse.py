import bs4
import requests
import sys
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.148 YaBrowser/22.7.2.899 Yowser/2.5 Safari/537.36',
}
parametrs=[]
if __name__ == "__main__":
    for param in sys.argv:
        parametrs.append(param)
for i in range(len(parametrs)):
    if parametrs[i]=="-n":
        namee=input("Enter the product name:")
        urle=input("Enter url,without \'https://megabuzz.ru/shop/startovyie-naboryi/\' :")
        f=open("name.txt",mode="a")
        fcheck=open("name.txt",mode="r").read()
        if namee+" "+urle in fcheck:
            print("Already created!")
            print("I'm quitting...")
            exit()
        f.write(namee+" "+urle+"\n")
        ff=open("primer.txt",mode="a")
        ff.write(namee+"\n")
while True:
    inp = input("Name of product:")
    if inp=="quit":
        exit()
    f = open("name.txt").read()
    a = f.split("\n")
    for i in range(len(a)):
        b = a[i].split(" ")
        if inp == b[0]:
            url = "https://megabuzz.ru/shop/startovyie-naboryi/" + b[1]
            res = requests.get(url)
            print("Response code:", res.status_code)
            try:
                soup = bs4.BeautifulSoup(res.text, 'html.parser')
                print(soup.find("span", class_="woocommerce-Price-amount amount").text + " " + soup.find("p",class_="stock in-stock").text)
            except:
                print("Can't find data")
    print("Product not founded.")


