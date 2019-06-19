# -*- coding: utf-8 -*- 
import xdrlib, sys, os
import xlrd

reload(sys)
sys.setdefaultencoding('utf-8') 

global fileName, keyRow
fileName = 'data_test.xlsx'

keyRow = 2#key行
typeRow = 1#数据类型行


def parse_excel(fileName):
	data = xlrd.open_workbook(fileName)
	sheetsNames = data.sheet_names()

	for sheetName in sheetsNames:
		table = data.sheet_by_name(sheetName)

		# print table.nrows, table.ncols#行数和列数
		keys = table.row(keyRow)
		contentStr = 'let ' + sheetName + ' = '

		colStart = 0;
		tableType = table.cell(1, 0).value
		if tableType == 'key':
			contentStr += '{\n'
			colStart = 1
		elif tableType == 'index':
			contentStr += '[\n'

		for row in xrange(keyRow + 1, table.nrows):

			if tableType == 'key':
				contentStr += '\t' + str(table.cell(row, 0).value) + ': '
			else:
				contentStr += '\t'
			contentStr += '{'

			for col in xrange(colStart, table.ncols):
				contentStr += keys[col].value + ': '

				dataType = table.cell(typeRow, col).value
				if dataType == 'n' or dataType == 'index':
					contentStr += str(int(table.cell(row, col).value))
				elif dataType == 's' or dataType == 'key':
					contentStr += '\"' + str(table.cell(row, col).value) + '\"'
				elif dataType == 'f':
					contentStr += str(float(table.cell(row, col).value))
				elif dataType == 'hash':
					contentStr += '{' + str(table.cell(row, col).value) + '}'
				elif dataType == 'arr':
					contentStr += '[' + str(table.cell(row, col).value) + ']'

				if col < table.ncols - 1:
					contentStr += ', '

			contentStr += '},\n'

		if tableType == 'key':
			contentStr += '};\n'
		elif tableType == 'index':
			contentStr += '];\n'


		contentStr += 'module.exports = ' + sheetName + ';'
		# print contentStr

		# if not os.path.exists('out'):
		# 	os.mkdir('out')
		fp = open('data/v0-' + sheetName + ".js", 'w')
		fp.write(contentStr)
		print sheetName + ' successful!'

def main():
   	parse_excel(fileName)
   		

if __name__=="__main__":
    main()