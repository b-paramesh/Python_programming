# delete_product.py
from supabase import create_client, Client
from dotenv import load_dotenv
import os
 
load_dotenv()
 
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)
 
def delete_product(product_id):
    resp = sb.table("products").delete().eq("product_id", product_id).execute()
    return resp.data
 
if __name__ == "__main__":
    pid = int(input("Enter product_id to delete: ").strip())
    confirm = input(f"Are you sure you want to delete product {pid}? (yes/no): ").strip().lower()
    if confirm == "yes":
        deleted = delete_product(pid)
        if deleted:
            print("Deleted:", deleted)
        else:
            print("No product deleted — check product_id.")
    else:
        print("Delete cancelled.")


def update_stock(product_id, new_stock):
    resp = sb.table("products").update({"stock": new_stock}).eq("product_id", product_id).execute()
    return resp.data
 
if __name__ == "__main__":
    pid = int(input("Enter product_id to update: ").strip())
    new_stock = int(input("Enter new stock value: ").strip())
 
    updated = update_stock(pid, new_stock)
    if updated:
        print("Updated record:", updated)
    else:
        print("No record updated — check product_id.")
 
 