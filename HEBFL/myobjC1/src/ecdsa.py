from __future__ import print_function

from binascii import hexlify

import bitcoin as b
from sha3 import keccak_256

from .util import tobe256, bytes_to_int, randb256


def pack_signature(v, r, s):
	"""
通过使用' s '的最后一位来存储' v '来节省一个字节。
将签名打包成两个256位字
这是可能的，因为' s '是' N '的模，并且是最高位
	"""
	assert v == 27 or v == 28
	v = (v - 27) << 255
	return tobe256(r), tobe256(s | v)


def unpack_signature(r, sv):
	sv = bytes_to_int(sv)
	if (sv & (1 << 255)):
		v = 28
		sv = sv ^ (1 << 255)
	else:
		v = 27
	return v, bytes_to_int(r), sv


def pubkey_to_ethaddr(pubkey):
	if isinstance(pubkey, tuple):
		assert len(pubkey) == 2
		pubkey = b.encode_pubkey(pubkey, 'bin')
	return hexlify(keccak_256(pubkey[1:]).digest()[12:])


def sign(messageHash, seckey):
	return pack_signature(*b.ecdsa_raw_sign(messageHash, seckey))


def recover(messageHash, r, sv):
	 return pubkey_to_ethaddr(b.ecdsa_raw_recover(messageHash, unpack_signature(r, sv)))


if __name__ == "__main__":
	# 验证新生成的密钥的随机样本最终不会设置取代'v'的'flag'位
	while True:
		print("Generating key")
		messageHash = randb256()
		seckey = randb256()
		pubkey = pubkey_to_ethaddr(b.privtopub(seckey))

		print("Signing")
		sig_t = b.ecdsa_raw_sign(messageHash, seckey)
		sig = sign(messageHash, seckey)
		assert unpack_signature(*sig) == sig_t

		print("Recovering")
		pubkey_v = recover(messageHash, *sig)
		print("Pubkey:", pubkey_v, pubkey)
		print("Message:", messageHash.encode('hex'))
		print("Sig:", sig[0].encode('hex'), sig[1].encode('hex'))
		assert pubkey == pubkey_v
