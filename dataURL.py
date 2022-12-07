import os
class DataURL:

  dataFile = "dataURL.txt"

  def __init__(self):
    fileTest = open(self.dataFile, 'a')
    fileTest.close()

  def dataWrite(self):
    dataOpen = open(self.dataFile, 'a')
    siteURL = input("Site adresini ön eki ile birlikte giriniz: ")
    kontrolhttp = siteURL[:7]
    kontrolhttps = siteURL[:8]
    http = "http://"
    https = "https://"
    if kontrolhttp == http or kontrolhttps == https:
        dataOpen.write(siteURL + "\n")
        dataOpen.close()
        print("Url kaydedildi.")
    else:
        print("Hata!")
        print("url'nin ön ekini (/'https://' veya 'http://') giriniz.")

  def dataRead(self):
      dataOpen = open(self.dataFile, 'r')
      if os.stat(self.dataFile).st_size==0:
          print("Henüz kaydedilmiş adres yok!")
      else:
            for dataShow in dataOpen:
                print(dataShow)
      dataOpen.close()