# This is an automatically generated code sample.
# To make this code sample work in your Oracle Cloud tenancy,
# please replace the values for any parameters whose current values do not fit
# your use case (such as resource IDs, strings containing ‘EXAMPLE’ or ‘unique_id’, and
# boolean, number, and enum parameters with values not fitting your use case).
import oci
# Create a default config using DEFAULT profile in default location
# Refer to
# https://docs.cloud.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm#SDK_and_CLI_Configuration_File
# for more info
config = oci.config.from_file()
# Initialize service client with default config file
artifacts_client = oci.artifacts.ArtifactsClient(config)
# Send the request to service, some parameters are not required, see API
# doc for more info
update_generic_artifact_response = artifacts_client.update_generic_artifact(
    artifact_id="ocid1.genericartifact.oc1.eu-frankfurt-1.0.amaaaaaagmaryaya235dpgjkaeoo6sg3ljplbmtc2owujyrq3hc4fybdpuaq")
# Get the data from response
print(update_generic_artifact_response.data)