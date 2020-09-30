#install module imageio terlebih dahulu
#buka terminal kemudian masukkan code 'pip3 install imageio' *untuk python3
import imageio
import os

clip = os.path.abspath('') 
#didalam tanda '' ,masukkan nama file mp4. biar lebih mudah masukkan file video dalam folder yang sama
#contoh clip = os.path.abspath('okay.mp4') 
def gifMaker (inputPath, targetFormat):
    outputPath = os.path.splitext (inputPath)[0] + targetFormat
    print(f'converting {inputPath} \n to {outputPath}')

    reader =imageio.get_reader(inputPath)
    fps = reader.get_meta_data()['fps']

    writer =imageio.get_writer(outputPath,fps=fps)
    for frames in reader:
        writer.append_data(frames)
        print(f'Frame {frames}')
    print ('Selesai!')
    writer.close()
gifMaker(clip,'.gif')
#clip untuk inputPath, dan targetFormat yang kita inginkan adalah gif