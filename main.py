import sys
import json
import struct
import traceback
import subprocess

try:
    # Python 3.x version
    # Read a message from stdin and decode it.
    def getMessage():
        rawLength = sys.stdin.buffer.read(4)
        if len(rawLength) == 0:
           sys.exit(0)
        messageLength = struct.unpack('@I', rawLength)[0]
        message = sys.stdin.buffer.read(messageLength).decode('utf-8')
        return json.loads(message)

    # Encode a message for transmission,
    # given its content.
    def encodeMessage(messageContent):
        encodedContent = json.dumps(messageContent, separators=(',', ':')).encode('utf-8')
        encodedLength = struct.pack('@I', len(encodedContent))
        return {'length': encodedLength, 'content': encodedContent}

    # Send an encoded message to stdout
    def sendMessage(encodedMessage):
        sys.stdout.buffer.write(encodedMessage['length'])
        sys.stdout.buffer.write(encodedMessage['content'])
        sys.stdout.buffer.flush()
        
    while True:
        receivedMessage = getMessage()

        if receivedMessage['delete'] == True:
            for obj in receivedMessage['objects']:
                subprocess.run(f'mkdir "{obj["fileFolder"]}"', shell=True)
                subprocess.run(f'tar -xf "{obj["filePath"]}" -C "{obj["fileFolder"]}"', shell=True)
                subprocess.run(f'del "{obj["filePath"]}" -force', shell=True)
                
        else:
            for obj in receivedMessage['objects']:
                subprocess.run(f'mkdir "{obj["fileFolder"]}"', shell=True)
                subprocess.run(f'tar -xf "{obj["filePath"]}" -C "{obj["fileFolder"]}"', shell=True)

        sendMessage(encodeMessage("Ok"))

except Exception as e:
    sys.stdout.buffer.flush()
    sys.stdin.buffer.flush()
    # https://discuss.python.org/t/how-to-read-1mb-of-input-from-stdin/22534/14
    with open('nm_python.log', 'w', encoding='utf-8') as f:
        traceback.print_exc(file=f)
    sys.exit(0)