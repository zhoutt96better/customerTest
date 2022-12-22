# coding: utf-8
import oci

config = oci.config.from_file()
# Initialize service client with default config file
artifacts_client = oci.artifacts.ArtifactsClient(config)
# Send the request to service, some parameters are not required, see API
# doc for more info
update_generic_artifact_response = artifacts_client.update_generic_artifact(
    artifact_id="ocid1.genericartifact.oc1.eu-frankfurt-1.0.amaaaaaagmaryaya235dpgjkaeoo6sg3ljplbmtc2owujyrq3hc4fybdpuaq")
# Get the data from response
print(update_generic_artifact_response.data)