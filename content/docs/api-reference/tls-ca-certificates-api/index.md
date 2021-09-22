---
title: "TLS CA Certificates API"
description: "TLS CA Certificates API Reference"
lead: "TLS CA Certificates API Reference"
date: 2021-06-09T13:53:24+01:00
lastmod: 2021-06-09T13:53:24+01:00
draft: false
images: []
menu: 
  docs:
    parent: "api-reference"
weight: 114
toc: true
---

## TLS CA Certificates API Examples

Create the [bearer_token](../../setup-and-administration/getting-access-tokens-using-client-secret) and store in a file in a secure local directory with 0600 permissions.

Set the URL (for example):

```bash
export URL=https://app.rkvst.io 
```

### TLS CA Certificate Upload

Define the TLS CA certificate parameters and store in `/path/to/jsonfile` (certificate field shortened for brevity):

```json
{
    "display_name": "Some description",
    "certificate": "-----BEGIN CERTIFICATE-----\nMIIFxDCCA6ygAwIBAgIBAjANBgkqhkiG9w0BAQsFADCBsDELMAkGA1UEBhMCVVMx\nETAPBgNV....1NF/BjDZ4wdexw==\n-----END CERTIFICATE-----\n"
}
```

To include the PEM file content in a JSON string it must be flattened to a single line.

To create a single line representation of a PEM file for the RKVST API, you must replace new lines with the literal string “\n”. 

The following unix command could be used:

```bash
awk 'NF {sub(/\r/, ""); printf "%s\\n",$0;}' cert-name.pem
```

Create the CA Certificate:

```bash
curl -v -X POST \
    -H "@$BEARER_TOKEN_FILE" \
    -H "Content-type: application/json" \
    -d "@/path/to/jsonfile" \
    $URL/archivist/v1/tlscacertificates
```

The response is (certificate field shortened for brevity):

```json
{
    "identity": "tlscacertificates/3f5be24f-fd1b-40e2-af35-ec7c14c74d53",
    "display_name": "Some description",
    "certificate": "-----BEGIN CERTIFICATE----- MIIEBDCCAuygAwIBAgIDAjppMA0GCSqGSIb3DQEBBQUAMEIxCzAJBgNVBAYTAlVT -----END CERTIFICATE-----"
}
```

### TLS CA Certificate Retrieval

TLS CA Certificate records in RKVST are tokenized at creation time and referred to in all API calls and smart contracts throughout the system by a unique identity of the form:

```bash
tlscacertificates/12345678-90ab-cdef-1234-567890abcdef
```

If you do not know the certificate’s identity you can fetch TLS CA Certificate records using other information you do know, such as the certificate’s name.

#### Fetch all TLS CA Certificates

To fetch all TLS CA certificates records, simply `GET` the `tlscacertificates` resource:

```bash
curl -v -X GET \
     -H "@$BEARER_TOKEN_FILE" \
     $URL/archivist/v1/tlscacertificates
```

#### Fetch specific TLS CA Certificate by Identity

If you know the unique identity of the TLS CA certificate Record simply `GET` the resource:

```bash
curl -v -X GET \
     -H "@$BEARER_TOKEN_FILE" \
     $URL/archivist/v1/tlscacertificates/6a951b62-0a26-4c22-a886-1082297b063b
```

#### Fetch TLS CA Certificates by Name

To fetch all TLS CA Certificates with a specific name, `GET` the `tlscacertificates` resource and filter on `display_name`:

```bash
curl -g -v -X GET \
     -H "@$BEARER_TOKEN_FILE" \
     $URL/archivist/v1/tlscacertificates?display_name=Acme
```

Each of these calls returns a list of matching TLS CA Certificate records in the form (certificate field shortened for brevity):

```json
{
    "certificates": [
        {
            "identity": "tlscacertificates/6a951b62-0a26-4c22-a886-1082297b063b",
            "display_name": "Some description",
            "certificate": "-----BEGIN CERTIFICATE----- MIIEBDCCAuygAwIBAgIDAjppMA0GCSqGSIb3DQEBBQUAMEIxCzAJBgNVBAYTAlVT -----END CERTIFICATE----- "
        },
        {
            "identity": "tlscacertificates/12345678-0a26-4c22-a886-1082297b063b",
            "display_name": "Some other description",
            "certificate": "-----BEGIN CERTIFICATE----- XYZEBDCCAuygAwIBAgIDAjppMA0GCSqGSIb3DQEBBQUAMEIxCzAJBgNVBAYTAlVT -----END CERTIFICATE----- "
        }
    ]
}
```

#### TLS CA Certificate Deletion

To delete a TLS CA Certificate, issue the following request:

```bash
curl -v -X DELETE \
    -H "@$BEARER_TOKEN_FILE" \
    -H "Content-type: application/json" \
    $URL/archivist/v1/tlscacertificates/47b58286-ff0f-11e9-8f0b-362b9e155667
```

The response is `{}`.

#### Updating a TLS CA Certificate

Define the TLS CA certificates parameters to be changed and store in /path/to/jsonfile:

```json
{
    "display_name": "new description"
}
```

Update the TLS CA Certificate:

```bash
curl -v -X PATCH \
    -H "@$BEARER_TOKEN_FILE" \
    -H "Content-type: application/json" \
    -d "@/path/to/jsonfile" \
    $URL/archivist/v1/tlscacertificates/47b58286-ff0f-11e9-8f0b-362b9e155667
```

The response is (certificate field shortened for brevity):

```json
{
    "identity": "tlscacertificates/3f5be24f-fd1b-40e2-af35-ec7c14c74d53",
    "display_name": "Some description",
    "certificate": "-----BEGIN CERTIFICATE----- MIIEBDCCAuygAwIBAgIDAjppMA0GCSqGSIb3DQEBBQUAMEIxCzAJBgNVBAYTAlVT -----END CERTIFICATE-----"
}
```

## TLS CA Certificates OpenAPI Docs

{{< openapi url="https://raw.githubusercontent.com/jitsuin-inc/archivist-docs/master/doc/openapi/tlscacertificatesv1.swagger.json" >}}
