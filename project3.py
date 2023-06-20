#/Users/alhelal/Desktop/467 Chaya/proj3/

import argparse
import csv
import datetime
from fileinput import filename
from importlib.metadata import files
from importlib.resources import path
import math
import os
from posixpath import split
import re
import pymongo
import subprocess
#from pymongo import MongoClient
import sys
import cv2
import xlsxwriter
#from opencv-python import cv2
print("Thank You Professor Chaja for the wonderful class")
print("FML")

def main(input, outputarg):
    testkey = [] 
    frames = "frames"
    print("works")
    print(f"Processing video file: {input}")
    input_file = "twitch_nft_demo.mp4"
    output = "/Users/alhelal/Desktop/467 Chaya/proj3/"
    start_frame = 0
    end_frame = 11000
    frame_rate = 1
    output_dir = os.path.join(output, 'frames')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Open the video file
    video_file = input
    cap = cv2.VideoCapture(video_file) #cap is representing a cv2.VideoCapture object

    frame_number = 0
    frame_list= []
    """
    while cap.isOpened():
        ret, frame = cap.read()
        # Break the loop if we have reached the end of the video
        if not ret:
            break

        # Save the current frame as an image
        frame_filename = os.path.join(output_dir, f'frame{frame_number:04d}.png')
        cv2.imwrite(frame_filename, frame)

        #frame_list.append(frame)

        frame_number += 1




    cap.release()
    cv2.destroyAllWindows()"""
    print("first run to get frames")
    print("second run to get the frames from the folder. Recommended to comment out the os.pathcheck and the cap - cv2 destroywindows code.")
 
    frame_directory = "/Users/alhelal/Desktop/467 Chaya/proj3/frames"
    png_files = [f for f in os.listdir(frame_directory) if f.endswith('.png')]
    frame_pattern = re.compile(r'frame(\d{4})\.png')
    #connect()
    
    frame_list = [int(frame_pattern.search(f).group(1)) for f in png_files if frame_pattern.search(f)]
    #file_numbers = set
    #xytech = []
    xytech_dict = {}
  
    #print(sorted(frame_list))
    max_frame_num = max(frame_list)
    print(max_frame_num)
    client = pymongo.MongoClient("mongodb+srv://alazmine:Muda@cluster0.fdnlwld.mongodb.net/?retryWrites=true&w=majority")
    #db = client["database"]
    #db = client['mydatabase']
    mydb = client["mydatabase"]
    filesub = mydb["files"]
    mycollection = mydb["mycollection"]
    collection2 = mydb["collection2"]
    xytechbasenumfiles =[]
    newlist = []
    filepaths = []
    filerange = []
    testing = {}
    for entry in collection2.find({}, {"Files to Fix": 1}):
        files_to_fix = entry.get("Files to Fix", [])
        
        xytechbasenumfiles.append(files_to_fix)
    
    print(f'{files_to_fix}\n')
    print("\n")
    #print("split_each")
    #print(xytechbasenumfiles)
    for eachpath in xytechbasenumfiles:
        for path in eachpath:
            split_value = path.split()
            keypath = split_value[0]
            numrange = split_value[1]
            if keypath in xytech_dict:
                xytech_dict[keypath].append(numrange)
            else:
                xytech_dict[keypath] = [numrange]
    print("below is xytechandbasefilenum")
    print("outside of test")
    print("\n")
    for key, value in xytech_dict.items():
        print(f"Key: {key}, Value: {value}")
    """
    testdict2 = {}
    testval2 = []
    for document in collection2.find():
        # Check if the 'Files to Fix' field is present in the document
        if "Files to Fix" in document:
            # Iterate through the 'Files to Fix' and process each path
            for path in document["Files to Fix"]:
               #print(path)
                testval2.append(path)
     print("split_each")
    for eachpath in testval2: 
        split_each = eachpath.split()
        keypath = split_each[0]
        numrange = split_each[1]
        if keypath in testdict2:
            testdict2[keypath].append(numrange)
        else: 
            testdict2[keypath] = [value]
            
        #print(split_each)#works
        #print(keypath)#works
        #print(numrange)#works

    #works
    #print("testval2")
    #for each in testval2:
    #    print(each)
    print("testdict2")
    for key, value in testdict2.items():
        print(f"Key: {key}, Value: {value}")
        """

                
    """
    new_frames_hmap = {}
    for document in collection2.find():
        # Check if the 'Files to Fix' field is present in the document
        if "Files to Fix" in document:
            # Iterate through the 'Files to Fix' and process each path
            for path in document["Files to Fix"]:
                path_parts = path.split()
                if len(path_parts) == 2:
                    location, frame_range = path_parts
                    testkey.append(location)
                    if "-" not in frame_range:
                        # Case of single frame number
                        frame_num = int(frame_range)
                        if frame_num <= max_frame_num:
                            if location not in new_frames_hmap:
                                new_frames_hmap[location] = []
                            new_frames_hmap[location].append([frame_num])
                    else:
                        # Case of frame range
                        start, end = frame_range.strip('[]').split('-')
                        if int(end) <= max_frame_num and int(start) <= max(frame_list):
                            if location not in new_frames_hmap:
                                new_frames_hmap[location] = []
                            new_frames_hmap[location].append(list(range(int(start), int(end) + 1)))

    

    #print(sorted(frame_list))
    print('this is the hmap\n')

    
    for key, value in new_frames_hmap.items():
        print(f"Key: {key}, Value: {value}")
    """
    #print(xytechbasenumfiles)
    

    #print(newlist)
    #print(filepaths)
    #print(filerange)
    
    """
    for entry in mydb.collection2.find({}, {"Files to Fix": 1}):
        files_to_fix = entry.get("Files to Fix", [])
        for file in files_to_fix:
          path, *nums = file.split()
          if not nums:
            continue
          nums = nums[0].strip("[]")
          if "-" in nums:
            start, end = nums.split("-")
            start, end = int(start), int(end)
            if end <= max_frame_num:
                xytech_dict[path] = list(range(start, end + 1))
          else:
            num = int(nums)
            if num <= max_frame_num:
                xytech_dict[path] = [num]
                """
    """
    for doc in collection2.find():
        if "Files to Fix" in doc:
            for each in doc["Files to Fix"]:
                 #print( (int)( each))
                 
                 print(each)
                 path_and_numbers = each.strip().split(" ")
                # print("Path and numbers")
                 print("Path and numbers", path_and_numbers)
                 path = path_and_numbers[0]
                 numbers = path_and_numbers[1]
                 #print(path)
                 #print(numbers)
                 #xytech_dict[path] = numbers
                 if len(path_and_numbers) >= 2:
                    path = ' '.join(path_and_numbers[:-1])

                       
                    #numbers = path_and_numbers[-1]
                    #if numbers in frame_list:
                       #if path not in xytech_dict:
                        #xytech_dict[path] = []
                       #xytech_dict[path].append(numbers)
                      #this got the numbers but put it not right keys
                    #  if "[" in path_and_numbers[-1] and "]" in path_and_numbers[-1]:
                     #    range_str = path_and_numbers[-1].replace("[", "").replace("]", "")
                     #    start, end = range_str.split("-")
                    #     filerange.extend(list(range(int(start), int(end) + 1)))
                    #  else:
                    #    filerange.append(int(path_and_numbers[-1]))
                      #xytech_dict[path] = filerange
                       #path = path_and_numbers[0]
                     
                                 #xytech_dict[path] = testnumber
                       #testnumbers = path_and_numbers[1:]
                       #testnumbers = [int(num) for num in (' '.join(path_and_numbers[1:]))]
                       
                       #pathv2 = path_and_numbers[0]
                       #numberv2 = path_and_numbers[1]
                       #path = ' '.join(path_and_numbers[:-1]) get file and beginning numbers
                       #print("b4path", path)
                      # path = ' '.join(path_and_numbers[:-1])
                       #numbers = path_and_numbers[-1].replace("[", "").replace("]", "")
                       
                       #numbers = path_and_numbers[-1]
                       #pathafterv1 = path_and_numbers[0]
                    numbers = path_and_numbers[-1]
                       
                      # filepaths.append(path)
                      # filerange.append(numbers)
                       #print("pathv2", pathv2)
                       #print("numberv2", numberv2)
                       #print("Path:", path)
                       #print("Numbers:", numbers)
                      # if any(int(n) in frame_list for n in path_and_numbers[1:]):
                    xytech_dict[path] = numbers

                       #start, end = numbers.split('-')
                       #if '-' in numbers:
                        #  start, end = numbers.split('-')
                       #else:
                        #  start = end = numbers
                       #xytech_dict[path] = (start, end)
                       #xytech_dict[path] = {'start': int(start), 'end': int(end)}
                       #print("before splitjoin")
                       #numbers = ''.join(c if c.isdigit() else ' ' for c in numbers)
                       #numbers = numbers.strip().split()
                      # print(numbers)
                       #xytech_dict[path] = numbers
                 
                 each = each.strip()  # remove any extra spaces around the string
                 parts = each.split(' ')  # split the path and numbers by space
                 if len(parts) > 1:
                      path = parts[0]
                      nums = parts[1]
                      nums = nums.strip('[]')  # remove the brackets around the numbers
                      nums = nums.replace('-', ':')  # replace dash with colon to make a range
                      nums = nums.split(':')  # split the numbers into a list
                      nums = [int(num) for num in nums]  # convert the numbers to integers
                      num_range = list(range(nums[0], nums[-1]+1))  # create a list of numbers from the range
                      #xytech_dict[path] = num_range  # add the path and numbers to the dictionary

                
                 #parts = each.split()
                 
                 #path = parts[0]
                #nums = ' '.join(parts[1:])
                # nums = nums.strip('[]')
                #xytech_dict[path] = nums.split()

                 #file_numbers.append(each.strip())
                 #file_numbers.add(each)
                 #xytech.append(each)
                 #test = each
                 #mylist = list(set(each))
    else:
        print("No frame_ranges field found in the document with _id:", doc["_id"])
    """
    #print(filepaths)
    #print(filerange)
    #xytech_dict[filepaths] = filerange
    #print(f"\n{xytech_dict}")
    #print("xytech")
    #for key, value in xytech_dict.items():
     #   print(f"Key: {key}, Value: {value}")
    
    testdict = {}
    testval = set()
    """for key, value in xytech_dict.items():
        for i in range(len(value)):
            if '-' in value[i]:
                start, end = value[i].strip('[]').split('-')
                value[i] = list(range(int(start), int(end)+1))
    
       # if isinstance(value[i], list):
        #if isinstance(value, list) and len(value) > 0 and isinstance(value[0], list):
         #   values = [item for sublist in value for item in sublist] + value[1:]
            #splitvalues.append(value)
        
                testdict[key] = value
          
    """
    """ testval = set()
    for key, value in xytech_dict.items():
        modified_value = []
        for item in value:
            if '-' in item:
                start, end = item.strip('[]').split('-')
                modified_value.extend(list(range(int(start), int(end) + 1)))
        if modified_value:
            testdict[key] = modified_value"""

    testval = set()
    for key, value in xytech_dict.items():
        modified_value = []
        for item in value:
            if '-' in item:
                start, end = item.strip('[]').split('-')
                modified_value.extend(filter(lambda x: x <= 5918, range(int(start), int(end) + 1)))
        if modified_value:
            testdict[key] = modified_value
    print("testdict")
    #print(testdict)
    for key, value in testdict.items():
        print(f"Key: {key}, Value: {value}")

    #for key in new_frames_hmap:
    #    testkey.append(key)
    #print(testkey)
            
    print("\n")
    fps = get_fps(input)
    print("\n")
    print("FPS: ",fps)
    lengthofvid = get_vid_length(input)
    print("\n")
    print("Length of video: ",lengthofvid)
    fpscheck = int(fps * lengthofvid)
    print("\n")
    print("FPSCHECK: ",fpscheck)
    testval = []
    
    for key, value in testdict.items():
        for item in value:
         if isinstance(item, list):
            for sub_item in item:
                testval.append(sub_item)
         else:
            testval.append(item)
    testval = list(set(testval))
    print("Value Check: ")
    print("\n")
    print(sorted(testval))
    #timecode = []
    
    deci_seconds = list(set([frame_number/fps for frame_number in  testval]))
    #timecode = ''
    deci_seconds.sort()

    """  for deci in testval:
        seconds, milliseconds = divmod(int(deci * 1000), 1000)
        hours, seconds = divmod(seconds, 3600)
        minutes, seconds = divmod(seconds, 60)
        timecode += f"{hours:02d}:{minutes:02d}:{seconds:02d},{milliseconds:03d}"
        timecode += ":"
    
    """
    timecode = convert_frames_to_timecodes(testval, fps)
    print("finally")

    print("\n")
    print("\n",sorted(timecode))
 
    #num_deci = len(deci_seconds)
    print("\n")
    #print(deci_seconds)
    print(len(testkey))
    print(len(testval))
    print(len(timecode))
    #print(f"There are {num_deci} deci_seconds.")
    print("\n")
    #print(f"\n{timecode}\n")
    #num_time = len(timecode)
    #print(f"There are {num_time} numtime.")
    #cmd = ['ffprobe', '-select_streams', 'v', '-show_entries', 'frame=coded_picture_number,timecode', '-of', 'csv', '-i', input]

    #result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #if result.returncode == 0:
    #    print(result.stdout.decode())
    #else:
     #   print(result.stderr.decode())
    #extract(input)
    ranges_dict = {}
    row = 1
    
    for key, value in testdict.items():
        location = key
        ranges = []

        # Sort the frames in ascending order
        sorted_frames = sorted(value)

        start_frame = sorted_frames[0]
        end_frame = sorted_frames[0]
        for frame in sorted_frames[1:]:
            if frame == end_frame + 1:
                end_frame = frame
            else:
                ranges.append((start_frame, end_frame))
                start_frame = frame
                end_frame = frame

        # Add the last range
        ranges.append((start_frame, end_frame))

        ranges_formatted = [f"[{start}-{end}]" if start != end else f"[{start}]" for start, end in ranges]
        ranges_dict[location] = ranges_formatted
        sorted_items = sorted(ranges_dict.items(), key=lambda x: (min(int(val[1:-1].split('-')[0]) for val in x[1])))
    print(ranges_dict)
    if outputarg == "csv": 
        print("CSV File output\n")
        #f = open("project.csv", "x")
        with open("project3.csv", "w", newline="") as csvfile:
            fields= ["Location", "Ranges"]
            thewriter = csv.DictWriter(csvfile, fieldnames=fields)
            thewriter.writeheader()
            Write = csv.writer(csvfile)
            splitDR = ["Directory", "Frame_Ranges"]
            lastWrite = csv.DictWriter(csvfile, fieldnames = splitDR)
         
            for eachloc, eachval in sorted_items:
                #lastWrite.writerow({"directory": eachloc, "frames": ""})
                for number in eachval:
                    lastWrite.writerow({"Directory": eachloc, "Frame_Ranges": number})

            

           
            #Write = csv.writer(csvfile)
            #csvfile.write("Location,Ranges,Timecode,Thumbnail\n")
   
    elif args.output == "xls":
        print("XLS output")
        workbook = xlsxwriter.Workbook("project3.xlsx")
        worksheet = workbook.add_worksheet()
        #worksheet.set_column('A:A', 15)  # Location
        #worksheet.set_column('B:B', 20)  # Ranges
        #worksheet.set_column('C:C', 15)  # Timecode
        #worksheet.set_column('D:D', 30)         
        worksheet.write(0, 0, "Location")
        worksheet.write(0, 1, "Ranges")
        worksheet.write(0, 2, "Timecode")
        worksheet.write(0, 3, "Thumbnail")
        worksheet.set_column(0, 200, 50)
        #worksheet.set_default_row(30)
        video_file = input
        #cap = cv2.VideoCapture(video_file)
        sorted_dict = sorted(xytech_dict.items(), key=lambda x: x[0])
        #for i, each in enumerate(timecode):
             #timecode_xls = timecode
            #timecode_xls = ", ".join(timecode)
            #worksheet.write(i + 1, 2, timecode_xls)
       
        """
        row = 0
        for key, value in sorted_dict:
            location = key
            ranges = []

            for frame in value:
                if '-' in frame:
                    start, end = frame.strip('[]').split('-')
                    start_num = int(start)
                    end_num = int(end)
                    ranges.append(f"{start_num}-{end_num}")
                else:
                    frame_num = int(frame)
                    ranges.append(f"{frame_num}")

                worksheet.write(row, 0, location)
                for each in ranges:
                 #' '.join(ranges)
                 worksheet.write(row, 1,each)
                 row += 1
        workbook.close()
        """
        """row = 1
        for key, value in xytech_dict.items():
            location = key
            ranges = []

            for frame in value:
                if '-' in frame:
                    start, end = frame.strip('[]').split('-')
                    start_num = int(start)
                    end_num = int(end)
                    ranges.append((start_num, end_num))
                else:
                    frame_num = int(frame)
                    ranges.append((frame_num, frame_num))

            sorted_ranges = sorted(ranges, key=lambda x: x[0])
            sorted_ranges_formatted = [f"[{start}-{end}]" if start != end else f"[{start}]" for start, end in sorted_ranges]
            #frame_timecodes = [timecode[frame_num] for start, end in sorted_ranges for frame_num in range(start, end + 1)]

            worksheet.write(row, 0, location)
            for each in sorted_ranges_formatted:
                worksheet.write(row, 1, each)
                row += 1
            #worksheet.write(row, 2, ', '.join(frame_timecodes))

        ranges_dict = {}
        row = 1
        
        for key, value in testdict.items():
            location = key
            ranges = []

            # Sort the frames in ascending order
            sorted_frames = sorted(value)

            start_frame = sorted_frames[0]
            end_frame = sorted_frames[0]
            for frame in sorted_frames[1:]:
                if frame == end_frame + 1:
                    end_frame = frame
                else:
                    ranges.append((start_frame, end_frame))
                    start_frame = frame
                    end_frame = frame

            # Add the last range
            ranges.append((start_frame, end_frame))

            ranges_formatted = [f"[{start}-{end}]" if start != end else f"[{start}]" for start, end in ranges]
            ranges_dict[location] = ranges_formatted
        """

        # Print the updated dictionary
        #for location, ranges in ranges_dict.items():
        #for location, ranges in sorted(ranges_dict.items(), key=lambda x: (x[0], sorted(x[1]))):
        #for location, ranges in sorted(ranges_dict.items(), key=lambda x: (x[0], [int(val) for val in re.findall(r'\d+', ' '.join(x[1]))])):
        sorted_items = sorted(ranges_dict.items(), key=lambda x: (min(int(val[1:-1].split('-')[0]) for val in x[1])))

        for location, ranges in sorted_items:
            
            print(f"Key: {location}, Value: {ranges}") 
            #frame_timecodes = [timecode[frame] for start, end in ranges for frame in range(start, end + 1)]
            #print(f"Key: {location}, Value: {ranges}, Timecodes: {frame_timecodes}")
            worksheet.write(row, 0, location)
            for each in ranges:
                worksheet.set_row(row, 90)
                worksheet.write(row, 1 ,each)
                worksheet.write(row, 0, location)
                row += 1
        column = 1
        #timecode.sort()
        #print(timecode)
        #for eachtimecode in timecode:
        #    worksheet.write(column, 2 ,eachtimecode)
        #    column +=1
        print("ranges")
       
        finaltimecode= []
        storestart = []
        #middle_numbers = []

        #
        print("range_str")
        for location, ranges in sorted_items:
            for range_str in ranges:
                print(range_str)
                start, end = map(int, range_str.strip('[]').split('-'))
                middle_number = (start + end) // 2
                #middle_numbers.append(middle_number)
                storestart.append(middle_number)
                
                #print("middle#",middle_number)
                #print(start)
                #print(end)
                ##get index
                start_indices = [i for i, val in enumerate(testval) if val == start]
                end_indices = [i for i, val in enumerate(testval) if val == end]
                print(f"Range {range_str}: Start Indices = {start_indices}, End Indices = {end_indices}")
                for eachl in start_indices:
                    
                    #print(eachl)
                    for eachr in end_indices:
                        start_timecode = timecode[eachl]
                        end_timecode = timecode[eachr]
                        #print(start_timecode)
                        #print(end_timecode)
                        timecode_range = (f"{start_timecode}/{end_timecode}")
                        finaltimecode.append(timecode_range)
            
        
        match_number = [start_val for start_val in storestart if start in frame_list]
        print(storestart)
        #matchingpng_files = sorted([f for f in os.listdir(frame_directory) if any(f.endswith(f'{str(number).zfill(4)}.png') for number in match_number)], key=lambda x: match_number.index(int(x[-8:-4])))
        #matchingpng_files = sorted([f for f in os.listdir(frame_directory) if any(f.endswith(f'{str(number).zfill(4)}.png') for number in match_number)], key=lambda x: (match_number.index(int(x[-8:-4])), int(x[-8:-4])))
        matchingpng_files = []
        
        for every in match_number:
            matching_files = [f for f in os.listdir(frame_directory) if f.endswith(f'{str(every).zfill(4)}.png')]
            matchingpng_files.extend(matching_files)
        #for every in match_number:
        #    f = os.listdir(frame_directory)
        #    if all(f.endswith(f'{str(every).zfill(4)}.png')):
        #        matchingpng_files.append(f)

        print(len(match_number))
        print("# of png")
        print(len(matchingpng_files))
        

        #print(finaltimecode)
        for eachlr in finaltimecode:
            worksheet.write(column, 2 ,eachlr)
            column +=1

        ###images
        #frame_list.sort()
        #match_number.sort()
        matching_numbers = [x for x in testval if x in frame_list]
        print("matchnumber")
        print(match_number)
        #matchingpng_files = [f for f in os.listdir(frame_directory) if any(f.endswith(f'{str(number).zfill(4)}.png') for number in match_number)]
        #matchingpng_files = [f for f in os.listdir(frame_directory) if any(f.endswith(f'{str(number).zfill(4)}.png') for number in matching_numbers)]
               
        # //Users/alhelal/Desktop/467 Chaya/proj3/frames/frame0002.png
        #matchingpng_files.sort()
        print(matchingpng_files)
        thirdrow = 1
        #worksheet.set_column(thirdrow, 3, 20)
        #image_path = "/Users/alhelal/Desktop/467 Chaya/proj3/frames/" + matchingpng_files
        #for each in matchingpng_files:
            #image_path = "/Users/alhelal/Desktop/467 Chaya/proj3/frames/" + each
            #worksheet.write(thirdrow, 3, each)
        #    worksheet.set_column(3,3,18)
        #    worksheet.insert_image(thirdrow, 3, image_path, {'x_scale': 0.5, 'y_scale': 0.5})
        #     thirdrow +=1

        for image_file in matchingpng_files:
            image_path = "/Users/alhelal/Desktop/467 Chaya/proj3/frames/" + image_file
            worksheet.insert_image(thirdrow, 3, image_path,{'x_scale': 0.1, 'y_scale': 0.1,'width': 96, 'height': 74})
            thirdrow+=1

        
        workbook.close()
  
def get_fps(video_path):
    cmd = ['ffprobe', '-v', 'error', '-select_streams', 'v', '-of', 
           'default=noprint_wrappers=1:nokey=1', '-show_entries', 
           'stream=r_frame_rate', video_path]
    output = subprocess.check_output(cmd).decode('utf-8').strip()
    if '/' in output:  # Frame rate might be a ratio, so we compute it
        num, den = output.split('/')
        return float(num) / float(den)
    else:
        return float(output)

    #video_path = '/path/to/your/video.mp4'
    
def get_vid_length(input):
    video = input
    command = ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", video]
    x = float(subprocess.check_output(command))
    return x


def convert_frames_to_timecodes(frames, fps):
    timecodes = []
    for frame in frames:
        total_seconds = frame / fps
        hours = int(total_seconds // 3600)
        minutes = int((total_seconds % 3600) // 60)
        seconds = int(total_seconds % 60)
        deci_seconds = round((total_seconds - int(total_seconds)) * fps)
        timecodes.append(f"{hours:02d}:{minutes:02d}:{seconds:02d}:{deci_seconds:02d}")
    return timecodes


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='OpenCV video processing')
    parser.add_argument('-p', "--process", help='full path to input video that will be processed')
    parser.add_argument("--output", choices=["csv", "xls"])
    args = parser.parse_args()

    if args.process is None:
    # or args.output is None:
        sys.exit("Please provide path to input and output video files! See --help")

    main(args.process, args.output)