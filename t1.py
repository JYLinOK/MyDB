import mydb


a = [
   "product_id INT NOT NULL AUTO_INCREMENT",
   "product_name VARCHAR(100) NOT NULL",
   "product_manufacturer VARCHAR(40) NOT NULL",
   "submission_date DATE",
   "PRIMARY KEY ( product_id )"
]

# a = '123456'
# print(f'{a[:-1] = }')

# s = ['123,', '456', '789,']
# print(f'{str(a) = }')


b = (1, 2, 3)
b = [1, 2, 3]
print(f'{tuple(b) = }')
print(f'{type(tuple(b))= }')



