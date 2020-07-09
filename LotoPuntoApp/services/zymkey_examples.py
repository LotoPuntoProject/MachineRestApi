from __future__ import print_function

import zymkey

from zymkey.exceptions import VerificationError

secret_message = 'Hello, Bob.  --Alice'

print('Signing data...', end='')
signature = zymkey.client.sign(secret_message)

print('OK')

print('Verifying data...', end='')
zymkey.client.verify(secret_message, signature)
print('OK')

print('Verifying tainted data...', end='')
try:
    zymkey.client.verify(secret_message.replace('Alice', 'Eve'), signature)
except VerificationError:
    print('FAIL, yay!')
else:
    raise Exception('verification should have failed, but passed')

# Flash the LED to indicate the operation is underway
zymkey.client.led_flash(500, 100)

# Generate random blocks of 512 to fill a 1MB array
bs = 512
num_blocks = 256
print('Generating random block from Zymkey ({!r} bytes)...'.format(bs * num_blocks))
random_bytes = []
for x in range(num_blocks):
    random_bytes += zymkey.client.get_random(bs)

# Encrypt the random data
print('Encrypting random block...')
encrypted = zymkey.client.lock(random_bytes)

# Decrypt the random data
print('Decrypting encrypted block...')
decrypted = zymkey.client.unlock(encrypted)

decrypted_list = list(decrypted)
random_list = list(random_bytes)

if decrypted_list == random_list:
    print('PASS: Decrypted data matches original random data')
else:
    print('Decrypted data does not match original random data')

# Turn off the LED
zymkey.client.led_off()

print('Done!')

# -------------------------------------------------------------------------------------------------




import zymkey
from textwrap import fill

print('Testing data lock...')
src = bytearray(b'\x01\x02\x03\x04')
dst = zymkey.client.lock(src)
print('Original Data')
s = fill(' '.join('{:02X}'.format(c) for c in src), 49)
print(s)
print('Encrypted Data')
s = fill(' '.join('{:02X}'.format(c) for c in dst), 49)
print(s)

print('Testing data unlock...')
new_src = dst
new_dst = zymkey.client.unlock(new_src)
print('Decryped Data')
s = fill(' '.join('{:02X}'.format(c) for c in new_dst), 49)
print(s)

print('Turning LED on...')
zymkey.client.led_on()

print('Testing get_random() with 512 bytes...')
num = 512
random_bytes = zymkey.client.get_random(num)
s = fill(' '.join('{:02X}'.format(c) for c in random_bytes), 49)
print(s)

print('Turning LED off...')
zymkey.client.led_off()

print('Flashing LED off, 500ms on, 100ms off...')
zymkey.client.led_flash(500, 100)

print('Testing zkCreateRandDataFile with 1MB...')
num = 1024 * 1024
file_path = '/tmp/r.bin'
zymkey.client.create_random_file(file_path, num)

print('Turning LED off...')
zymkey.client.led_off()

print('Testing get_ecdsa_public_key()...')
pk = zymkey.client.get_ecdsa_public_key()
s = fill(' '.join('{:02X}'.format(c) for c in pk), 49)
print(s)

print('Testing create_ecdsa_public_key_file()...')
zymkey.client.create_ecdsa_public_key_file('/tmp/pk.pem')


# ---------------------------------------------------------------
import zymkey

class ZymkeyFeatures(object):

    def __init__(self):
        self.zym = zymkey.client

    def createEcdsPublicKeyFile(self, path="/tmp/pk.pem", slot=0):
        try:
            self.zym.create_ecdsa_public_key_file(path, slot)
            return True
        except Exception as Err:
            print(f" ### ERROR ### {Err}")
            return False

    def getAccelerometerData(self):
        try:
            axis = ("x", "y", "z")
            accel_data = self.zym.get_accelerometer_data()
            return dict(map(lambda data,axis: (axis, [{"value":data.g_force, "tap_dir": data.tap_dir}]), accel_data, axis)) 
        except Exception as Err:
            print(f" ### ERROR ### {Err}")
            return False

    def lockUnlockPlainText(self, src, lock, dst=None, encryption_key='zymkey'):
        try:
            if dst:
                if lock:
                    self.zym.lock(src, dst, encryption_key)
                    return True
                self.zym.unlock(src, dst, encryption_key)
                return True
            else:
                if lock:
                    data = self.zym.lock(src, dst, encryption_key)
                    return data
                data = self.zym.unlock(src, dst, encryption_key)
                return data

        except Exception as Err:
            print(f" ### ERROR ### {Err}")
            return False

