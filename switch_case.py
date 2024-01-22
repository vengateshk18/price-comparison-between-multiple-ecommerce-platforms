import numpy as np
import pandas as pd
def compare():
    def product_matching(product):
     while(product != "Exit"):   
        match product:
            case 'iphone 14':
                print(" 128GB \n 256GB \n 512GB")
                storage = input("Enter storage capacity: ")
                match storage:
                    case '128':
                        print("Select Product")
                        print("APPLE iPhone 14 (Blue, 128 GB)")
                        print("APPLE iPhone 14 (Purple, 128 GB)")
                        print("APPLE iPhone 14 (Midnight, 128 GB)")
                        print("\n")
                        a=['APPLE iPhone 14 (Blue, 128 GB)','APPLE iPhone 14 (Purple, 128 GB)','APPLE iPhone 14 (Midnight, 128 GB)']
                        index=int(input("enter the product"))
                        product_select=a[index]
                        print(product_select)
                        match product_select:
                            case'APPLE iPhone 14 (Blue, 128 GB)':
                                return "APPLE iPhone 14 (Blue, 128 GB)"
                            case'APPLE iPhone 14 (Purple, 128 GB)':
                                return "APPLE iPhone 14 (Purple, 128 GB)"
                            case'APPLE iPhone 14 (Midnight, 128 GB)':
                                return "APPLE iPhone 14 (Midnight, 128 GB)"
                            case default:
                                print("The you searched is not found")
                                print("Please try any one of these")
                                return 0
                            
                    case '256':
                        print("Select Product")
                        print("APPLE iPhone 14 (Midnight, 256 GB)")
                        print("APPLE iPhone 14 (Blue, 256 GB)")
                        print("APPLE iPhone 14 (Starlight, 256 GB)")
                        print("\n")
                        product_select = input("Select any one among these: ")
                        match product_select:
                            case'APPLE iPhone 14 (Midnight, 256 GB)':
                                return "APPLE iPhone 14 (Midnight, 256 GB)"
                            case'APPLE iPhone 14 (Blue, 256 GB)':
                                return "APPLE iPhone 14 (Blue, 256 GB)"
                            case'APPLE iPhone 14 (Starlight, 256 GB)':
                                return "APPLE iPhone 14 (Starlight, 256 GB)"
                            case default:
                                return 0
                    case '512':
                        print("Select Product")
                        print("APPLE iPhone 14 (Yellow, 512 GB)")
                        print("APPLE iPhone 14 (Midnight, 512 GB)")
                        print("APPLE iPhone 14 (Blue, 512 GB)")
                        print("\n")
                        product_select = input("Select any one among these: ")
                        match product_select:
                            case'APPLE iPhone 14 (Yellow, 512 GB)':
                                return "APPLE iPhone 14 (Yellow, 512 GB)"
                            case'APPLE iPhone 14 (Midnight, 512 GB)':
                                return "APPLE iPhone 14 (Midnight, 512 GB)"
                            case'APPLE iPhone 14 (Blue, 512 GB)':
                                return "APPLE iPhone 14 (Blue, 512 GB)"
                            case default:
                                return 0
                    case default:
                        return
                    
    product = input("Enter product name: ")
    df = pd.read_excel("iphone_flipkart_data.xlsx")
    print(df.columns)
    head = product_matching(product)
    print("\n")
    if (head == 0):
       print("The product iyou searched is not found")
       print("Please try any one of these")
       print("To quit enter ","Exit")
       product_matching(product)
    else:
       print("Product you asked: ",str(head))
       cell_value=True
       if df['Product_name          '].str.contains(head).any(): 
           cell_value=True
       if cell_value==False:
           print("product searched not found")
       else:
          for index, row in df.iterrows():
             column_one_value = row.iloc[0]  # First column (index 0)
             column_two_value = row.iloc[1]
             if(column_one_value==head):
               print("The product price:",column_two_value)
               print("To quit enter ","Exit")
               print("To proceed enter Proceed")
               proceed=input()
               if(proceed == 'Proceed'):
                 product_matching(product)
               else:
                 print("Thank you")