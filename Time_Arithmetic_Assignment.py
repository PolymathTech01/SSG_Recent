class TimeConversion:             
    def convert_DayInput_To_Seconds(self):
        return int(Time_to_convert) * 86400
    def convert_HourInput_To_Seconds(self):
        return int(Time_to_convert) * 3600
    def convert_MinuteInput_To_Seconds(self):
        return int(Time_to_convert) * 60
    def convert_ADayInput_To_Seconds(self):
        return int(TimeA_to_Convert) * 86400
    def convert_AHourInput_To_Seconds(self):
        return int(TimeA_to_Convert) * 3600
    def convert_AMinuteInput_To_Seconds(self):
        return int(TimeA_to_Convert) * 60
    def convert_BDayInput_To_Seconds(self):
        return int(TimeB_to_Convert) * 86400
    def convert_BHourInput_To_Seconds(self):
        return int(TimeB_to_Convert) * 3600
    def convert_BMinuteInput_To_Seconds(self):
        return int(TimeB_to_Convert) * 60
    
           
while True:
           arithmetic = int(input('Do you want to make \n 1. Time Calculations \n 2.Time Conversion \n'))
           if arithmetic == 1:
                while True:
                    input_Operation = int(input(
                        'Specify the Operation you want to carry out\n 1. Addition\n 2. Subtraction\n'
                    ))
                    while True:
                        InputA_Time_Format = int(input(
                        'Specify your Input Time A Format\n 1. Day\n 2. Hours\n 3. Minutes\n 4. Seconds\n Enter No. Corresponding with Format:'
                        ))
                        if InputA_Time_Format >0 and InputA_Time_Format <5:
                            True
                            TimeA_to_Convert = int(input('Enter The Time A: '))
                            break
                        else:
                            (
                            print("Invalid input, Enter a corresponding Number with desired Format")
                            )
                    while True:
                        InputB_Time_Format = int(input(
                        'Specify your Input Time B Format\n 1. Day\n 2. Hours\n 3. Minutes\n 4. Seconds\n Enter No. Corresponding with Format:'
                        ))
                        if InputB_Time_Format >0 and InputB_Time_Format <5:
                            True
                            TimeB_to_Convert = int(input('Enter the Time B: '))
                            break
                        else:
                            (
                            print("Invalid input, Enter a corresponding Number with desired Format")
                            )
                    while True:
                        Output_Time_Format = int(input(
                        'Specify your Output Time Format\n 1. Day\n 2. Hours\n 3. Minutes\n 4. Seconds\n Enter No. Corresponding with Format:'
                        ))
                        if Output_Time_Format >0 and Output_Time_Format <5:
                            True
                            break
                        else:
                            (
                            print("Invalid input, Enter a corresponding Number with desired Format")
                            )
                    True
                    break
                True
                break

           elif arithmetic == 2:
                while True:
                    Input_Time_Format = int(input(
                     'Specify your Input Time Format\n 1. Day\n 2. Hours\n 3. Minutes\n 4. Seconds\n Enter No. Corresponding with Format:'
                    ))
                    if Input_Time_Format >0 and Input_Time_Format <5:
                        True
                        Time_to_convert = int(input('Enter The Time you want to convert: '))
                        break
                    else:
                       (
                       print("Invalid input, Enter a corresponding Number with desired Format")
                       )
                while True:
                    Output_Time_Format = int(input(
                     'Specify your Output Time Format\n1. Day\n 2. Hours\n 3. Minutes\n 4. Seconds\n Enter No. Corresponding with Format:'
                    ))
                    if Output_Time_Format >0 and Output_Time_Format <5:
                       True
                       break
                    else:
                       (
                       print("Invalid input, Enter a corresponding Number with desired Format")
                       )
                True
                break
           else:
                print('Please Select Between 1 and 2')
                
converter = TimeConversion()
inputAInSeconds = None
inputBInSeconds = None
inputsInSeconds = None
while arithmetic == 1:
    if InputA_Time_Format == 1:
        inputAInSeconds = converter.convert_ADayInput_To_Seconds()
    elif InputA_Time_Format == 2:
        inputAInSeconds = converter.convert_AHourInput_To_Seconds()
    elif InputA_Time_Format == 3:
        inputAInSeconds = converter.convert_AMinuteInput_To_Seconds()
    else:
        inputAInSeconds = Time_to_convert
        
    if InputB_Time_Format == 1:
        inputBInSeconds = converter.convert_BDayInput_To_Seconds()
    elif InputB_Time_Format == 2:
        inputBInSeconds = converter.convert_BHourInput_To_Seconds()
    elif InputB_Time_Format == 3:
        inputBInSeconds = converter.convert_BMinuteInput_To_Seconds()
    else:
        inputBInSeconds = TimeB_to_Convert
    
    if input_Operation == 1:
        inputsInSeconds = inputAInSeconds + inputBInSeconds
    else:
        inputsInSeconds = inputAInSeconds - inputBInSeconds
    
    if Output_Time_Format == 1:
        dayResult = inputsInSeconds / 86400
        print("Approximately " + str(round(dayResult)) + " days")
        break
    elif Output_Time_Format == 2:
        hourResult = inputsInSeconds / 3600
        print("Approximately " + str(round(hourResult)) + " hours")
        break
    elif Output_Time_Format == 3:
        minutesResult = inputsInSeconds / 60
        print("Approximately " + str(round(minutesResult)) + " minutes")
        break
    else:
        secondsResult = inputsInSeconds
        print("Approximately " + str(round(secondsResult)) + " seconds")
        break
        
    
        
while arithmetic == 2:
    if Input_Time_Format == 1:
        inputsInSeconds = converter.convert_DayInput_To_Seconds()
    elif Input_Time_Format == 2:
        inputsInSeconds = converter.convert_HourInput_To_Seconds()
    elif Input_Time_Format == 3:
        inputsInSeconds = converter.convert_MinuteInput_To_Seconds()
    else:
        inputsInSeconds = Time_to_convert
        
    if Output_Time_Format == 1:
        dayResult = inputsInSeconds / 86400
        print("Approximately " + str(round(dayResult)) + " days")
        break
    elif Output_Time_Format == 2:
        hourResult = inputsInSeconds / 3600
        print("Approximately " + str(round(hourResult)) + " hours")
        break
    elif Output_Time_Format == 3:
        minutesResult = inputsInSeconds / 60
        print("Approximately " + str(round(minutesResult)) + " minutes")
        break
    else:
        secondsResult = inputsInSeconds
        print("Approximately " + str(round(secondsResult)) + " seconds")
        break
        
    