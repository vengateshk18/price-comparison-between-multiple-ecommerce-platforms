import flipkart as fk
import amazon as az
import snapdeal as snap
import switch_case
import delete_file
user_product=input("Enter the product:")
fk.scrap_flipkart(user_product)
az.scrap_amazon(user_product)
snap.scrap_snapdeal(user_product)