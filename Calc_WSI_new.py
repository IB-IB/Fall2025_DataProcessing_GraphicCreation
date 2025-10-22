# Jennifer Roath
# September 2011
# Calculating WSI 

import os
import sys
from string import atoi
from string import *
#from stats import *

# Usage: python format_WSI.py <huctable> <runoff> <withdrawals> <output file name>
# <huctable> has two columns, the current HUC and the downstream HUC
# <runoff> has two columns, hucid and total runoff in m3/year
# <withdrawals> has two columns, hucid and annual withdrawals in m3/year


def orderArray(HUC_array):
    temp_HUC_sort = []
    # create new array with HUCs sorted by order 

    ordert = []
    lidx = len(HUC_array)-1
    
    #assume highest rank is length of array
    while lidx >= 0:
        ordert.append(lidx)
        lidx=lidx-1
   

  #  zer = 0
  #  ordert.append(zer)
  #  print ordert

  #  print len(ordert)        
    for j in range(len(ordert)):
        hidx = 0
        while hidx < len(HUC_array):
            if HUC_array[hidx][4] == ordert[j]:
                temp_HUC_sort.append(HUC_array[hidx])
            hidx=hidx+1

    return temp_HUC_sort

def findUP(HUC_array, hidx):
    DStemp = HUC_array[hidx][0]
    DSrank = HUC_array[hidx][4]
    # Current HUC in the flow path
    # Logic is moving UP stream

    fidx = 0
    while fidx < len(HUC_array):
            
        if DStemp == HUC_array[fidx][1]:
            # Search to find when DStemp appears in the 'Flows to' column
            UPrank = HUC_array[fidx][4]

            if UPrank > DSrank:
                # The UP HUC already has a higher order, do not change
                fidx=fidx+1  

            if UPrank <= DSrank:
                # The UP HUC has the same or lower order, make it greater than the current HUC
                HUC_array[fidx][4] = DSrank + 1
         
                if DSrank > 500:
                    return 
                findUP(HUC_array, fidx)
        else:
            fidx=fidx+1
            # Keep looping through to find the next UP HUC


def rankArray(HUC_array):
    hidx=0
    # Counter for the current HUC loop
    while hidx < len(HUC_array):
       # print hidx, HUC_array[hidx][0]
        findUP(HUC_array, hidx)
        hidx=hidx+1       
        # Once no more UP HUCs found, start new search with next HUC

def openfile(filename):
    """opens a file in the read mode, reads all lines and closes the file
    and returns the array of all lines"""
    fin = open(filename , "r")
    lines = fin.readlines()
    fin.close()
    return lines

def makearray(listname):
    sidx = 0
    outarray = []
    while sidx < len(listname):
        """takes desired data columns strips out the spaces
        and puts into new array"""
        listname[sidx] = listname[sidx].strip().split('\t')
        row = []
        j = 0 #counter for the position along row
        while j < len(listname[sidx]):
            r = listname[sidx][j]
            row.append(r)
            j = j+1
        outarray.append(row)
        sidx = sidx +1
    return outarray

def removeRepeat(array):
    sidx = 1
    outarray = []
    while sidx < len(array):
        if array[sidx-1][0] != array[sidx][0]:
            r = array[sidx-1]
            outarray.append(r)
        sidx=sidx+1
    last = len(array)-1
    beforelast = len(array)-2
    if array[beforelast][0] != array[last][0]:
        r = array[last]
        outarray.append(r)
    outlast = len(outarray)-1
    #print outarray[outlast]
    return outarray

### Start of main program

if(len(sys.argv) != 5):
    print "huc12 table, total runoff, withdrawals, outputfile"
    sys.exit()

# INPUTS
#HUC10 = 0
#HUC10_DS = 1
#Tot Cunsumptiveuse [m3]= 2
#Streamflow [m3] = 3

# OUTPUTS (initialized as zero in txt)
#Rank = 4
#Leaving = 5
#Supply = 6
#Demand = 7
#WSI = 8

print "opening huc10 table"
HUC_in = openfile(sys.argv[1])
h12 = makearray(HUC_in)

print "opening total runoff"
HUC_in = openfile(sys.argv[2])
tr = makearray(HUC_in)
print len(tr)

print "opening total withdrawal file"
HUC_in = openfile(sys.argv[3])
tw = makearray(HUC_in)

print "start out table"
huc_array = []
hidx = 0
twcnt = 0
trcnt = 0
cnt = 0

while hidx < len(h12):
    huc_check = h12[hidx][0]
    if h12[hidx][1].isdigit():
        huc_ds = int(h12[hidx][1])
    else:
        replace = 999999
        huc_ds = int(replace)

            
    # Withdrawals
    tw_out = -99
    if huc_check == tw[hidx][0]:
        tw_out = float(tw[hidx][1])

    if tw_out == -99:
        twcnt=twcnt+1

    #runoff
    tr_out = -99
    if huc_check == tr[hidx][0]:
        tr_out = float(tr[hidx][1])
    
    if tr_out == -99:
        trcnt=trcnt+1      

    #fill in array
    if tw_out != -99 and tr_out != -99:
        zer = 0
        row = []
        row.append(int(huc_check))
        row.append(huc_ds)
        row.append(tw_out) #m^3
        row.append(tr_out) #m^3
        row.append(int(zer))
        row.append(zer)
        row.append(zer)
        row.append(zer)
        row.append(zer)
        huc_array.append(row)
        #print row
        cnt=cnt+1

    hidx = hidx+1
    
print "Total HUC10: " + str(cnt)
 
huc_array = removeRepeat(huc_array)
print "There are "+str(twcnt)+" TW errors, "+str(trcnt)+" TR errors"


#Part 1: Rank HUCs

print "Assigning Rank to HUCs"

rankArray(huc_array)

# if rank>100, then it was an error loop. make it last to calculate
hidx = 0
zer = 0
cnt=0
while hidx < len(huc_array):
        if huc_array[hidx][4] > 500:
            huc_array[hidx][4] = int(zer)
            print "Closed Loop Error in HUC " + str(huc_array[hidx][0])
            cnt=cnt+1
        hidx=hidx+1


print "Total Closed Loop Errors " + str(cnt)


print "Finished Ranking HUCs"

# Part 2 - Sort Array based on Rank

print "Sorting Array based on Rank"


HUC_sort = orderArray(huc_array)
print "After sort: " +str(len(HUC_sort))
print "Before sort: " + str(len(huc_array))

print "Finished Sorting Array"

##print "Fixing for Closed Loop Errors"
##
##def closedLoops(HUC_array, hidx):
##    DStemp = HUC_array[hidx][1]
##    DSrank = HUC_array[hidx][4]
##    # Current HUC in the flow path
##    # Logic is moving UP stream
##
##    fidx = 0
##    while fidx < len(HUC_array):
##            
##        if DStemp == HUC_array[fidx][0]:
##            # Search to find when DStemp appears in the 'Flows to' column
##            UPrank = HUC_array[fidx][5]
##
##            if UPrank < 100:
##                # The UP HUC is before the closed loop started
##                DSrank = UPrank - 1
##                HUC_array[hidx][5] = DSrank
##                fidx = len(HUC_array)
##
##            if UPrank > 100:
##                # The UP HUC is still in the Loop, check next UP HUC
##                closedLoops(HUC_array, fidx)
##                
##        else:
##            fidx=fidx+1
##            # Keep looping through to find the next UP HUC




print "Finished Sorting Array"


# Part 3 - WSI Calculations

print "Calculating WSI"

hidx=0
while hidx < len(HUC_sort):
    # convert to float
    totw = HUC_sort[hidx][2]
    HUC_sort[hidx][2] = float(totw)
    stream = HUC_sort[hidx][3]
    HUC_sort[hidx][3] = float(stream)
    leave = HUC_sort[hidx][5]
    HUC_sort[hidx][5] = float(leave)
    hidx=hidx+1

widx = 0
cnt=0
while widx < len(HUC_sort):

    supply = HUC_sort[widx][3] #streamflow

    sidx=0
    while sidx < len(HUC_sort):              
        if HUC_sort[widx][0] == HUC_sort[sidx][1]:
            supply = supply + HUC_sort[sidx][5]
            # add the upstream runoff
        sidx=sidx+1

    demand = HUC_sort[widx][2]

    if supply == 0:
#        print "Zero Supply in HUC ", HUC_sort[widx][0]
        cnt=cnt+1
    else:
        wsi = demand/supply
        HUC_sort[widx][8] = wsi
        HUC_sort[widx][6] = supply
        HUC_sort[widx][7] = demand

        leaving = supply 
        if leaving < 0:
            HUC_sort[widx][5] = 0
        else:
            HUC_sort[widx][5] = leaving

    widx=widx+1

#print HUC_sort[0:20]
print "Total Supply Zero Errors: " +str(cnt)
print "Finished Calculating WSI"

# Part 5 - Write Output File

print "Writing text file"
    
outFile = sys.argv[4]
fout = open(outFile,"w") 

fout.write('HUC10\tHUC10_DS\tTotWD_m3\tStream_m3\tRank\tLeaving\tSupply\tDemand\tWSI\n')
for i in range(len(HUC_sort)):
    for r in range(len(HUC_sort[i])):
        fout.write(str(HUC_sort[i][r]))
        fout.write("\t")
    fout.write("\n")
fout.close()

print "Finished writing text file"
