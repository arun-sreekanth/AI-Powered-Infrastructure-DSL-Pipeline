import boto3
import base64
from botocore.exceptions import ClientError

class SecretAgent:
    def __init__(self):
        self.kms_client = boto3.client('kms')

    def decrypt_secret(self, encrypted_blob):
        try:
            response = self.kms_client.decrypt(CiphertextBlob=base64.b64decode(encrypted_blob))
            plaintext = response['Plaintext']
            return plaintext.decode('utf-8')
        except ClientError as e:
            print(f\"Error decrypting secret: {e}\")
            return None

    def run(self):
        print(\"🔐 Injecting secrets securely from AWS KMS\")
        # Example encrypted secret (replace with your encrypted value)
        encrypted_secret = \"<base64-encrypted-string>\"
        secret_value = self.decrypt_secret(encrypted_secret)
        if secret_value:
            print(f\"Secret: {secret_value}\")
        else:
            print(\"Failed to decrypt secret.\")
