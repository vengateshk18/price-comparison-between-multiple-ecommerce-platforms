import os
file_to_delete_amazon = 'amazon_data.xlsx'
file_to_delete_flipakart='flipkart_data.xlsx'
file_to_delete_snapdeal='snapdeal_data.xlsx'
try:
    os.remove(file_to_delete_amazon)
    os.remove(file_to_delete_flipakart)
    os.remove(file_to_delete_snapdeal)
    print(f"File '{file_to_delete_flipakart} 'and' {file_to_delete_amazon} has been deleted.")
except FileNotFoundError:
    print(f"File '{file_to_delete_amazon} 'or' {file_to_delete_flipakart} not found. It may have already been deleted or never existed.")
except Exception as e:
    print(f"An error occurred while trying to delete the file: {str(e)}")
