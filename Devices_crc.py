from binascii import unhexlify
from crcmod import mkCrcFun
class CRC16_xmodem:
    # CRC16/XMODEM
    def crc16_xmodem(s) :
        crc16 = mkCrcFun(0x11021 , rev=False , initCrc=0x0000 , xorOut=0x0000)
        return get_crc_value(s , crc16)

    # common func
    def get_crc_value(s , crc16) :
        data = s.replace(' ' , '')
        crc_out = hex(crc16(unhexlify(data))).upper()
        str_list = list(crc_out)
        if len(str_list) == 5 :
            str_list.insert(2 , '0')  # 位数不足补0
        crc_data = ''.join(str_list[2 :])
        return crc_data[:2] + ' ' + crc_data[2 :]



