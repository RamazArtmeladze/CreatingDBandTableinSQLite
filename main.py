import sqlite3
print("\nგამარჯობა,\nთქვენ იმყოფებით სისტემაში, სადაც შესაძლებელია \nსტრუქტურიზებული მონაცემთა ბაზის შექმა.\nგთხოვთ, მიჰყევით ინსტრუქციას.\n")

# 1) ის ინტერაქტიულ რეჟიმში გვეკითხება, თუ რა სახელით გვსურს ბაზის შექმნა;
db_name = input("შეიყვანეთ მონაცემთა ბაზის დასახელება: ")+".db"

# 2) შემდეგ პროგრამა გვეკითხება თუ რა სახელით შექმნას მან ცხრილი აღნიშნულ ბაზაში;
table_name = input("შეიყვანეთ შესაქმნელი ცხრილის დასახელება: ")

# 3) შემდეგ ნაბიჯზე პროგრამამ გვკითხოს თუ რამდენი სვეტი უნდა გააჩნდეს აღნიშნულ ცხრილს;
inp_check = True

while inp_check:
    try:
        col_num = int(input("შეიყვანეთ საჭირო სვეტების რაოდენობა: "))
        inp_check = False
    except:
        print("გთხოვთ შეიყვანოთ რიცხვი სწორ ფორმატში!")

# 4) მოხდეს აღნიშნული რაოდენობის სვეტების სახელების და მათი ტიპების ინტერაქტიულად შეტანა;
data_types = ["NULL", "INTEGER", "REAL", "TEXT", "BLOB"]

col_names =[]
col_dict = {}

for i in range(col_num):
    dat_check = True
    col_name = input(f"შეიყვანეთ სვეტი N.{i+1} დასახელება: ")
    col_names.append(col_name)
    while dat_check:
        col_type = input(f"შეიყვანეთ სვეტი N.{i+1} ტიპი (NULL, INTEGER, REAL, TEXT, BLOB): ").upper()
        if col_type in data_types:
            dat_check = False
    col_dict[col_name] = col_type

# 5) საბოლოოდ კი შეიქმნას ბაზა და მასში ცხრილი მითითებული სვეტებით;
class NewDataBase:

    def __init__(self, db_name, table_name,col_num,col_names,col_dict):
        self.db_name = db_name
        self.table_name = table_name
        self.col_num = col_num
        self.col_names = col_names
        self.col_dict = col_dict

    def create_db(self):
        db_text = f"CREATE TABLE IF NOT EXISTS {self.table_name}(\n"
        for i in self.col_names:
            db_text = db_text + "    " + i + " " + col_dict[i] + ", "
        db_text = db_text[0:-2] + ")"

        with sqlite3.connect(self.db_name) as connection:
            cursor = connection.cursor()

        cursor.execute(db_text)
        connection.commit()

        cursor.close()
        connection.close()



database = NewDataBase(db_name, table_name,col_num,col_names,col_dict)
database.create_db()
