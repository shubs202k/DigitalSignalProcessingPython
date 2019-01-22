import mysignals as sigs
from matplotlib import pyplot as plt
from matplotlib import style
#we can export the result we got to an external csv file
import csv

csvfile = "conv_output_signal.txt"

def convolution(sig_src_arr,imp_response_arr,sig_dest_arr):
    for x in range(len(sig_src_arr)+len(imp_response_arr)):
        sig_dest_arr[x] =0
        #initialize everything in tht output array to 0
    for x in range(len(sig_src_arr)):
        for y in range(len(imp_response_arr)):
            sig_dest_arr[x+y] = sig_dest_arr[x+y] + sig_src_arr[x]*imp_response_arr[y] 
#to write output to a csv file
    with open(csvfile,"w") as output:
        writer = csv.writer(output,lineterminator = ',')
        for x in sig_dest_arr:
            writer.writerow([x])
    
    style.use('ggplot')
    style.use('dark_background')
    
    f,plt_arr=plt.subplots(3,sharex=True)
    f.suptitle=("Convolution")

    plt_arr[0].plot(sig_src_arr)
    plt_arr[0].set_title("Input Signal")
    
    plt_arr[1].plot(imp_response_arr,color ="brown")
    plt_arr[1].set_title("Impulse Response",color ="brown")

    plt_arr[2].plot(sig_dest_arr,color="green")
    plt_arr[2].set_title("Output Signal",color ="green")
    
    plt.show()
    
#Initialize a list
output_signal=[None]*349
convolution(sigs.InputSignal_1kHz_15kHz,sigs.Impulse_response,output_signal)
