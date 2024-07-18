https://app.rkvst-poc.io/archivist/publicassets/ee77200d-796b-44e8-abb1-773ca6efe768

Browse to: https://app.rkvst-poc.io/archivist/publicassets/$ID
https://app.rkvst-poc.io/archivist/v2/attachments/publicassets/$ID

curl https://app.rkvst-poc.io/archivist/v2/attachments/publicassets/ee77200d-796b-44e8-abb1-773ca6efe768
curl https://app.rkvst-poc.io/archivist/v2/attachments/publicassets/ee77200d-796b-44e8-abb1-773ca6efe768

curl https://app.rkvst-poc.io/archivist/publicassets/$ID | jq

curl https://app.rkvst-poc.io/archivist/publicassets/$ID/ | jq



```
feed = {
  "id" : : tstr
  * tstr => any
}
```

Protected_Header = {
  ...
  392 => tstr            ; Feed
  393 => Reg_Info        ; Registration Policy info
}





Would you / should you trust downloading this file?
curl --output file.jpg https://app.rkvst-poc.io/archivist/v2/attachments/publicassets/ee77200d-796b-44e8-abb1-773ca6efe768/292b152f-628e-4ebc-9845-09cd8a6075d0

no!
Let's get some confidence:

ID=ee77200d-796b-44e8-abb1-773ca6efe768
curl https://app.rkvst-poc.io/archivist/publicassets/$ID | jq

Woo, this json makes me confident (why, I don't yet)

curl https://app.rkvst-poc.io/archivist/publicassets/$ID | jq  (get the attributes.arc_primary_image.arc_blob_identity (parse/blobs out))

ATTACHMENT=292b152f-628e-4ebc-9845-09cd8a6075d0
curl --output file.jpg https://app.rkvst-poc.io/archivist/v2/attachments/publicassets/{$ID}/{$ATTACHMENT}
821538bf-c1f3-42cc-9c76-496d0a4d34fc


```json
```