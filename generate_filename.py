'''generate_filename.py
   by jean-claude.feltes@education.lu
 
   generates a unique, numbered filename based on a pattern and a list of existing files
   get_next_filename(files, pattern) generates a new numbered filename of the pattern form
   pattern = basename_xxx.ext where xxx = number

   What for? To provide a means of creating e.g. logger files on an SD card, without the risk 
   of overwriting older ones 
'''

def fillup(number, nbdigits, padstr = '0'):
    ''' return string of integer number left padded with padstr'''
    s = str(number)
    l = len(s) 
    if l < nbdigits:
        s = padstr * (nbdigits - l) + s
    return s

def separate(name):
    '''separate filename of the form basename_xxx.ext where xxx = number
       into basename, number and extension'''
    try:
        nm, ext = name.split('.')
    except:
        nm = name
        ext = ''
        
    try:
        basename, number = nm.split('_')
    except:
        basename = nm
        number = '000'
    return basename, number, ext


def get_numbers(files, basename):
    ''' get list of numbers of files'''
    numbers = [] 
    for f in files:
        bname, number, ext = separate(f)
        #print(basename, number, ext)
        
        if bname == basename:
            numbers.append(number)
    numbers.sort()
    
    if len(numbers):
        biggest = numbers[-1]
    else:
        biggest = ''
    return numbers, biggest

def get_next_filename(files, pattern):
    '''get the next filename of the form pattern = basename_xxx.ext where xxx = number.
    If name pattern already exists, a new name with number incremented is returned,
    otherwise pattern is used as new name'''
    
    if files:
        basename, number, ext = separate(pattern)
        nbs, biggest = get_numbers(files, basename)
        n = int(biggest) + 1
        lengthnb = len(number)
        nb = fillup(n, lengthnb)
        #print(nb)
        newname = basename + '_' + nb + '.' + ext
    else:
        newname = pattern
    return newname

if __name__ == '__main__':
    # Test file list
    files = ['blah.txt', '8blah.txt', 'test.dat', 'test.txt', 'TEST',
         'blah_452.txt', 'blah_000.txt', 'blah_741.txt', 'blah_1.txt']

    # Tested also with these:
    #files = ['blah.txt', '8blah.txt', 'test.dat', 'test.txt', 'TEST',]
    #files = ['blah_020.txt']
    #files = []


    pattern = 'blah_00000.txt'
    name = get_next_filename(files, pattern)
    print(name)
