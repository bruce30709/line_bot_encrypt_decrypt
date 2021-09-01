class Base64():

    def __init__(self):

        ## We only need to do this once
        self.b64 = ["v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
         "K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","!","\"",
         "#","$","%","&",chr(0x27),"(",")","*","+",",","-",".","/",":",";","<","=",
         ">","?","@","[","\\","]","^","_","`","{","|","}","~","o"]

    def Encode(self, data):
        alphabet = self.b64
        bit_str = ""
        base64_str = ""

        for char in data:
            bin_char = bin(char).lstrip("0b")
            bin_char = bin_char.zfill(8)
            bit_str += bin_char

        brackets = [bit_str[x:x+6] for x in range(0,len(bit_str),6)]

        for bracket in brackets:
            if(len(bracket) < 6):
                bracket = bracket + (6-len(bracket))*"0"
            base64_str += alphabet[int(bracket,2)]

        ##Add padding characters to maintain compatibility with forced padding
        padding_indicator = len(base64_str) % 4
        if padding_indicator == 3:
            base64_str += "="
        elif  padding_indicator == 2:
            base64_str += "=="

        return base64_str

    def Decode(self, text, eof):
        alphabet = self.b64
        bit_str = ""
        text_str = ""

        for char in text:
            if char in alphabet:
                bin_char = bin(alphabet.index(char)).lstrip("0b")
                bin_char = bin_char.zfill(6)
                bit_str += bin_char

        brackets = [bit_str[x:x+8] for x in range(0,len(bit_str),8)]

        for bracket in brackets:
            ## When eof ignore last value in brackets to remove \x00
            if eof and brackets[len(brackets) -1] == bracket:
                pass
            else:
                text_str += chr(int(bracket,2))

        ## encode string as Latin-1 == ISO-8859-1
        return text_str.encode("ISO-8859-1")


 
a = Base64() 
x=input()
b=a.Decode('M&=wM].]VyA?GR&[GRA%I]Q#HOA_GRz/T%M?H?T@UR_%HBL?GRA.U?w>HSM*WS@'," ").decode()
print(b)
c=a.Encode(str.encode(x))
print(c)