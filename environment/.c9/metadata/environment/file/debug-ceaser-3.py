{"filter":false,"title":"debug-ceaser-3.py","tooltip":"/file/debug-ceaser-3.py","undoManager":{"mark":6,"position":6,"stack":[[{"start":{"row":2,"column":3},"end":{"row":3,"column":0},"action":"remove","lines":["",""],"id":7},{"start":{"row":2,"column":2},"end":{"row":2,"column":3},"action":"remove","lines":["\""]},{"start":{"row":2,"column":1},"end":{"row":2,"column":2},"action":"remove","lines":["\""]},{"start":{"row":2,"column":0},"end":{"row":2,"column":1},"action":"remove","lines":["\""]},{"start":{"row":1,"column":23},"end":{"row":2,"column":0},"action":"remove","lines":["",""]},{"start":{"row":1,"column":22},"end":{"row":1,"column":23},"action":"remove","lines":["n"]},{"start":{"row":1,"column":21},"end":{"row":1,"column":22},"action":"remove","lines":["o"]},{"start":{"row":1,"column":20},"end":{"row":1,"column":21},"action":"remove","lines":["i"]},{"start":{"row":1,"column":19},"end":{"row":1,"column":20},"action":"remove","lines":["t"]},{"start":{"row":1,"column":18},"end":{"row":1,"column":19},"action":"remove","lines":["p"]},{"start":{"row":1,"column":17},"end":{"row":1,"column":18},"action":"remove","lines":["i"]},{"start":{"row":1,"column":16},"end":{"row":1,"column":17},"action":"remove","lines":["r"]},{"start":{"row":1,"column":15},"end":{"row":1,"column":16},"action":"remove","lines":["c"]},{"start":{"row":1,"column":14},"end":{"row":1,"column":15},"action":"remove","lines":["s"]},{"start":{"row":1,"column":13},"end":{"row":1,"column":14},"action":"remove","lines":["e"]},{"start":{"row":1,"column":12},"end":{"row":1,"column":13},"action":"remove","lines":["d"]},{"start":{"row":1,"column":11},"end":{"row":1,"column":12},"action":"remove","lines":[" "]},{"start":{"row":1,"column":10},"end":{"row":1,"column":11},"action":"remove","lines":["e"]},{"start":{"row":1,"column":9},"end":{"row":1,"column":10},"action":"remove","lines":["l"]},{"start":{"row":1,"column":8},"end":{"row":1,"column":9},"action":"remove","lines":["u"]},{"start":{"row":1,"column":7},"end":{"row":1,"column":8},"action":"remove","lines":["d"]},{"start":{"row":1,"column":6},"end":{"row":1,"column":7},"action":"remove","lines":["o"]},{"start":{"row":1,"column":5},"end":{"row":1,"column":6},"action":"remove","lines":["m"]},{"start":{"row":1,"column":4},"end":{"row":1,"column":5},"action":"remove","lines":[" "]},{"start":{"row":1,"column":3},"end":{"row":1,"column":4},"action":"remove","lines":["r"]},{"start":{"row":1,"column":2},"end":{"row":1,"column":3},"action":"remove","lines":["u"]},{"start":{"row":1,"column":1},"end":{"row":1,"column":2},"action":"remove","lines":["o"]},{"start":{"row":1,"column":0},"end":{"row":1,"column":1},"action":"remove","lines":["Y"]},{"start":{"row":0,"column":3},"end":{"row":1,"column":0},"action":"remove","lines":["",""]},{"start":{"row":0,"column":2},"end":{"row":0,"column":3},"action":"remove","lines":["\""]},{"start":{"row":0,"column":1},"end":{"row":0,"column":2},"action":"remove","lines":["\""]},{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"remove","lines":["\""]},{"start":{"row":0,"column":0},"end":{"row":56,"column":23},"action":"insert","lines":["","# Module Lab: Caesar Cipher Program Bug #3","#","# In a previous lab, you created a Caesar cipher program. This version of","# the program is buggy. Use a debugger to find the bug and fix it.","","# Double the given alphabet","def getDoubleAlphabet(alphabet):","    doubleAlphabet = alphabet + alphabet","    return doubleAlphabet","","# Get a message to encrypt","def getMessage():","    stringToEncrypt = input(\"Please enter a message to encrypt: \")","    return stringToEncrypt","","# Get a cipher key","def getCipherKey():","    shiftAmount = input(\"Please enter a key (whole number from 1-25): \")","    return shiftAmount","","# Encrypt message","def encryptMessage(message, cipherKey, alphabet):","    encryptedMessage = \"\"","    uppercaseMessage = \"\"","    uppercaseMessage = message.upper()","    for currentCharacter in uppercaseMessage:","        position = alphabet.find(currentCharacter)","        newPosition = position + int(cipherKey)","        if currentCharacter in alphabet:","            encryptedMessage = encryptedMessage + alphabet[newPosition]","        else:","            encryptedMessage = encryptedMessage + currentCharacter","    return encryptedMessage","","# Decrypt message","def decryptMessage(message, cipherKey, alphabet):","    decryptKey = -1 * int(cipherKey)","    return encryptMessage(message, cipherKey, alphabet)","","# Main program logic","def runCaesarCipherProgram():","    myAlphabet=\"ABCDEFGHIJKLMNOPQRSTUVWXYZ\"","    print(f'Alphabet: {myAlphabet}')","    myAlphabet2 = getDoubleAlphabet(myAlphabet)","    print(f'Alphabet2: {myAlphabet2}')","    myMessage = getMessage()","    print(myMessage)","    myCipherKey = getCipherKey()","    print(myCipherKey)","    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)","    print(f'Encrypted Message: {myEncryptedMessage}')","    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)","    print(f'Decrypted Message: {myDecryptedMessage}')","","# Main logic","runCaesarCipherProgram("]}],[{"start":{"row":56,"column":23},"end":{"row":56,"column":24},"action":"insert","lines":[")"],"id":8}],[{"start":{"row":55,"column":12},"end":{"row":55,"column":13},"action":"insert","lines":["S"],"id":9}],[{"start":{"row":38,"column":40},"end":{"row":38,"column":41},"action":"remove","lines":["r"],"id":10},{"start":{"row":38,"column":39},"end":{"row":38,"column":40},"action":"remove","lines":["e"]},{"start":{"row":38,"column":38},"end":{"row":38,"column":39},"action":"remove","lines":["h"]},{"start":{"row":38,"column":37},"end":{"row":38,"column":38},"action":"remove","lines":["p"]},{"start":{"row":38,"column":36},"end":{"row":38,"column":37},"action":"remove","lines":["i"]},{"start":{"row":38,"column":35},"end":{"row":38,"column":36},"action":"remove","lines":["c"]}],[{"start":{"row":38,"column":35},"end":{"row":38,"column":36},"action":"insert","lines":["d"],"id":11},{"start":{"row":38,"column":36},"end":{"row":38,"column":37},"action":"insert","lines":["e"]},{"start":{"row":38,"column":37},"end":{"row":38,"column":38},"action":"insert","lines":["c"]},{"start":{"row":38,"column":38},"end":{"row":38,"column":39},"action":"insert","lines":["r"]}],[{"start":{"row":38,"column":39},"end":{"row":38,"column":40},"action":"insert","lines":["y"],"id":12},{"start":{"row":38,"column":40},"end":{"row":38,"column":41},"action":"insert","lines":["p"]},{"start":{"row":38,"column":41},"end":{"row":38,"column":42},"action":"insert","lines":["t"]}],[{"start":{"row":38,"column":35},"end":{"row":38,"column":45},"action":"remove","lines":["decryptKey"],"id":13},{"start":{"row":38,"column":35},"end":{"row":38,"column":45},"action":"insert","lines":["decryptKey"]}]]},"ace":{"folds":[],"scrolltop":354.7170104980469,"scrollleft":0,"selection":{"start":{"row":46,"column":28},"end":{"row":46,"column":28},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":24,"state":"start","mode":"ace/mode/python"}},"timestamp":1729696766299,"hash":"327b9393581f448eacc45774e3f959083b98c3e3"}