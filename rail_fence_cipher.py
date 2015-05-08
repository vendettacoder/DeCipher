# -*- coding: utf-8 -*-
"""
Created on Fri May  1 13:37:51 2015

@author: Rohan Kulkarni

"""

""" (Intermediate): Rail Fence Cipher Before the days of computerised
encryption, cryptography was done manually by hand. This means the methods of
encryption were usually much simpler as they had to be done reliably by a
person, possibly in wartime scenarios. One such method was the rail-fence
cipher[1] . This involved choosing a number (we'll choose 3) and writing our
message as a zig-zag with that height (in this case, 3 lines high.) Let's say
our message is REDDITCOMRDAILYPROGRAMMER. We would write our message like this:

R   I   M   I   R   A   R
 E D T O R A L P O R M E
  D   C   D   Y   G   M

See how it goes up and down? Now, to get the ciphertext, instead of reading with
the zigzag, just read along the lines instead. The top line has RIMIRAR, the
second line has EDTORALPORME and the last line has DCDYGM. Putting those
together gives you RIMIRAREDTORALPORMEDCDYGM, which is the ciphertext. You can
also decrypt (it would be pretty useless if you couldn't!). This involves
putting the zig-zag shape in beforehand and filling it in along the lines. So,
start with the zig-zag shape:

?   ?   ?   ?   ?   ?   ?
 ? ? ? ? ? ? ? ? ? ? ? ?
  ?   ?   ?   ?   ?   ?

The first line has 7 spaces, so take the first 7 characters (RIMIRAR)
and fill them in.

R   I   M   I   R   A   R
 ? ? ? ? ? ? ? ? ? ? ? ?
  ?   ?   ?   ?   ?   ?

The next line has 12 spaces, so take 12 more characters (EDTORALPORME)
and fill them in.

R   I   M   I   R   A   R
 E D T O R A L P O R M E
  ?   ?   ?   ?   ?   ?

Lastly the final line has 6 spaces so take the remaining 6 characters
(DCDYGM) and fill them in.

R   I   M   I   R   A   R
 E D T O R A L P O R M E
  D   C   D   Y   G   M
  
Then, read along the fence-line (zig-zag) and you're done!
Input Description
You will accept lines in the format:

enc # PLAINTEXT
or
dec # CIPHERTEXT

where enc # encodes PLAINTEXT with a rail-fence cipher using # lines,
and dec # decodes CIPHERTEXT using # lines.

For example:
enc 3 REDDITCOMRDAILYPROGRAMMER
Output Description

Encrypt or decrypt depending on the command given. So the example above gives:
RIMIRAREDTORALPORMEDCDYGM
Sample Inputs and Outputs
enc 2 LOLOLOLOLOLOLOLOLO
Result: LLLLLLLLLOOOOOOOOO

enc 4 THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG
Result: TCNMRZHIKWFUPETAYEUBOOJSVHLDGQRXOEO

dec 4 TCNMRZHIKWFUPETAYEUBOOJSVHLDGQRXOEO
Result: THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG

dec 7 3934546187438171450245968893099481332327954266552620198731963475632908289907
Result: 3141592653589793238462643383279502884197169399375105820974944592307816406286 (pi)
"""

from Tkinter import *
import itertools


def encryptor():
        n=int(v2.get())
        string=v1.get()
        layers=[]
        init_even=(2*n)-3
        init_odd=0
        for i in range(n):
            if i == n-1 or i == 0:
                init_even=(2*n)-3
            arr=[]
            count=0
            z=i
            while z<len(string):
                arr.append(string[z])
                if count%2==0:
                    z+=init_even+1
                elif(count%2 != 0 and i!=0 and i != n-1):
                    z+=init_odd+1
                elif(count%2 != 0 and (i!=0 or i != n-1)):
                    z+=init_even+1
                count+=1
            layers.append(arr)
            init_even-=2
            init_odd+=i+1
        layers=''.join(list(itertools.chain(*layers)))
        v3.set(layers)

def decryptor():
        n=int(v2.get())
        string=v1.get()
        print('string len',len(string))
        output=list('#'*len(string))
        layer=0
        init_even=(2*n)-3
        init_odd=1
        output[0]=string[0]
        pos=1
        while layer<n:
            z=layer
            if(layer>0):
                output[z]=string[pos]
            count=0
            while z < len(output):
                flag=0
                if layer==0:
                    if z<(len(output)):
                        flag=1
                        z+=(2*n)-2
                        if z<(len(output)):
                            output[z]=string[pos]
                            pos+=1
                elif layer==n-1:
                    if z<(len(output)):
                        flag=1
                        z+=(2*n)-2
                        if z<(len(output)):
                            pos+=1
                            output[z]=string[pos]
                elif layer!=0 and layer!=n-1 and count%2==0:
                    z+=init_even+1
                    if z<(len(output)):
                        flag=1
                        pos+=1
                        output[z]=string[pos]
                elif layer!=0 and layer!=n-1 and count%2!=0:
                    z+=init_odd+1
                    if z<(len(output)):
                        flag=1
                        pos+=1
                        output[z]=string[pos]
                if flag==0:
                    pos+=1
                count+=1
            init_even-=2
            if(layer!=0):
                init_odd+=2
            layer+=1
        output=''.join(output)
        v3.set(output)

def main():
    global v1,v2,v3
    window=Tk()
    window.geometry("325x280+300+300")
    l1=Label(window,text="Input String",padx=10)
    l2=Label(window,text="Number of Levels",padx=10)
    l3=Label(window,text="Output String",padx=10)
    v1=StringVar()
    v2=StringVar()
    v3=StringVar()
    e1=Entry(window,bd=5,textvariable=v1)
    e2=Entry(window,bd=5,textvariable=v2)
    e3=Entry(window,bd=5,textvariable=v3)
    b1=Button(window,text='Perform Encryption')
    b2=Button(window,text='Perform Decryption')
    l1.grid(row=0,column=0)
    e1.grid(row=0,column=1)
    l2.grid(row=1,column=0)
    e2.grid(row=1,column=1)
    b1.grid(row=2,column=0)
    b2.grid(row=2,column=1)
    l3.grid(row=3,column=0)
    e3.grid(row=3,column=1)
    b1.configure(command=encryptor)
    b2.configure(command=decryptor)
    window.mainloop()

if __name__=='__main__':
    main()
