import pandas as pd
import difflib
def comparison_product_amazon(product_name):
    product_name=product_name.upper()
    read_file=pd.read_excel('amazon_data.xlsx')
    amazon=find_close_match(product_name,read_file,0.45)
    for i in range(0,len(amazon)):
       print("%d for %s" %(i+1,amazon[i][0]))
    exect_product=int(input("In this list select any one appropriate product!!! by any one number"))
    amazon_get=amazon[exect_product-1][0]
    print(amazon_get+":Your selection!!!")
    amazon=find_close_match(amazon_get,read_file,0.60)
    print(amazon)
def find_close_match(product_name,read_file,cutoff):
   sorted_values=read_file.sort_values('Product_price',ascending=True)
   similar_products = []
   for index, row in sorted_values.iterrows():
        product_title = row['Product_name']
        product_price = row['Product_price']
        if isinstance(product_title, str):
         similar_titles = difflib.get_close_matches(product_name,[product_title], n=1, cutoff=cutoff)
         if similar_titles:
            similar_product_title = similar_titles[0]
            similar_products.append((similar_product_title, product_price))
   print(len(similar_products)) 
   return similar_products
def comaparison_product_flipkart(product_name):
    product_name=product_name.upper()
    read_file=pd.read_excel('flipkart_data.xlsx')
    file_read_amazon=pd.read_excel('amazon_data.xlsx')
    flipkart=find_close_match(product_name,read_file,0.30)
    for i in range(0,len(flipkart)):
       print("%d for %s" %(i+1,flipkart[i][0]))
    exect_product=int(input("In this list select any one appropriate product!!! by any one number"))
    flipkart_get=flipkart[exect_product-1][0]
    print(flipkart_get+":Your selection!!!")
    flipkart=find_close_match(flipkart_get,file_read_amazon,0.55)
    for item in flipkart:
       print(item)
comaparison_product_flipkart("iphone 15 pro")
