branch_a_products = {"bread", "milk", "butter", "jam"}
print(branch_a_products)
branch_b_products = {"bread", "cheese", "butter", "ketchup"}
print(branch_b_products)
union_of_both_branchs = branch_a_products | branch_b_products
print(union_of_both_branchs)
Intersecvtion_of_both_branchs = branch_a_products & branch_b_products
print(Intersecvtion_of_both_branchs)
Onyl_on_a = branch_a_products - branch_b_products
print(Onyl_on_a)
ketchup = "ketchup" in branch_a_products
print(ketchup)
essential_items = frozenset({"milk", "bread", "ketchup"})
print(essential_items)