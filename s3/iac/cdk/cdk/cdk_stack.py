from aws_cdk import (
    # Duration,
    Stack,
    aws_s3 as s3,
    App,
    Environment
    # aws_sqs as sqs,
)
from constructs import Construct

class CdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        bucket = s3.Bucket(self, "MyFirstBucket-9973")
        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "CdkQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )

app = App()
CdkStack(app, "S3CDKStack", 
         env = Environment(account='522732149164', region='ap-south-1'),
         )
app.synth()