---
title: "Blobs API"
description: "Blobs API Reference"
lead: "Blobs API Reference"
date: 2021-06-09T13:32:57+01:00
lastmod: 2021-06-09T13:32:57+01:00
draft: false
images: []
menu: 
  developers:
    parent: "api-reference"
weight: 109
toc: true
aliases: 
  - /docs/api-reference/blobs-api/
---
{{< note >}}
**Note:** This page is primarily intended for developers who will be writing applications that will use DataTrails for provenance.
If you are looking for a simple way to test our API you might prefer our [Postman collection](https://www.postman.com/datatrails-inc/workspace/datatrails-public/overview), the [YAML runner](/developers/yaml-reference/story-runner-components/) or the [Developers](https://app.datatrails.ai) section of the web UI.

Additional YAML examples can be found in the articles in the [Overview](/platform/overview/introduction/) section.
{{< /note >}}

## Blob API Examples

The Blobs API enables you to upload Binary Large OBjects (BLOBs) such as documents, process artifacts and images to attach to your evidence ledger.

{{< note >}}
**Note:** Blobs cannot be searched or listed as a collection in their own right: they must always be associated with an Asset or Event through an Attachment Attribute and can only be downloaded by users with appropriate access rights to that Attachment.
Take note of the Blob ID returned in the API response, it will be needed for use with Assets and Events.<br>
For information on Attachments and how to implement them, please refer to [the Events API Reference](../events-api/#adding-attachments).
{{< /note >}}

Create the [bearer_token](/developers/developer-patterns/getting-access-tokens-using-app-registrations) and store in a file in a secure local directory with 0600 permissions.

### Sample Attachment

An attachment can be any type of file, from media files to code files.
The sample uses Fyodor (cat.jpg), but the `BLOB_FILE` can be replaced with any content you desire:

- Download a picture of Fyodor, or select another file for upload:

  ```bash
  curl https://app.datatrails.ai/archivist/v2/attachments/publicassets/208c5282-750e-4302-86f8-eb751de89005/events/4161673f-efa4-4391-bf06-347edd53024e/dae5a430-7d2e-4b88-b753-c09bdcc48c33 \
    -o cat.jpg
  ```

### Upload a Blob

- Identify the file to upload:

  ```bash
  BLOB_FILE=./cat.jpg
  ```

- Upload the blob stored at /path/to/file:

  ```bash
  curl -X POST \
      -H "@$HOME/.datatrails/bearer-token.txt" \
      -H "content_type=image/jpg" \
      -F "file=@$BLOB_FILE" \
      https://app.datatrails.ai/archivist/v1/blobs \
      | jq
  ```

  The response:

  ```json
  {
    "hash": {
      "alg": "SHA256",
      "value": "h123456"
    },
    "identity": "blobs/b123467-8901",
    "mime_type": "image/jpeg",
    "size": 21779,
    "tenantid": "t1234567-8901-xxxx-xxxx-xxxxxxxxxxxx",
    "timestamp_accepted": "2025-01-27T23:45:29Z"
  }
  ```

### Retrieve a Blob

- Capture the Blob identity from the above POST.  
  Note, the `<blob-id>` combines `blobs/` and the ID  
  example:`"identity": "blobs/b123467-8901"` becomes `BLOB_ID=blobs/b123467-8901`:

  ```bash
  BLOB_ID=<blob-id>
  ```

- Retrieve a specific Blob, downloading the `cat.jpg` file:

  ```bash
  curl -H "@$HOME/.datatrails/bearer-token.txt" \
      -H "content_type=image/jpg" \
      --output "$BLOB_FILE" \
      https://app.datatrails.ai/archivist/v1/$BLOB_ID
  ```

### Finding Blobs

The Blobs API does not support a discovery or query API that lists all possible blobs.
Blobs are discovered through their usage within the DataTrails platform, such as the [Attachments API](/developers/api-reference/attachments-api/) or the primary image of an Asset or Event.
Through the Attachments API, capture the value of the `"arc_blob_identity"`, nested below a named attribute with an `"arc_attribute_type": "arc_attachment"`:

```json
{
  "event_attributes": {
    "conformance_report": {
      "arc_attribute_type": "arc_attachment",
      "arc_blob_identity": "blobs/b123456-7890",
      "arc_blob_hash_value": "h123456",
      "arc_blob_hash_alg": "SHA256",
      "arc_file_name": "Conformance.pdf"
    }
  }
}
```

## Blobs OpenAPI Docs

{{< openapi url="https://raw.githubusercontent.com/datatrails/datatrails-openapi/main/doc/blobsv1.swagger.json" >}}
