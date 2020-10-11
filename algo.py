import pandas as pd

def Float_Convert_Mask(x):
	try:
		float(x)
		return True # numeric, success!
	except ValueError:
		return False # not numeric
	except TypeError:
		return False # null type

def Float_Convert_Column(df, colName):
	return df[df[colName].map(Float_Convert_Mask)][colName].map(float)

def Get_Year_Low(df):
	temp = df['52 Week Range'].str.split(" - ", n=1, expand=True)
	return Float_Convert_Column(temp,0)

def Get_Year_High(df):
	temp = df['52 Week Range'].str.split(" - ", n=1, expand=True)
	return Float_Convert_Column(temp,1)

def Pre_Process(df):
	temp = df.copy()
	temp['Open'] = temp['Open'].str.replace(',','')
	temp['Volume'] = temp['Volume'].str.replace(',','')

	return temp

def Get_Magic_Val(df):
	'''Get 52 week high and low df'''
	'''(52 week high / (52 week high - 52 week low)) * Beta '''
	yearLow = Get_Year_Low(df)
	yearHigh = Get_Year_High(df)

	'''Get Beta Df'''
	beta = Float_Convert_Column(df,'Beta (5Y Monthly)')

	df['Magic'] = (yearHigh / (yearHigh - yearLow)) * beta

	return df

def Get_Stocks_More_Than(df, value=10):
	'''Check if stock is more than 10'''
	temp = df.copy()
	temp['Open'] = Float_Convert_Column(df,'Open')
	temp = temp[temp['Open'] > value]
	return temp

def Get_Stocks_Less_Than(df, value=1000):
	'''Check if stock is less than 1000'''
	temp = df.copy()
	temp['Open'] = Float_Convert_Column(df,'Open')
	temp = temp[temp['Open'] < value]
	return temp

def Get_Volume_More_Than(df, value=200000):
	'''Check if Volume is more than 200000'''
	temp = df.copy()
	temp['Volume'] = Float_Convert_Column(df,'Volume')
	temp = temp[temp['Volume'] > value]
	return temp

def Length_Invest_From_Beta(df, length):
	temp = df.copy()
	temp['Beta (5Y Monthly)'] = Float_Convert_Column(df,'Beta (5Y Monthly)')
	if 'short' in length:
		temp = temp[temp['Beta (5Y Monthly)'] >= 1.1]
		temp = temp[temp['Beta (5Y Monthly)'] <= 1.8]
	elif 'med' in length:
		temp = temp[temp['Beta (5Y Monthly)'] >= 0.9]
		temp = temp[temp['Beta (5Y Monthly)'] <= 1.1]
	elif 'long' in length:
		temp = temp[temp['Beta (5Y Monthly)'] >= 0.2]
		temp = temp[temp['Beta (5Y Monthly)'] <= 0.9]

	return temp

def Length_Invest_From_Formula(df, length):
	temp = Get_Magic_Val(df)
	temp['Magic'] = Float_Convert_Column(temp,'Magic')
	if 'short' in length:
		temp = temp[temp['Magic'] >= 2]
	elif 'med' in length:
		temp = temp[temp['Magic'] >= 2.1]
	elif 'long' in length:
		temp = temp[temp['Magic'] >= 1.5]
		temp = temp[temp['Magic'] <= 2.6]

	return temp

def Prev_Close_Form(df):
	'''Only performed on short and long term'''
	'''abs((previous_close - 52 week high) > (previous_close * 0.10)'''
	temp = df.copy()
	temp['Previous Close'] = Float_Convert_Column(temp,'Previous Close')

	yearLow = Get_Year_Low(df)
	yearHigh = Get_Year_High(df)

	temp = temp[abs(temp['Previous Close']-yearHigh) > (temp['Previous Close']*0.10)]
	return temp


'''Finds best stock given length of investment
	input: float investment_amount, string (short,med,long)
	returns dictionary of statistics of best stock
'''
def Get_Stock(money, length):
	df = pd.read_csv('data_final.csv')
	print(df)
	procDf = Pre_Process(df)

	temp = Get_Stocks_Less_Than(procDf)
	temp = Get_Stocks_More_Than(temp)
	temp = Get_Volume_More_Than(temp)

	temp = Length_Invest_From_Beta(temp,length)
	temp = Length_Invest_From_Formula(temp,length)

	if (('short' in length) or ('long' in length)):
		temp = Prev_Close_Form(temp)
	
	''' Cool Machine Learning goes here :( '''
	duckling = temp.sample(1)
	return {'Ticker':duckling['ticker'].values[0],
			'Beta':duckling['Beta (5Y Monthly)'].values[0],
			'Previous Close':duckling['Previous Close'].values[0],
			'Open':duckling['Open'].values[0],
			'Bid':duckling['Bid'].values[0],
			'Days Range':duckling['Day\'s Range'].values[0],
			'52 Week Range':duckling['52 Week Range'].values[0],
			'Volume':duckling['Volume'].values[0],}

'''
/(52 week high / (52 week high - 52 week low)) * Beta 

abs((previous_close - 52 week high) > (previous_close * 0.10) && // Apply this only to long and short term investments

/Is stock > 10 
/Is stock < 1000

->Is stock at least 1 year old?

/Is traded stock volume > 200k

/Beta > 0.2 Beta < 1.8

/Assume short Term < 6 Weeks Mid Term < 6 months Long Term > 1 year

/Categorized: Long Term Investment 0.2 - 0.9 Mid Term Investment 0.9 - 1.1 Short Term Investment 1.1 - 1.8

/From Formula Long Term 1.5 - 2.6  Mid Term > 2.1 Short Term > 2.0

'''