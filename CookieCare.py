# encoding:utf-8
import math

def calories_needed_per_day(cat_weight, coef):
	'''
	计算每天所需的热量（单位：cal）。
	
	:param cat_weight: 曲奇猫体重值，单位：g
	:param coef: 系数值，无单位
	:return: 每天所需的热量（单位：cal）
	'''
	calories = ((cat_weight / 1000) ** 0.75) * 70 * coef * 1000
	return calories
	
def cal_dry_food_gram(cat_weight, coef, dry_food_unit_heat, canned_food_total_calories, canned_food_weight = None, canned_food_unit_heat = None):
	'''
	计算除去罐头之后，每天还需要的干猫粮重量（单位：g）
	
	:param cat_weight: 曲奇猫体重值，单位：g
	:param coef: 系数值，无单位
	:param dry_food_unit_heat: 干猫粮单位热量值，单位：kcal/kg
	:param canned_food_total_calories: 猫罐头提供的总热量，单位：cal
	:param canned_food_weight: 猫罐头重量，单位：g
	:param canned_food_unit_heat: 猫罐头单位热量值，单位：kcal/kg
	:return: 除去罐头之后，每天还需要的干猫粮重量（单位：g）
	'''
	# 计算出每天所需的热量（单位：cal）
	calories_needed = calories_needed_per_day(cat_weight, coef)
	
	# 计算猫罐头可提供的热量（单位：cal）
	if not canned_food_total_calories:
		canned_food_total_calories = canned_food_unit_heat * canned_food_weight
	
	# 计算除了罐头之外，还需要的剩余热量值（单位：cal）
	other_calories = calories_needed - canned_food_total_calories
	
	# 根据干猫粮的单位热量值计算需要的干猫粮重量（单位：g）
	dry_food_weight = other_calories / dry_food_unit_heat
	return round(dry_food_weight, 2)
	
def main():
	# 输入体重（单位：kg）
	weight = float(input('请输入曲奇的体重（单位：kg）：'))
	
	# 输入系数
	print('''
系数参考值：
四个月以下猫：3
四个月以上至一岁猫：2
运动量大的成年猫：1.6
未绝育的成年猫：1.4
绝育的成年猫：1.2
肥胖成年猫：1.0
减肥成年猫：0.8\n''')
	coef = float(input('请输入系数（具体系数见上面的系数参考值）：'))
	
	# 输入一罐罐头的热量值（单位：kcal）
	a_canned_food_total_heat = float(input('请输入一罐罐头的热量值（单位：kcal）：'))
	
	# 请输入喂食罐头的罐数
	canned_food_num = float(input('请输入喂食罐头的罐数：'))
	
	# 请输入干猫粮每千克的热量值（单位：kcal/kg）
	dry_food_unit_heat = float(input('请输入干猫粮每千克的热量值（单位：kcal/kg）：'))

	dry_food_gram = cal_dry_food_gram(weight * 1000, coef, dry_food_unit_heat, a_canned_food_total_heat * 1000 * canned_food_num)
	
	print('\n\n======= 计算结果 =======')
	print('曲奇今天需要的总热量为：{}kcal'.format(round(calories_needed_per_day(weight * 1000, coef) / 1000, 2)))
	print('罐头提供的热量为：{}kcal'.format(round(a_canned_food_total_heat  * canned_food_num, 2)))
	if dry_food_gram < 0:
		print('罐头热量超标（超出了{}kcal)，不需要再喂食猫粮！'.format(round(abs(dry_food_gram * dry_food_unit_heat) / 1000, 1)))
	else:
		print('除了罐头之外，还需补充的热量为：{}kcal，换算成还需喂的猫粮重量为：{}克'.format(round(dry_food_gram * dry_food_unit_heat / 1000, 2),dry_food_gram))

if __name__ == '__main__':
	while True:
		main()
		is_continue=input('\n\n\n==========\n是否继续计算（输入Y：是；输入N：否，退出程序）：')
		if is_continue in ['y', 'Y']:
			continue
		else:
			break