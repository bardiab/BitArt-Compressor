# BitArt Compressor/Decompressor
# By: Bardia Barahman

import re
import os


class Compression:
    """
    This class contains the functions to encode/decode the bitmap images
    """

    def encode_img(self, fileName):
        """
        Function to encode the .txt file. Reads image from fileName and
        compresses it into an encoded.txt file
        """
        f = open(fileName, 'r')
        lst = []
        for x in f:
            numSpaces = x.count(' ')
            newStr = self.compress_string(x)
            lst.append((numSpaces, newStr))

        #write encoding bitmap into a new fileName
        f = open("encoded.txt", "w+")
        for i in range(len(lst)):
                f.write(str(lst[i]))
        f.close()


    def compress_string(self, string):
        """
        Helper function to eliminate consecutive repeated characters,
        consecutive repeated spaces, and newline characters from a string
        """
        compressed = ''
        numSpaces = string.count(' ')
        #Adding the first nonspace character
        compressed += string[numSpaces]
        count = 1

        #Iterating through loop, skipping last char
        for i in range(numSpaces, len(string)-1):
            if (string[i] == string[i+1]):
                count += 1
            else:
                if (count > 1):
                    compressed += str(count)
                compressed += string[i+1]
                count = 1

        if(count>1):
            compressed += str(count)

        #convert to list to delete newline character at end
        lst = list(compressed)
        if (lst[-1] == '\n'):
            del lst[-1]
        str1 = "".join(lst)
        return str1


    def decode_img(self, fileName):
        """
        Function to decode the .txt file
        """
        e = open(fileName, 'r')
        data = e.readline()
        lst = self.get_tuples(data)

        d = open('decoded.txt', "w+")

        for x in lst:
            #Writing the # of blank spaces into file
            spaces = int(x[0]) *str(' ')
            d.write(spaces)

            #Writing the deocoded string followed by newline back into file
            decode = self.decompress_string(x[1])
            d.write(decode.strip('\'\"'))
            d.write('\n')


    def decompress_string(self, string):
        """
        Helper function to recreate original string from compressed version
        """
        decompressed = ''
        for i in range(len(string)):
            #accounting for two repeated digits
            if (self.is_number(string[i-1])):
                if (not self.is_number(string[i])):
                    decompressed += string[i]
                else:
                    continue
            else:
                if (self.is_number(string[i])):
                    #check if its a two digit number
                    repeated = self.get_repeated(string[i:])
                    #subtracting one to account for number that was already counted
                    decompressed += string[i-1]* (int(repeated) - 1)
                else:
                    decompressed += string[i]
        return decompressed


    def is_number(self, string):
        """
        Check if a string is a number.
        """
        try:
            int(string)
            return True
        except ValueError:
            return False


    def get_repeated(self, string):
        """
        Takes a string and returns the first occurence of how many times
        a character is repeated, returned as a string
        """
        regex = "[0-9]+"
        output = re.search(regex, string)
        return output.group()


    def get_tuples(self, string):
        """
        Takes a string from an encoded file and returns a list of tuples
        """
        regex = "\((\d*),\s([^\)]*)\)?"
        output = re.findall(regex, string)
        return list(output)


#Main Function
if __name__ == '__main__':
    obj = Compression()
    while True:
        data = input("Would you like to encode or decode your image? (e/d)\n")
        if data not in ('e', 'E', 'd', 'D'):
            print("\nSorry, please enter a valid option.")
            print("------------\n")
            continue
        else:
            break
    bitImg = 'data.txt'

    if data in ('e', 'E'):
        try:
            orig_size = int(os.stat(bitImg).st_size)
            obj.encode_img(bitImg)
            new_size = int(os.stat('encoded.txt').st_size)
            reduced = ((orig_size-new_size)/orig_size)*100

            print("\nSuccess! Encoded image located in 'encoded.txt'.")
            print("Reduced file size by "+str(round(reduced, 2))+"%")
        except:
            print("\nUnable to encode image. Please make sure there exists a valid 'data.txt' file.")

    if data in ('d', 'D'):
        try:
            obj.decode_img('encoded.txt')
            print("\nSuccessfully decoded image. Located under 'decoded.txt' in this directory.")
        except:
            print("\nError, unable to decode image.")
