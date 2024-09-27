import json

class BaseMessage:
    def __init__(self, Method):
        self.Method = Method


def encode_message(msg):
    content = json.dumps(msg) 
    return f'Content-Length {len(content)}\r\n\r\n{content}'

def decode_message(msg):

    #TODO: Improve this function pls
    msg_decoded = msg.decode(encoding="utf-8")
    r_position = msg_decoded.find("\r")
    content_raw = msg_decoded[:r_position]

    content_index = msg_decoded.rfind(content_raw)
    end_content_index = content_index + len("Content Length ")
    contentLength = msg_decoded[end_content_index:r_position]

    content = msg_decoded[msg_decoded.find("{"):]
    content_method = json.loads(content)
    message = BaseMessage(content_method['method'])


    return message.Method, int(contentLength)
