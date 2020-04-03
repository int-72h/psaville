from PIL import ImageDraw, Image
from sys import argv
numbers = {
'0' : '#ffffff',
'1' : '#33bcad',
'2' : '#ffff00',
'3' : '#8781bd',
'4' : '#f58220',
'5' : '#8ed8f8',
'6' : '#f6adcd',
'7' : '#584099',
'8' : '#ec008c',
'9' : '#00aeef',
}
colours = {
' ' : ' ',
'A' : numbers['1'],
'B' : numbers['2'],
'C' : numbers['3'],
'D' : numbers['4'],
'E' : numbers['5'],
'F' : numbers['6'],
'G' : numbers['7'],
'H' : numbers['8'],
'I' : numbers['9'],
'J' : [numbers['1'],numbers['0']],
'K' : [numbers['1'],numbers['1']],
'L' : [numbers['1'],numbers['2']],
'M' : [numbers['1'],numbers['3']],
'N' : [numbers['1'],numbers['4']],
'O' : [numbers['1'],numbers['5']],
'P' : [numbers['1'],numbers['6']],
'Q' : [numbers['1'],numbers['7']],
'R' : [numbers['1'],numbers['8']],
'S' : [numbers['1'],numbers['9']],
'T' : [numbers['2'],numbers['0']],
'U' : [numbers['2'],numbers['1']],
'V' : [numbers['2'],numbers['2']],
'W' : [numbers['2'],numbers['3']],
'X' : [numbers['2'],numbers['4']],
'Y' : [numbers['2'],numbers['5']],
'Z' : [numbers['2'],numbers['6']],
}

def drawLetter(x,y,col,sep=1):
	im = Image.new('RGB', (x,y), 'white')
	draw = ImageDraw.Draw(im)
	if type(col) == list:
		draw.rectangle([(0,0),(x,(y/2)-sep)],col[1])
		draw.rectangle([0,y/2,x,y],col[0])
	elif col == ' ':
		im = Image.new('RGB', (x,y), 'black')
		draw = ImageDraw.Draw(im)
##		draw.polygon([x/8,0,0,y/8,0,y/8,0,7*(y/8),0,7*(y/8),x/8,y,x/8,y,7*(x/8),y,7*(x/8),y,x,7*(y/8),x,7*(y/8),x,y/8,x,y/8,7*(x/8),0,7*(x/8),0,x/8,0],'gray')
	else:
		draw.rectangle([0,0,x,y],col)
	return im

def main(text,filename,x,y,vert=None):
	if x % len(text) or y % len(text):
		print('cant have fractional pixels, size wont be exact')
	x = round(x/len(text))   
	y = round(y/len(text))
	n = 0
	images = []
	inp = [char.upper() for char in text]
	print(inp)
	while n < len(inp):
		if inp[n] in colours:
			images.append(drawLetter(x,y,colours[inp[n]]))
		if inp[n] in numbers:
			if len(inp) == 1:
				images.append(drawLetter(x,y,numbers[inp[n]]))
			if inp[n+1] in numbers:
				print(inp[n])
				images.append(drawLetter(x,y,[numbers[inp[n]],numbers[inp[n+1]]]))
				n = n + 2
				continue
			if inp[n-1] not in numbers or n == 0:
				images.append(drawLetter(x,y,numbers[inp[n]]))
		n +=1
	print(images)        
	widths, heights = zip(*(i.size for i in images))
	total_width = sum(widths)
	max_height = max(heights)
	new_im = Image.new('RGB', (total_width, max_height),'gray')
	offset = 0
	for im in images:
	  new_im.paste(im, (offset,0))
	  offset += im.size[0]
	  if vert == '-v':
	   new_im.transpose(Image.ROTATE_270)
	new_im.save(filename)
	
if len(argv) < 4:
	print('Needs at least some text, a file name, x and y size.')
if len(argv) == 5:
	main(argv[1],argv[2],int(argv[3]),int(argv[4]))
if len(argv) == 6:
		main(argv[1],argv[2],argv[3],argv[4],argv[5])
