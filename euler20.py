def digit_means(num):
	prod_cont = 1
	i = 1
	while num >= 1:
		prod_cont = prod_cont * num
		num = num - 1
	return prod_cont

def  factorial_digit(num):
	my_str_num =str(digit_means(num))
	my_num_ls = []
	while my_str_num != "" :
		my_append_num = int(my_str_num[:1])
		my_num_ls.append(my_append_num)
		my_str_num =my_str_num[1:]
	return my_num_ls
def factorial_digit_sum(num):
	my_ls_of_nums = factorial_digit(num)
	return sum(my_ls_of_nums)


print factorial_digit_sum(10)
#>>> 27
print factorial_digit_sum(100)