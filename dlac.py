import os, sys

urls = sys.argv[2:]

outfile = sys.argv[1] # With file extension

os.system('mkdir tempaudio')
os.system('touch tempaudio/key.txt')

key = ''

for i,u in enumerate(urls):
    os.system(f'wget {u} -O tempaudio/TBC_{i}.mp3')
    key += f"file 'tempaudio/TBC_{i}.mp3'\n"

with open('tempaudio/key.txt','w') as f:
    f.write(key)

os.system(f'ffmpeg -f concat -safe 0 -i tempaudio/key.txt -c copy {outfile}')
os.system('rm -r tempaudio')
