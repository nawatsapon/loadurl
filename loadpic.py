import requests

#https://nhentai.net/g/233550/
#https://i.nhentai.net/galleries/1083985/62.jpg

for x in range(1, 62):
    str1 = 'D:/TestData/save2/%d.jpg' % (x)
    str2 = 'https://i.nhentai.net/galleries/1083985/%d.jpg' % (x)

    print("Open ", str2 ," and write ", str1)
    f = open(str1, 'wb')
    try:
        f.write(requests.get(str2).content)
    except IOError:
        print("[Error] File does not exist: ", str2)
    except requests.exceptions.ConnectTimeout as e:
        print "Too slow Mojo!"
    except requests.exceptions.ReadTimeout as e:
        print "Waited too long between bytes."

    f.close()
print("Done!")