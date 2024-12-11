import cbor2
import json
from hashlib import sha256

from datatrails_scitt_samples.statement_creation import (
    cose_key_ec2_p256,
    create_hashed_signed_statement,
    create_hashed_statement,
)

from datatrails_scitt_samples.cbor_header_labels import (
    HEADER_LABEL_CWT_CNF,
    HEADER_LABEL_CNF_COSE_KEY,
    HEADER_LABEL_PAYLOAD_HASH_ALGORITHM,
    HEADER_LABEL_LOCATION,
)

from pycose import headers
from pycose.messages import Sign1Message
from pycose.keys.curves import P256
from pycose.keys.keyparam import KpKty, EC2KpX, EC2KpY, KpKeyOps, EC2KpCurve
from pycose.keys.keytype import KtyEC2
from pycose.keys.keyops import VerifyOp
from pycose.keys import CoseKey

def open_signing_key(key_file: str) -> SigningKey:
    """
    opens the signing key from the key file.
    NOTE: the signing key is expected to be a P-256 ecdsa key in PEM format.
    """
    with open(key_file, encoding="UTF-8") as file:
        signing_key = SigningKey.from_pem(file.read(), hashlib.sha256)
        return signing_key

# Set SCITT COSE Header Parameters
issuer = "testissuer"
kid = b"testkey"
subject = "testsubject"


# Create a Hash of a statement
# uses: https://cose-wg.github.io/draft-ietf-cose-hash-envelope/draft-ietf-cose-hash-envelope.html

# Create a Statement
statement = {"author": "fred", "title": "my biography", "reviews": "mixed"}
# load the Statement
payload_contents = json.dumps(statement)

# Hash the statement
payload_hash = sha256(payload_contents.encode("utf-8")).digest()

# Set info how the hash was created
payload_hash_alg = "SHA-256"
payload_preimage_content_type = "application/json"

# Set an optional location for where the statement may be stored
payload_location = f"https://storage.example/{subject}"

# Provide Key/Value pairs for indexing
# uses: https://github.com/SteveLasker/cose-meta-map
meta_map_dict = {"key1": "value1", "key2": "42"}

# Open the signing key, based on a local private key
# TODO: This should be inverted to create the To Be Signed Bytes
# TODO: which may be signed remotely, or locally
# TODO: then create the signed statement
signing_key = open_signing_key(args.signing_key_file)

signed_statement = create_hashed_signed_statement(
  content_type=content_type,
  issuer=issuer,
  kid=kid,
  subject=subject,
  meta_map=meta_map_dict,
  payload=payload_hash,
  payload_hash_alg=payload_hash_alg,
  payload_location=payload_location,
  signing_key=signing_key
)

