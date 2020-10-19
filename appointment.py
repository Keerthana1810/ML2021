import datetime
def appointment_fil(choice):
    print("name of the doctor")
    name=input()
    current_time = datetime.datetime.now()
    k=current_time.hour
    if(name=="tarun" or "lakshmi" or "keerthna" or "haripriya" or "pavan" or "prasana" or "kushel kumar" or "laksmi " or "patel"):
        if k>9 and k<12:
            print("Available")
        elif k>14 and k<22:
                print("Available")
        else:
            print("Sorry the doctor is not available")
    else:
        print("once check ypur data")
    return