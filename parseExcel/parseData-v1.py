# -*- coding: utf-8 -*- 
import xdrlib, sys, os
import xlrd

reload(sys)
sys.setdefaultencoding('utf-8') 

global fileName, keyRow
fileName = 'data_test.xlsx'

keyRow = 2#key行
typeRow = 1#数据类型行

parseIndexFunc = '''
let sheetName = [];
for (let i = 0; i < data.length; ++ i) {
	let tmpData = {};
	for (let j = 0; j < dataKeys.length; ++ j) {
		tmpData[dataKeys[j]] = data[i][j];
	}
	sheetName[i] = tmpData;
}
data = null;
'''

parseHashFunc = '''
let sheetName = {};
for (let key in data) {
	if (data.hasOwnProperty(key)) {
		let tmpData = {};
		for (let j = 0; j < dataKeys.length; ++ j) {
			tmpData[dataKeys[j]] = data[key][j];
		}
		sheetName[key] = tmpData;
	}
}
data = null;
'''

def parse_hash_str(hashStr):
	dataArr = hashStr.split(', ')
	keysArr = '['
	valuesArr = '['
	for i in xrange(0, len(dataArr)):
		keysArr += '\'' + dataArr[i].split(': ')[0] + '\''
		# valuesArr.append(dataArr[i].split(': ')[1])
		valuesArr += dataArr[i].split(': ')[1];
		if i < (len(dataArr) - 1):
			keysArr += ', '
			valuesArr += ', '
	keysArr += ']'
	valuesArr += ']'
	print valuesArr
	return keysArr, valuesArr

def parse_excel(fileName):
	data = xlrd.open_workbook(fileName)
	sheetsNames = data.sheet_names()

	for sheetName in sheetsNames:
		table = data.sheet_by_name(sheetName)

		# print table.nrows, table.ncols#行数和列数
		keys = table.row(keyRow)
		keysStr = '['
		contentStr = 'let data' + ' = '
		colStart = 0;
		tableType = table.cell(1, 0).value
		if tableType == 'key':
			contentStr += '{\n'
			colStart = 1
		elif tableType == 'index':
			contentStr += '[\n'

		for col in xrange(colStart, table.ncols):
			keysStr += '\'' + keys[col].value + '\''
			if table.cell(typeRow, col).value == 'hash':
				keysArr, valuesArr = parse_hash_str(str(table.cell(typeRow + 2, col).value))
				keysStr += ': ' + keysArr
			if col < table.ncols - 1:
				keysStr += ', '

		for row in xrange(keyRow + 1, table.nrows):
			if tableType == 'key':
				contentStr += '\t' + str(table.cell(row, 0).value) + ': '
			else:
				contentStr += '\t'
			contentStr += '['

			for col in xrange(colStart, table.ncols):
				# contentStr += keys[col].value + ': '
				dataType = table.cell(typeRow, col).value
				if dataType == 'n' or dataType == 'index':
					contentStr += str(int(table.cell(row, col).value))
				elif dataType == 's' or dataType == 'key':
					contentStr += '\"' + str(table.cell(row, col).value) + '\"'
				elif dataType == 'f':
					contentStr += str(float(table.cell(row, col).value))
				elif dataType == 'hash':
					keysArr, valuesArr = parse_hash_str(str(table.cell(row, col).value))
					contentStr += valuesArr
				elif dataType == 'arr':
					contentStr += '[' + str(table.cell(row, col).value) + ']'

				if col < table.ncols - 1:
					contentStr += ', '

			if row < table.nrows - 1:
				contentStr += '],\n'
			else:
				contentStr += ']\n'

		if tableType == 'key':
			contentStr += '};\n'
		elif tableType == 'index':
			contentStr += '];\n'

		keysStr += '];'
		contentStr += 'let dataKeys = ' + keysStr

		if tableType == 'key':
			parseStr = parseHashFunc.replace('sheetName', sheetName)
		elif tableType == 'index':
			parseStr = parseIndexFunc.replace('sheetName', sheetName)
		
		contentStr += parseStr + 'module.exports = ' + sheetName + ';'
		# print contentStr

		# if not os.path.exists('out'):
		# 	os.mkdir('out')
		fp = open('data/v1-' + sheetName + ".js", 'w')
		fp.write(contentStr)
		print sheetName + ' successful!'

def main():
   	parse_excel(fileName)
   		

if __name__=="__main__":
    main()