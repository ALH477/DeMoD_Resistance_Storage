```
# xAI Artifact: Generated with Grok by xAI

import argparse
from typing import Dict, Callable

class CipherModule:
    """
    Modular cipher encryption/decryption for bitstreams.
    Supports registration of custom ciphers.
    """
    
    def __init__(self):
        self.ciphers: Dict[str, Dict[str, Callable[[str, str], str]]] = {}
        self.register_cipher('vigenere', self._vigenere_encrypt, self._vigenere_decrypt)
        self.register_cipher('caesar', self._caesar_encrypt, self._caesar_decrypt)
    
    def register_cipher(self, name: str, encrypt_func: Callable[[str, str], str], decrypt_func: Callable[[str, str], str]):
        self.ciphers[name.lower()] = {'encrypt': encrypt_func, 'decrypt': decrypt_func}
    
    def encrypt(self, bitstream: str, cipher_name: str, key: str) -> str:
        if not all(c in '01' for c in bitstream):
            raise ValueError("Input bitstream contains invalid characters (not binary)")
        if len(bitstream) == 0:
            raise ValueError("Input bitstream is empty")
        if not key:
            raise ValueError("Key cannot be empty")
        
        name = cipher_name.lower()
        if name not in self.ciphers:
            raise ValueError(f"No cipher registered for '{cipher_name}'")
        return self.ciphers[name]['encrypt'](bitstream, key)
    
    def decrypt(self, encrypted_bitstream: str, cipher_name: str, key: str) -> str:
        if not all(c in '01' for c in encrypted_bitstream):
            raise ValueError("Input encrypted bitstream contains invalid characters (not binary)")
        if len(encrypted_bitstream) == 0:
            raise ValueError("Input encrypted bitstream is empty")
        if not key:
            raise ValueError("Key cannot be empty")
        
        name = cipher_name.lower()
        if name not in self.ciphers:
            raise ValueError(f"No cipher registered for '{cipher_name}'")
        return self.ciphers[name]['decrypt'](encrypted_bitstream, key)
    
    def _caesar_encrypt(self, bitstream: str, key: str) -> str:
        try:
            shift = int(key) % 2
        except ValueError:
            raise ValueError("Caesar key must be an integer")
        return ''.join(str((int(bit) + shift) % 2) for bit in bitstream)
    
    def _caesar_decrypt(self, encrypted: str, key: str) -> str:
        try:
            shift = int(key) % 2
        except ValueError:
            raise ValueError("Caesar key must be an integer")
        return ''.join(str((int(bit) - shift) % 2) for bit in encrypted)
    
    def _vigenere_encrypt(self, bitstream: str, key: str) -> str:
        key_bits = ''.join(f'{ord(c):08b}' for c in key)
        if not key_bits:
            raise ValueError("Vigenere key generated empty bitstream")
        key_len = len(key_bits)
        return ''.join(str(int(bit) ^ int(key_bits[i % key_len])) for i, bit in enumerate(bitstream))
    
    def _vigenere_decrypt(self, encrypted: str, key: str) -> str:
        return self._vigenere_encrypt(encrypted, key)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Cipher module CLI.")
    parser.add_argument("action", choices=['encrypt', 'decrypt'], help="Action to perform")
    parser.add_argument("bitstream", type=str, help="Bitstream (or path to file with --file)")
    parser.add_argument("--cipher", default="vigenere", help="Cipher name")
    parser.add_argument("--key", required=True, help="Encryption/decryption key")
    parser.add_argument("--file", action="store_true", help="Treat bitstream as file path")
    args = parser.parse_args()
    
    cm = CipherModule()
    try:
        if args.file:
            with open(args.bitstream, 'r') as f:
                bitstream = f.read().strip()
        else:
            bitstream = args.bitstream
        
        if args.action == 'encrypt':
            result = cm.encrypt(bitstream, args.cipher, args.key)
        else:
            result = cm.decrypt(bitstream, args.cipher, args.key)
        
        print(f"Result: {result[:100]}...")
    except (ValueError, FileNotFoundError, OSError) as e:
        print(f"Error: {str(e)}")
```
