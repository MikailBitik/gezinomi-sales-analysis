import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

df = pd.read_excel('gezinomi_project/miuul_gezinomi.xlsx')
df.head()
df.info()
df.describe()

# Soru 2:Kaçunique şehirvardır? Frekanslarınedir?
df.nunique()
100*df["SaleCityName"].value_counts()/len(df)

# Soru 3:Kaç unique Concept vardır?
df["ConceptName"].nunique()

# Soru4: Hangi Concept’den kaçar tane satış gerçekleşmiş?
df["ConceptName"].value_counts()

# Soru5: Şehirlere göre satışlardan toplam ne kadar kazanılmış?
df.groupby("SaleCityName").agg({"Price": "sum"})

# Soru6: Concept türlerine göre ne kadar kazanılmış?
df.groupby("ConceptName").agg({"Price": "sum"})

# Soru7: Şehirlere göre PRICE ortalamaları nedir?
df.groupby(by="SaleCityName").agg({"Price": "mean"})

# Soru 8: Conceptlere göre PRICE ortalamaları nedir?
df.groupby("ConceptName").agg({"Price":"mean"})

# Soru 9: Şehir-Concept kırılımında PRICE ortalamalarınedir?
df.pivot_table("Price", "SaleCityName", "ConceptName", "mean")
#ÇÖZÜM VİDEOSUNDA YAPILAN:
df.groupby(by=["SaleCityName", "ConceptName"]).agg({"Price": "mean"}) #Asıl istenen bu şekildeymiş


## Görev 2: SaleCheckInDayDiff değişkenini kategorik bir değişkene çeviriniz
# SaleCheckInDayDiff değişkeni müşterinin CheckIn tarihinden ne kadar önce satin alımını tamamladığını gösterir.
# Aralıkları ikna edici şekilde oluşturunuz.
# Örneğin: ‘0_7’, ‘7_30', ‘30_90', ‘90_max’ aralıklarını kullanabilirsiniz.
# Bu aralıklar için "Last Minuters", "Potential Planners", "Planners", "Early Bookers“ isimlerini kullanabilirsiniz.

EB_Score = ["Last Minuters" if i<7 else ("Potential Planners" if i<30 else ("Planners" if i<90 else "Early Bookers")) for i in df["SaleCheckInDayDiff"]]
df["EB_Score"] = EB_Score

#ÇÖZÜM VİDEOSUNDA YAPILAN:
bins = [-1, 7, 30, 90, df["SaleCheckInDayDiff"].max()]
labels = ["Last Minuters", "Potential Planners", "Planners", "Early Bookers"]

df["EB_Score"] = pd.cut(df["SaleCheckInDayDiff"], bins, labels=labels)



## Görev 3: Şehir-Concept-EB Score, Şehir-Concept- Sezon, Şehir-Concept-CInDay kırılımında ortalama ödenen ücret ve yapılan işlem sayısı cinsinden inceleyiniz ?
df.groupby(["SaleCityName","ConceptName","EB_Score"]).agg({"Price": ["mean", "count"]})
df.groupby(["SaleCityName","ConceptName","Seasons"]).agg({"Price": ["mean", "count"]})
df.groupby(["SaleCityName","ConceptName","CInDay"]).agg({"Price": ["mean", "count"]})


## Görev 4: City-Concept-Season kırılımının çıktısını PRICE'a göre sıralayınız.
agg_df = df.groupby(["SaleCityName","ConceptName","Seasons"])["Price"].mean()
agg_df.sort_values(ascending=False)

#ÇÖZÜM VİDEOSUNDA YAPILAN:
agg_df = df.groupby(["SaleCityName","ConceptName","Seasons"]).agg({"Price": "mean"}).sort_values("Price", ascending=False)


## Görev 5: Indekste yer alan isimleri değişken ismine çeviriniz.
# Üçüncü sorunun çıktısında yer alan PRICE dışındaki tüm değişkenler index isimleridir. Bu isimleri değişken isimlerine çeviriniz.
agg_df = agg_df.reset_index()


## Görev 6: Yeni seviye tabanlı müşterileri (persona) tanımlayınız.
# Yeni seviye tabanlı satışları tanımlayınız ve veri setine değişken olarak ekleyiniz.
# Yeni eklenecek değişkenin adı: sales_level_based
# Önceki soruda elde edeceğiniz çıktıdaki gözlemleri bir araya getirerek sales_level_based değişkenini oluşturmanız gerekmektedir

sales_level_based = (agg_df["SaleCityName"]+"_"+agg_df["ConceptName"]+"_"+agg_df["Seasons"]).str.upper()
df["sales_level_based"] = sales_level_based

#ÇÖZÜM VİDEOSUNDA YAPILAN:
agg_df["sales_level_based"] = agg_df[["SaleCityName", "ConceptName", "Seasons"]].agg(lambda x: '_'.join(x).upper(), axis=1)


## Görev 7: Yeni müşterileri (personaları) segmentlere ayırınız.
# Yeni personaları PRICE’a göre 4 segmente ayırınız.
# Segmentleri SEGMENT isimlendirmesi ile değişken olarak agg_df’e ekleyiniz.
# Segmentleri betimleyiniz (Segmentlere göre group by yapıp price mean, max, sum’larını alınız).
agg_df["SEGMENT"] = pd.qcut(agg_df["Price"], 4, labels=["D", "C", "B", "A"])
agg_df.groupby("SEGMENT").agg({"Price": ["mean", "max", "sum"]})


## Görev 8: Yeni gelen müşterileri sınıflandırıp, ne kadar gelir getirebileceklerini tahmin ediniz.
# Antalya’da herşey dahil ve yüksek sezonda tatil yapmak isteyen bir kişinin ortalama ne kadar gelir kazandırması beklenir?
# Girne’de yarım pansiyon bir otele düşük sezonda giden bir tatilci hangi segmentte yer alacaktır?
new_user = "ANTALYA_HERŞEY DAHIL_HIGH"
agg_df[agg_df["sales_level_based"] == new_user]