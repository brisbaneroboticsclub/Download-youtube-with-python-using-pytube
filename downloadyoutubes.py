from pytube import YouTube

'''

https://github.com/pytube/pytube
https://pytube.io/en/latest/api.html#pytube.Stream.download

Install pytube on your OS
pip install pytube

'''

# Specify the youtube URL you want to download here.
yt = YouTube('http://youtube.com/watch?v=2lAe1cqCOXo')

#print(dir(yt))

print('-------------')

data =''

# Keep trying to obtain stream data until successful.
while data == '':
    #print('Attempt ',i)
    try:
        data = yt.streams
        #print(data)
        #print(type(data))

        # Only select mp4 streams.
        data = yt.streams.filter(file_extension='mp4')

    except:
        print('No response. Retrying now.')
        print('-------------')

#Print the streams available
print('Youtube mp4 data streams available.')
for datum in data:
    print(datum)

print('Downloading now.')

# Insert a tag number from results here.
stream = yt.streams.get_by_itag(18)

# Change file dpwnload attributes here.
x = stream.download(filename = 'pytyubedownload.mp4')

print('Your file "',yt.title,'" is located in this folder: ',x)

print('Download Complete.')